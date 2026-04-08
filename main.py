from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from neo4j import GraphDatabase
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Radiology Knowledge Graph API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── BAĞLANTILAR ───────────────────────────────────────────────────────────────
driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_ANON_KEY")
)


# ── MODELLER ──────────────────────────────────────────────────────────────────

class DiagnoseRequest(BaseModel):
    organ: str
    modality: str
    finding_ids: List[str]
    clinical_context_ids: Optional[List[str]] = []

class FindingsRequest(BaseModel):
    organ: str
    modality: str

class QuizAnswerRequest(BaseModel):
    user_id: str
    question_id: str
    concept_id: str
    organ: str
    user_answer: int
    score: int
    time_spent_ms: int


# ── TEMEL ENDPOINTS ───────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "ok", "message": "Radiology KG API çalışıyor"}


@app.get("/organs")
def get_organs():
    with driver.session() as session:
        result = session.run("MATCH (o:Organ) RETURN o ORDER BY o.name")
        return [dict(r["o"]) for r in result]


@app.post("/findings")
def get_findings(req: FindingsRequest):
    with driver.session() as session:
        result = session.run("""
            MATCH (m:Modality {id: $modality})-[:HAS_FINDING]->(f:Finding)
            WHERE f.organ = $organ
            RETURN f ORDER BY f.sequence, f.display_order
        """, organ=req.organ, modality=req.modality)

        findings = [dict(r["f"]) for r in result]
        grouped = {}
        for f in findings:
            seq = f.get("sequence", "diger")
            if seq not in grouped:
                grouped[seq] = []
            grouped[seq].append(f)

        return {"organ": req.organ, "modality": req.modality, "grouped": grouped}


@app.post("/diagnose")
def diagnose(req: DiagnoseRequest):
    if not req.finding_ids:
        raise HTTPException(status_code=400, detail="En az bir bulgu seçilmeli")

    with driver.session() as session:
        suggests_result = session.run("""
            MATCH (f:Finding)-[r:SUGGESTS]->(d:Diagnosis)
            WHERE f.id IN $finding_ids AND d.organ = $organ
            WITH d,
                 sum(r.weight) as base_score,
                 collect({finding: f.name, weight: r.weight, required: r.required, source: r.source}) as matched_findings,
                 collect(CASE WHEN r.required = true THEN f.id ELSE null END) as required_findings
            RETURN d, base_score, matched_findings, required_findings
        """, finding_ids=req.finding_ids, organ=req.organ)

        diagnoses_raw = []
        for r in suggests_result:
            d = dict(r["d"])
            diagnoses_raw.append({
                "diagnosis": d,
                "base_score": r["base_score"],
                "matched_findings": r["matched_findings"],
                "required_findings": [x for x in r["required_findings"] if x],
            })

        if not diagnoses_raw:
            return {"diagnoses": [], "message": "Eşleşen tanı bulunamadı"}

        excludes_result = session.run("""
            MATCH (f:Finding)-[r:EXCLUDES]->(d:Diagnosis)
            WHERE f.id IN $finding_ids
            RETURN d.id as diagnosis_id, sum(r.weight) as exclude_score
        """, finding_ids=req.finding_ids)
        exclude_map = {r["diagnosis_id"]: r["exclude_score"] for r in excludes_result}

        multiplier_map = {}
        if req.clinical_context_ids:
            ctx_result = session.run("""
                MATCH (c:ClinicalContext)-[r:MODIFIES_WEIGHT]->(d:Diagnosis)
                WHERE c.id IN $context_ids AND r.finding_id IN $finding_ids
                RETURN d.id as diagnosis_id, max(r.multiplier) as multiplier
            """, context_ids=req.clinical_context_ids, finding_ids=req.finding_ids)
            multiplier_map = {r["diagnosis_id"]: r["multiplier"] for r in ctx_result}

        results = []
        for item in diagnoses_raw:
            d = item["diagnosis"]
            did = d["id"]
            base = item["base_score"]
            excl = exclude_map.get(did, 0)
            mult = multiplier_map.get(did, 1.0)
            final_score = (base - excl) * mult
            if final_score <= 0:
                continue

            confidence = min(round((final_score / 3.0) * 100), 99)
            results.append({
                "id":              did,
                "name":            d.get("name"),
                "risk_level":      d.get("risk_level"),
                "lirads":          d.get("lirads"),
                "icd10":           d.get("icd10"),
                "source":          d.get("source"),
                "report_template": d.get("report_template"),
                "confidence":      confidence,
                "base_score":      round(base, 3),
                "exclude_score":   round(excl, 3),
                "multiplier":      mult,
                "final_score":     round(final_score, 3),
                "matched_findings": item["matched_findings"],
            })

        results.sort(key=lambda x: x["final_score"], reverse=True)

        if results:
            top_ids = [r["id"] for r in results[:5]]
            actions_result = session.run("""
                MATCH (d:Diagnosis)-[r:REQUIRES_ACTION]->(a:Action)
                WHERE d.id IN $diagnosis_ids
                WITH d.id as diagnosis_id, a, r.order as ord
                ORDER BY ord
                RETURN diagnosis_id,
                       collect({id: a.id, name: a.name, urgency: a.urgency,
                                urgency_level: a.urgency_level, order: ord}) as actions
            """, diagnosis_ids=top_ids)
            action_map = {r["diagnosis_id"]: r["actions"] for r in actions_result}
            for res in results:
                res["actions"] = sorted(
                    action_map.get(res["id"], []),
                    key=lambda x: x.get("order", 99)
                )

        if results:
            diff_result = session.run("""
                MATCH (d1:Diagnosis {id: $top_id})-[r:DIFFERENTIATES_FROM]->(d2:Diagnosis)
                RETURN d2.name as name, r.key_finding as key_finding, r.modality as modality
            """, top_id=results[0]["id"])
            results[0]["differentials"] = [
                {"name": r["name"], "key_finding": r["key_finding"], "modality": r["modality"]}
                for r in diff_result
            ]

        return {
            "organ": req.organ, "modality": req.modality,
            "findings": req.finding_ids, "contexts": req.clinical_context_ids,
            "diagnoses": results
        }


@app.get("/clinical-contexts")
def get_clinical_contexts():
    with driver.session() as session:
        result = session.run("MATCH (c:ClinicalContext) RETURN c ORDER BY c.name")
        return [dict(r["c"]) for r in result]


# ── ÖĞRENME ENDPOINTS ─────────────────────────────────────────────────────────

@app.get("/learn/map/{organ}")
def get_learning_map(organ: str):
    """Organ için öğrenme haritası"""
    with driver.session() as session:
        concepts = session.run("""
            MATCH (c:Concept {organ: $organ})
            RETURN c ORDER BY c.level, c.category
        """, organ=organ)

        prereqs = session.run("""
            MATCH (c1:Concept {organ: $organ})-[:PREREQUISITE_OF]->(c2:Concept {organ: $organ})
            RETURN c1.id as from_id, c2.id as to_id
        """, organ=organ)

        return {
            "organ": organ,
            "concepts": [dict(r["c"]) for r in concepts],
            "prerequisites": [{"from": r["from_id"], "to": r["to_id"]} for r in prereqs]
        }


@app.get("/learn/concept/{concept_id}")
def get_concept(concept_id: str):
    """Concept detayı + sorular + ilgili tanılar"""
    with driver.session() as session:
        result = session.run("""
            MATCH (c:Concept {id: $id})
            OPTIONAL MATCH (c)-[:PREREQUISITE_OF]->(next:Concept)
            OPTIONAL MATCH (prev:Concept)-[:PREREQUISITE_OF]->(c)
            OPTIONAL MATCH (c)-[:RELATES_TO]->(d:Diagnosis)
            RETURN c,
                collect(DISTINCT {id: next.id, name: next.name}) as unlocks,
                collect(DISTINCT {id: prev.id, name: prev.name}) as requires,
                collect(DISTINCT {id: d.id, name: d.name, risk_level: d.risk_level}) as diagnoses
        """, id=concept_id)

        row = result.single()
        if not row:
            raise HTTPException(status_code=404, detail="Concept bulunamadı")

        questions = session.run("""
            MATCH (q:Question)-[:TESTS]->(c:Concept {id: $id})
            RETURN q ORDER BY q.level
        """, id=concept_id)

        return {
            **dict(row["c"]),
            "unlocks":   [x for x in row["unlocks"]  if x["id"]],
            "requires":  [x for x in row["requires"]  if x["id"]],
            "diagnoses": [x for x in row["diagnoses"] if x["id"]],
            "questions": [dict(r["q"]) for r in questions]
        }


@app.get("/learn/questions/{concept_id}")
def get_questions(concept_id: str):
    """Concept için sorular — cevaplar gizli"""
    with driver.session() as session:
        result = session.run("""
            MATCH (q:Question)-[:TESTS]->(c:Concept {id: $id})
            RETURN q ORDER BY q.level
        """, id=concept_id)

        questions = []
        for r in result:
            q = dict(r["q"])
            q.pop("correct", None)
            q.pop("explanation", None)
            questions.append(q)

        return {"concept_id": concept_id, "questions": questions}


@app.get("/learn/question/{question_id}/answer")
def get_answer(question_id: str):
    """Sorunun doğru cevabı ve açıklaması"""
    with driver.session() as session:
        result = session.run("""
            MATCH (q:Question {id: $id})
            RETURN q.correct as correct, q.explanation as explanation
        """, id=question_id)

        row = result.single()
        if not row:
            raise HTTPException(status_code=404, detail="Soru bulunamadı")

        return {"correct": row["correct"], "explanation": row["explanation"]}


# ── SM-2 ENDPOINTS ────────────────────────────────────────────────────────────

@app.post("/quiz/answer")
def submit_answer(req: QuizAnswerRequest):
    """Cevapla → SM-2 hesapla → Supabase'e kaydet"""
    with driver.session() as session:
        result = session.run("""
            MATCH (q:Question {id: $id})
            RETURN q.correct as correct, q.explanation as explanation
        """, id=req.question_id)
        row = result.single()
        if not row:
            raise HTTPException(status_code=404, detail="Soru bulunamadı")

        is_correct  = (req.user_answer == row["correct"])
        explanation = row["explanation"]

    # Quiz geçmişine kaydet
    supabase.table("quiz_history").insert({
        "user_id":       req.user_id,
        "question_id":   req.question_id,
        "concept_id":    req.concept_id,
        "organ":         req.organ,
        "is_correct":    is_correct,
        "user_answer":   req.user_answer,
        "score":         req.score,
        "time_spent_ms": req.time_spent_ms
    }).execute()

    # SM-2 hesapla
    sm2_result = supabase.rpc("calculate_sm2", {
        "p_user_id":    req.user_id,
        "p_concept_id": req.concept_id,
        "p_score":      req.score
    }).execute()

    return {
        "is_correct":  is_correct,
        "explanation": explanation,
        "sm2":         sm2_result.data
    }


@app.get("/quiz/due/{user_id}")
def get_due_reviews(user_id: str):
    """Bugün tekrar edilecek conceptler"""
    result = supabase.rpc("get_due_reviews", {
        "p_user_id": user_id
    }).execute()

    due_concepts = result.data or []

    if due_concepts:
        concept_ids = [c["concept_id"] for c in due_concepts]
        with driver.session() as session:
            neo_result = session.run("""
                MATCH (c:Concept) WHERE c.id IN $ids RETURN c
            """, ids=concept_ids)
            concept_map = {dict(r["c"])["id"]: dict(r["c"]) for r in neo_result}

        for c in due_concepts:
            c["concept"] = concept_map.get(c["concept_id"], {})

    return {"due_count": len(due_concepts), "concepts": due_concepts}


@app.get("/quiz/progress/{user_id}")
def get_user_progress(user_id: str):
    """Kullanıcı ilerleme özeti"""
    result = supabase.table("user_progress") \
        .select("*").eq("user_id", user_id).execute()

    progress = result.data or []
    total  = len(progress)
    strong = len([p for p in progress if p["strength"] >= 4])
    weak   = len([p for p in progress if p["strength"] <= 1 and p["n"] > 0])

    return {
        "total_concepts": total,
        "strong":  strong,
        "weak":    weak,
        "details": progress
    }


@app.get("/quiz/stats/{user_id}")
def get_user_stats(user_id: str):
    """Son 7 günlük istatistikler"""
    result = supabase.table("daily_stats") \
        .select("*").eq("user_id", user_id) \
        .order("date", desc=True).limit(7).execute()

    return {"stats": result.data or []}


@app.on_event("shutdown")
def shutdown():
    driver.close()

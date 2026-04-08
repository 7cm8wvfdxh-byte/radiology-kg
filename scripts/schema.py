from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI      = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# ── ADIM 1: Constraint'ler — her biri ayrı session.run() ─────────────────────
constraints = [
    "CREATE CONSTRAINT IF NOT EXISTS FOR (o:Organ) REQUIRE o.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (m:Modality) REQUIRE m.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (f:Finding) REQUIRE f.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (d:Diagnosis) REQUIRE d.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (a:Action) REQUIRE a.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (c:ClinicalContext) REQUIRE c.id IS UNIQUE",
]

with driver.session() as session:
    for c in constraints:
        session.run(c)
print("✓ Constraints oluşturuldu")

# ── ADIM 2: Organ düğümleri ───────────────────────────────────────────────────
def create_organs(tx):
    organs = [
        {"id": "liver",    "name": "Karaciğer", "name_en": "Liver"},
        {"id": "brain",    "name": "Beyin",     "name_en": "Brain"},
        {"id": "lung",     "name": "Akciğer",   "name_en": "Lung"},
        {"id": "kidney",   "name": "Böbrek",    "name_en": "Kidney"},
        {"id": "pancreas", "name": "Pankreas",  "name_en": "Pancreas"},
    ]
    for o in organs:
        tx.run("MERGE (o:Organ {id: $id}) SET o.name = $name, o.name_en = $name_en", **o)
    return len(organs)

# ── ADIM 3: Modality düğümleri ────────────────────────────────────────────────
def create_modalities(tx):
    modalities = [
        {"id": "us", "name": "Ultrasonografi",         "name_en": "Ultrasound"},
        {"id": "ct", "name": "Bilgisayarlı Tomografi",  "name_en": "CT"},
        {"id": "mr", "name": "Manyetik Rezonans",       "name_en": "MRI"},
    ]
    for m in modalities:
        tx.run("MERGE (m:Modality {id: $id}) SET m.name = $name, m.name_en = $name_en", **m)
    return len(modalities)

# ── ADIM 4: Organ → Modality ilişkileri ──────────────────────────────────────
def create_organ_modality_relations(tx):
    relations = [
        ("liver",    "us"), ("liver",    "ct"), ("liver",    "mr"),
        ("brain",    "ct"), ("brain",    "mr"),
        ("lung",     "ct"), ("lung",     "mr"),
        ("kidney",   "us"), ("kidney",   "ct"), ("kidney",   "mr"),
        ("pancreas", "us"), ("pancreas", "ct"), ("pancreas", "mr"),
    ]
    for organ_id, modality_id in relations:
        tx.run("""
            MATCH (o:Organ {id: $organ_id})
            MATCH (m:Modality {id: $modality_id})
            MERGE (o)-[:HAS_MODALITY]->(m)
        """, organ_id=organ_id, modality_id=modality_id)
    return len(relations)

# ── ADIM 5: ClinicalContext düğümleri ────────────────────────────────────────
def create_clinical_contexts(tx):
    contexts = [
        {"id": "cirrhosis",          "name": "Siroz",                   "description": "Herhangi bir etiyolojide karaciğer sirozu"},
        {"id": "chronic_hbv",        "name": "Kronik HBV",              "description": "Kronik hepatit B enfeksiyonu"},
        {"id": "known_malignancy",   "name": "Bilinen Malignite",        "description": "Aktif veya öyküde primer malignite"},
        {"id": "normal_background",  "name": "Normal Zemin",            "description": "Bilinen karaciğer hastalığı yok"},
        {"id": "young_female_ocs",   "name": "Genç Kadın / OKS",        "description": "OKS kullanımı, obezite — adenom riski"},
        {"id": "young_female_asymp", "name": "Genç Kadın Asemptomatik", "description": "FNH için tipik demografik"},
        {"id": "prior_hcc",          "name": "Önceki HKH",              "description": "Daha önce HKH tanısı almış"},
    ]
    for c in contexts:
        tx.run("""
            MERGE (c:ClinicalContext {id: $id})
            SET c.name = $name, c.description = $description
        """, **c)
    return len(contexts)

# ── ADIM 6: Action düğümleri ──────────────────────────────────────────────────
def create_actions(tx):
    actions = [
        {"id": "mdt",              "name": "MDT'ye Yönlendir",         "urgency": "kritik",  "urgency_level": 1},
        {"id": "biopsy",           "name": "Biyopsi",                  "urgency": "yuksek",  "urgency_level": 2},
        {"id": "multiphase_ct",    "name": "Multifazik BT",            "urgency": "yuksek",  "urgency_level": 2},
        {"id": "multiphase_mr",    "name": "Multifazik MR",            "urgency": "yuksek",  "urgency_level": 2},
        {"id": "gadoxetate_mr",    "name": "Gadoxetat MR (Primovist)", "urgency": "orta",    "urgency_level": 3},
        {"id": "ceus",             "name": "CEUS",                     "urgency": "orta",    "urgency_level": 3},
        {"id": "mrcp",             "name": "MRCP",                     "urgency": "orta",    "urgency_level": 3},
        {"id": "followup_3m_ct",   "name": "3 Ay BT/MR Kontrol",       "urgency": "orta",    "urgency_level": 3},
        {"id": "followup_6m_us",   "name": "6 Ay US Takip",            "urgency": "elektif", "urgency_level": 4},
        {"id": "no_followup",      "name": "Takip Gerekmez",           "urgency": "elektif", "urgency_level": 5},
        {"id": "afp",              "name": "AFP Tetkiki",              "urgency": "yuksek",  "urgency_level": 2},
        {"id": "ca199_cea",        "name": "CA 19-9, CEA",             "urgency": "orta",    "urgency_level": 3},
        {"id": "staging_ct",       "name": "Evreleme BT (TAP)",        "urgency": "kritik",  "urgency_level": 1},
        {"id": "surgical_consult", "name": "Cerrahi Konsültasyon",     "urgency": "yuksek",  "urgency_level": 2},
        {"id": "hydatid_serology", "name": "Hidatik Seroloji",         "urgency": "orta",    "urgency_level": 3},
        {"id": "ocs_cessation",    "name": "OKS Kesimi",               "urgency": "yuksek",  "urgency_level": 2},
    ]
    for a in actions:
        tx.run("""
            MERGE (a:Action {id: $id})
            SET a.name = $name, a.urgency = $urgency, a.urgency_level = $urgency_level
        """, **a)
    return len(actions)


# ── ÇALIŞTIR ──────────────────────────────────────────────────────────────────
with driver.session() as session:
    n = session.execute_write(create_organs)
    print(f"✓ {n} Organ düğümü")

with driver.session() as session:
    n = session.execute_write(create_modalities)
    print(f"✓ {n} Modality düğümü")

with driver.session() as session:
    n = session.execute_write(create_organ_modality_relations)
    print(f"✓ {n} Organ-Modality ilişkisi")

with driver.session() as session:
    n = session.execute_write(create_clinical_contexts)
    print(f"✓ {n} ClinicalContext düğümü")

with driver.session() as session:
    n = session.execute_write(create_actions)
    print(f"✓ {n} Action düğümü")

driver.close()
print("\n✓ Şema başarıyla oluşturuldu.")

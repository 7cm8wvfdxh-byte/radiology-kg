from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

CONCEPTS = [

    # ── KATMAN 4: AYIRıCI TANI ZİNCİRLERİ ───────────────────────────────────

    {
        "id": "dd_hypervascular_lesion",
        "name": "Hipervasküler Lezyon Ayırıcı Tanı Zinciri",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "Arteryel fazda parlayan her lezyon HKH değildir. HKH, FNH, adenom, hemanjiom (flash fill), hipervasküler metastaz, arteryovenöz şant ayrımı sistematik yapılmalı.",
        "why_matters": "Arteryel enhancement görünce refleks 'HKH' diyemezsin. Klinik bağlam, ek bulgular ve washout durumu ayırımı belirler. Yanlış tanı yanlış tedavi.",
        "key_points": [
            "APHE + washout + siroz → HKH (LR-5)",
            "APHE + washout YOK + HBP hiperintens → FNH",
            "APHE + washout YOK + HBP hipointens + kimyasal kayma → Adenom",
            "APHE + tüm fazlarda yüksek sinyal + T2 ampul bulb → Flash fill hemanjiom",
            "APHE + bilinen primer + multipl → Hipervasküler metastaz (NET, RCC)",
            "APHE + wedge şekli + damar kökenli → Arteryovenöz şant (psödolezyon)",
            "AV şant: 3 boyutlu değerlendirmede kama şekli, portal fazda kaybolur"
        ],
        "source": "LI-RADS v2018, EASL 2016, ACG 2024, Radiology Assistant"
    },
    {
        "id": "dd_hypodense_lesion_ct",
        "name": "BT'de Hipodens Lezyon Ayırıcı Tanı Zinciri",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "Portal venöz fazda hipodens lezyon: basit kist, metastaz, HKH (washout), apse, lenfoma. Her birini ayırt eden kritik bulgular farklıdır.",
        "why_matters": "Portal fazda 'hipodens kitle var' demek başlangıç. Asıl iş ayırımı yapmak. Enhancement paterni, klinik bağlam ve natif dansite birlikte değerlendirilmeli.",
        "key_points": [
            "Su dansitesi (<20 HU) + enhancement yok → Basit kist",
            "Hipodens + periferik rim + DWI kısıtlama + ateş → Apse",
            "Hipodens + periferik enhancement + bilinen primer → Metastaz",
            "Hipodens + arteryel APHE + washout + siroz → HKH",
            "Multipl hipodens + lenfadenopati + dalak tutulumu → Lenfoma",
            "Hipodens + yağ baskılı T1 hiperintens → Kanama/protein içerikli",
            "Periportal hipodens halo → Ödem/lenfatik dilatasyon (lezyon değil)"
        ],
        "source": "ACG 2024, Radiology Key, LI-RADS v2018"
    },
    {
        "id": "dd_cystic_lesion_liver",
        "name": "Kistik Karaciğer Lezyonu Karar Ağacı",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "US'de anekoik/BT'de su dansiteli lezyon gören radyolog sistematik ayırım yapmalı. Basit kist, komplike kist, hidatik, musinöz neoplazm, kistik metastaz, apse farklı yönetim.",
        "why_matters": "Basit kistte takip gereksiz. Hidatik kiste ince iğne biyopsisi anaflaksi riski. Musinöz neoplazm rezeksiyon gerektirebilir. Ayırım yönetimi belirler.",
        "key_points": [
            "Adım 1: Tamamen anekoik/su dansiteli + ince duvar + enhancement yok → Basit kist",
            "Adım 2: Duvar kalınlaşması veya septa + enhancement → Komplike kist veya neoplazm",
            "Adım 3: Kalsifik duvar + kız kesecik + iç membran → Hidatik kist",
            "Adım 4: Büyük + septasyonlu + mural nodül + kadın → Musinöz kistik neoplazm",
            "Adım 5: Solid komponent + bilinen primer → Kistik metastaz",
            "Adım 6: Rim enhancement + DWI kısıtlama + ateş → Apse",
            "MR T2 + DWI + kontrast: belirsiz US/BT bulgularını çözer"
        ],
        "source": "ACG 2024, WHO 2003, EASL, Radiology Key"
    },
    {
        "id": "dd_t2_bright_lesion",
        "name": "MR T2'de Parlak Lezyon Ayırıcı Tanı",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "T2'de parlak lezyon: hemanjiom, kist, apse, FNH santral skar, bazı HKH. Parlaklık derecesi ve ek bulgular ayırımı sağlar.",
        "why_matters": "T2'de parlak = sıvı = kist veya hemanjiom refleksi tehlikeli. Apse ve bazı malign lezyonlar da T2 parlak. Parlaklık derecesi ve DWI kritik.",
        "key_points": [
            "Belirgin parlak (BOS gibi, ampul bulb): Hemanjiom veya Basit kist",
            "Orta parlak + DWI kısıtlama → Apse veya malignite",
            "Hafif-orta parlak + APHE + washout → HKH (yardımcı özellik)",
            "Belirgin parlak + rim enhancement + klinik ateş → Apse",
            "Orta parlak + santral skar + APHE → FNH (santral skar T2 parlak)",
            "T2 shine-through tuzağı: DWI parlak ama ADC de parlak → gerçek kısıtlama değil",
            "T2 heterojen + APHE + washout + mozaik → İleri evre HKH"
        ],
        "source": "LI-RADS v2018, EASL 2016, Radiology Key MR Liver"
    },
    {
        "id": "dd_portal_hypertension_differential",
        "name": "Portal Hipertansiyon Nedenlerinin Ayırımı",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "Portal HT: prehepatik, intrahepatik, posthepatik nedenler. Görüntüleme lokalizasyonu belirler. Doğru nedenin tespiti yönetimi tamamen değiştirir.",
        "why_matters": "Siroz kaynaklı portal HT ile Budd-Chiari veya portal ven trombozu tamamen farklı yönetilir. Nedeni bulmadan 'portal HT var' demek yetersiz.",
        "key_points": [
            "Prehepatik: portal ven trombozu — kavernöz transformasyon (kronik)",
            "İntrahepatik sinüzoidal: siroz (en sık), sarkoidoz, amiloidoz",
            "İntrahepatik presinüzoidal: şistosomiasis, primer biliyer kolanjit",
            "Posthepatik: Budd-Chiari (hepatik ven), sağ kalp yetmezliği",
            "Kaudat lob hipertrofisi → Budd-Chiari",
            "Normal karaciğer + portal ven trombozu → Hiperkoagülabilite ara",
            "Doppler US: portal akım yönü, hepatik ven akımı, dalga formu"
        ],
        "source": "EASL 2018, ACG 2024, Radiology Key Portal Hypertension"
    },
    {
        "id": "dd_incidental_liver_lesion",
        "name": "İnsidental Karaciğer Lezyonu — Yönetim Algoritması",
        "organ": "liver",
        "level": 4,
        "category": "technique",
        "summary": "Başka endikasyonla çekilen BT/MR'da saptanan karaciğer lezyonunun yönetimi risk profiline göre belirlenir. Gereksiz ileri tetkik hem maliyet hem anksiyete yaratır.",
        "why_matters": "Her insidental lezyon MR veya biyopsi gerektirmez. ACR kriterleri hangi lezyonun ne kadar sürede ne ile takip edileceğini belirler. Bunu bilmemek gereksiz iş yükü yaratır.",
        "key_points": [
            "Normal KC + <1 cm hipodens → Takip gerekmez (çok büyük ihtimalle kist/hemanjiom)",
            "Normal KC + 1-1.5 cm hipodens → 6 ayda BT veya MR ile karakterizasyon",
            "Normal KC + tipik hemanjiom bulguları → Takip gerekmez",
            "Onkoloji hastası + yeni lezyon → Her boyutta değerlendir (metastaz ekarte et)",
            "Siroz + herhangi lezyon → LI-RADS algoritması",
            "Belirsiz lezyon → MR en yüksek doku karakterizasyonu sağlar",
            "ACR incidental bulgu kriterleri yaş, boyut ve karaciğer zeminine göre tablolar içerir"
        ],
        "source": "ACR Incidental Findings Committee, ACG 2024, Radiology Key"
    },
    {
        "id": "dd_liver_mass_young_woman",
        "name": "Genç Kadında Karaciğer Kitlesi — Öncelikli Tanılar",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "Genç asemptomatik kadında karaciğer kitlesi büyük olasılıkla benigndir. FNH en sık, adenom OKS ile ilişkili, hemanjiom her yaşta. Malignite nadir ama ekarte edilmeli.",
        "why_matters": "Bu demografide HKH çok nadir. Gereksiz biyopsi ve agresif tedaviden kaçınmak için doğru öncelik sırası kritik. Gadoxetat MR bu grupta tanısal.",
        "key_points": [
            "FNH: en sık, OKS ile artmaz, tedavi gerektirmez — gadoxetat MR tanısal",
            "Adenom: OKS/obezite ile ilişkili — OKS kes, 6 ayda MR takip",
            "Hemanjiom: en sık benign KC lezyonu, her yaşta",
            "Öneri sırası: Gadoxetat MR → HBP hiperintens = FNH (bitti)",
            "Gadoxetat MR → HBP hipointens + kimyasal kayma = Adenom HNF-1α",
            "Gadoxetat MR → HBP hipointens + T2 parlak (atoll) = İnflamatuar adenom",
            "β-katenin şüphesi (heterojen, atipik) → Biyopsi"
        ],
        "source": "EASL 2016, ACG 2024, Radiology Key"
    },
    {
        "id": "dd_elevated_afp_imaging",
        "name": "AFP Yüksekliği + Karaciğer Lezyonu — Tanı Algoritması",
        "organ": "liver",
        "level": 4,
        "category": "technique",
        "summary": "AFP yüksekliği ile karaciğer lezyonu birlikte değerlendirildiğinde HKH olasılığı artar. AFP düzeyi ve lezyon karakterizasyonu birlikte yönetimi belirler.",
        "why_matters": "AFP >20 ng/mL + siroz + yeni lezyon = HKH tarama pozitif. AFP çok yüksek (>200 ng/mL) ise LI-RADS'ta yardımcı özellik olarak kullanılabilir.",
        "key_points": [
            "AFP >20 ng/mL: anlamlı yükselme, siroz zemininde HKH tarama pozitif",
            "AFP >200 ng/mL: LI-RADS 2024'te yardımcı özellik olarak eklendi",
            "AFP yüksek + LR-4 → Multidisipliner tartışma, biyopsi değerlendirme",
            "AFP yüksek + LR-5 → Biyopsi gerekmez, tedavi planı",
            "AFP negatif HKH sık: %30-40 HKH AFP üretmez",
            "CA 19-9 yüksek + lezyon → ICC veya pankreatobiliyer patoloji",
            "CEA yüksek + multipl lezyon → Kolorektal metastaz"
        ],
        "source": "AASLD 2023, LI-RADS 2024, EASL 2018"
    },
]

# ── ÖNKOŞULLAR ────────────────────────────────────────────────────────────────
PREREQUISITES = [
    {"from": "lirads_lr_categories_decision", "to": "dd_hypervascular_lesion"},
    {"from": "contrast_dynamics_interactive",  "to": "dd_hypervascular_lesion"},
    {"from": "concept_fnh_vs_adenoma",        "to": "dd_hypervascular_lesion"},
    {"from": "hemangioma_variants",           "to": "dd_hypervascular_lesion"},

    {"from": "ct_physics_hu",                 "to": "dd_hypodense_lesion_ct"},
    {"from": "liver_ct_protocol",             "to": "dd_hypodense_lesion_ct"},
    {"from": "contrast_dynamics_interactive",  "to": "dd_hypodense_lesion_ct"},

    {"from": "cyst_characterization_full",    "to": "dd_cystic_lesion_liver"},
    {"from": "liver_abscess_types",           "to": "dd_cystic_lesion_liver"},
    {"from": "us_physics_liver",              "to": "dd_cystic_lesion_liver"},

    {"from": "mr_physics_t1_t2",              "to": "dd_t2_bright_lesion"},
    {"from": "concept_dwi",                  "to": "dd_t2_bright_lesion"},
    {"from": "hemangioma_variants",           "to": "dd_t2_bright_lesion"},

    {"from": "portal_hypertension",           "to": "dd_portal_hypertension_differential"},
    {"from": "liver_vascular_pathology",      "to": "dd_portal_hypertension_differential"},
    {"from": "liver_budd_chiari",             "to": "dd_portal_hypertension_differential"},

    {"from": "liver_systematic_reading",      "to": "dd_incidental_liver_lesion"},
    {"from": "liver_ct_protocol",             "to": "dd_incidental_liver_lesion"},
    {"from": "lirads_lr_categories_decision", "to": "dd_incidental_liver_lesion"},

    {"from": "concept_fnh_vs_adenoma",        "to": "dd_liver_mass_young_woman"},
    {"from": "adenoma_subtypes_full",         "to": "dd_liver_mass_young_woman"},
    {"from": "concept_hbp",                  "to": "dd_liver_mass_young_woman"},

    {"from": "concept_lirads",               "to": "dd_elevated_afp_imaging"},
    {"from": "lirads_lr_categories_decision", "to": "dd_elevated_afp_imaging"},
    {"from": "liver_lab_tests",              "to": "dd_elevated_afp_imaging"},
]

# ── CONCEPT → DIAGNOSIS ───────────────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "dd_hypervascular_lesion",    "diagnosis": "hcc",        "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_hypervascular_lesion",    "diagnosis": "fnh",        "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_hypervascular_lesion",    "diagnosis": "hca",        "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_hypervascular_lesion",    "diagnosis": "hemangioma", "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_hypodense_lesion_ct",     "diagnosis": "metastasis", "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_hypodense_lesion_ct",     "diagnosis": "hcc",        "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_cystic_lesion_liver",     "diagnosis": "simple_cyst","relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_cystic_lesion_liver",     "diagnosis": "hydatid_cyst","relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_cystic_lesion_liver",     "diagnosis": "abscess",    "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_t2_bright_lesion",        "diagnosis": "hemangioma", "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_liver_mass_young_woman",  "diagnosis": "fnh",        "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_liver_mass_young_woman",  "diagnosis": "hca",        "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_elevated_afp_imaging",    "diagnosis": "hcc",        "relation": "SUPPORTS_DIAGNOSIS"},
]

# ── SORULAR ───────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_av_shunt_vs_hcc",
        "concept_id": "dd_hypervascular_lesion",
        "type": "multiple_choice",
        "question": "Arteryel fazda kama (wedge) şeklinde, portal fazda kaybolan enhancement ne anlama gelir?",
        "options": [
            "LR-5 — kesin HKH",
            "Arteryovenöz şant — psödolezyon, HKH değil",
            "FNH — santral skar karakteristik",
            "Flash fill hemanjiom"
        ],
        "correct": 1,
        "explanation": "Kama (wedge/segmental) şeklinde arteryel enhancement portal fazda kayboluyor → arteryovenöz şant (psödolezyon). Portal venöz kan arteryel sisteme karışır, arteryel fazda lezyon gibi görünür. 3 boyutlu değerlendirmede damar anomalisi ile bağlantı görülebilir. HKH nodüler şekil alır, portal fazda washout gösterir, kama şeklinde olmaz.",
        "level": 4
    },
    {
        "id": "q_hypervascular_no_washout",
        "concept_id": "dd_hypervascular_lesion",
        "type": "multiple_choice",
        "question": "Sirozlu hastada 18 mm APHE lezyonu var, washout yok, HBP hiperintens. En olası tanı?",
        "options": [
            "HKH — LR-4",
            "FNH — HBP hiperintensite tanısal",
            "Adenom — HBP hipointens beklenir",
            "Hemanjiom — T2 ampul bulb lazım"
        ],
        "correct": 1,
        "explanation": "APHE var ama washout yok → HKH dışı düşün. HBP hiperintens → FNH. Siroz zemininde FNH nadir ama mümkün. Gadoxetat MR'da HBP hiperintensite FNH için güçlü kanıt (%95+ özgüllük). Adenom HBP'de hipointenstir. Bu bulgu kombinasyonu LI-RADS algoritmasında LR-3/4 + benign yardımcı özellik → downgrade.",
        "level": 4
    },
    {
        "id": "q_cystic_ladder",
        "concept_id": "dd_cystic_lesion_liver",
        "type": "multiple_choice",
        "question": "US'de 3 cm kistik lezyon: kalın duvar + iç septalar + mural nodül + 45 yaş kadın. Öncelikli tanı ve yapılacak tetkik?",
        "options": [
            "Basit kist — takip gerekmez",
            "Hidatik kist — seroloji",
            "Musinöz kistik neoplazm — gadoxetat MR veya kontrastlı MR",
            "Apse — antibiyotik başla"
        ],
        "correct": 2,
        "explanation": "Kalın duvar + septa + mural nodül + orta yaş kadın → musinöz kistik neoplazm (MCN) ekarte edilmeli. MCN'in %15-30'u malign dönüşüm potansiyeli taşır. Gadoxetat veya ekstrasellüler kontrastlı MR mural nodül ve solid komponent değerlendirmesi için gerekli. Basit kist bu kriterlerle uyuşmaz. Hidatik kista kız kesecik/membran beklenir.",
        "level": 4
    },
    {
        "id": "q_t2_shine_through",
        "concept_id": "dd_t2_bright_lesion",
        "type": "multiple_choice",
        "question": "DWI'da parlak görünen lezyon için ADC haritasına bakıldığında da parlak. Bu ne anlama gelir?",
        "options": [
            "Gerçek difüzyon kısıtlama — malignite şüpheli",
            "T2 shine-through artefaktı — gerçek kısıtlama değil",
            "Hemanjiom kriterleri",
            "Kist kriterleri"
        ],
        "correct": 1,
        "explanation": "T2 shine-through: T2'de çok parlak olan yapılar (kist, hemanjiom) DWI'da da parlak görünür çünkü DWI T2 ağırlıklıdır. Gerçek difüzyon kısıtlaması: DWI parlak + ADC KOYU. ADC haritasında parlak kalıyorsa bu T2 etkisinin yansımasıdır — gerçek kısıtlama değil. Bu tuzak kist ve hemanjiomun yanlışlıkla malign kategorize edilmesine yol açar.",
        "level": 4
    },
    {
        "id": "q_young_woman_hbp",
        "concept_id": "dd_liver_mass_young_woman",
        "type": "multiple_choice",
        "question": "23 yaş kadın, OKS kullanıyor, 4 cm karaciğer lezyonu. Gadoxetat MR'da APHE var, HBP hipointens, T1 kimyasal kaymada sinyal düşümü. En olası tanı ve yönetim?",
        "options": [
            "FNH — takip gerekmez",
            "HKH — MDT",
            "Adenom HNF-1α subtipi — OKS kes, 6 ay MR takip",
            "Hemanjiom — takip gerekmez"
        ],
        "correct": 2,
        "explanation": "Genç kadın + OKS + APHE + HBP hipointens + kimyasal kayma sinyal düşümü (yağ içeriği) → Adenom HNF-1α subtipi. HBP hipointens FNH'yı ekarte eder. Kimyasal kayma yağlı HNF-1α subtipini gösterir. Yönetim: OKS kesi + 6 ayda MR takip. Boyut ≥5 cm → cerrahi değerlendirme. HKH bu yaşta siroz olmadan çok nadir.",
        "level": 4
    },
    {
        "id": "q_incidental_lesion",
        "concept_id": "dd_incidental_liver_lesion",
        "type": "multiple_choice",
        "question": "50 yaş erkek, kolon polip taraması BT'de karaciğerde 8 mm hipodens lezyon, belirgin enhancement yok. Bilinen karaciğer hastalığı yok. Yönetim?",
        "options": [
            "Acil biyopsi",
            "1 haftada MR ile karakterizasyon",
            "Takip gerekmez — <1 cm, normal KC zemini, büyük ihtimalle kist/hemanjiom",
            "Multifazik BT"
        ],
        "correct": 2,
        "explanation": "ACR insidental bulgu kriterleri: normal karaciğer zemininde <1 cm hipodens lezyon → takip gerekmez. Bu boyutta ve bu zeminde lezyon büyük ihtimalle kist veya hemanjiom. Malignite riski çok düşük. Gereksiz ileri tetkik hasta anksiyetesini ve maliyeti artırır. Eğer bilinen malignite olsaydı her boyutta değerlendirmek gerekecekti.",
        "level": 4
    },
    {
        "id": "q_portal_ht_cause",
        "concept_id": "dd_portal_hypertension_differential",
        "type": "multiple_choice",
        "question": "Portal hipertansiyon bulguları olan hastada karaciğer normal görünüyor, hepatik venler patent, kaudat lob normal. Doppler'da portal vende akım yok. Tanı?",
        "options": [
            "Siroz — karaciğer erken evrede normal görünebilir",
            "Budd-Chiari — hepatik ven oklüzyonu",
            "Prehepatik portal hipertansiyon — portal ven trombozu",
            "Sağ kalp yetmezliği — posthepatik"
        ],
        "correct": 2,
        "explanation": "Normal karaciğer + hepatik venler patent + portal vende akım yok → Prehepatik portal HT (portal ven trombozu). Siroz intrahepatik, Budd-Chiari posthepatik (hepatik ven), sağ kalp yetmezliği posthepatik ama karaciğer konjesyon bulguları olur. Portal ven trombozu: kronik ise kavernöz transformasyon gelişir (portal ven yerine kollateral venöz yapılar). Nedeni ara: hiperkoagülabilite, siroz, HKH invazyonu.",
        "level": 4
    },
]


# ── SEED ──────────────────────────────────────────────────────────────────────

def seed_concepts(tx):
    for c in CONCEPTS:
        tx.run("""
            MERGE (c:Concept {id:$id})
            SET c.name=$name, c.organ=$organ, c.level=$level,
                c.category=$category, c.summary=$summary,
                c.why_matters=$why_matters, c.key_points=$key_points,
                c.source=$source
        """, **{k: v for k, v in c.items()})
    return len(CONCEPTS)

def seed_prerequisites(tx):
    for p in PREREQUISITES:
        tx.run("""
            MATCH (c1:Concept {id:$from_id})
            MATCH (c2:Concept {id:$to_id})
            MERGE (c1)-[:PREREQUISITE_OF]->(c2)
        """, from_id=p["from"], to_id=p["to"])
    return len(PREREQUISITES)

def seed_concept_diagnosis(tx):
    for cd in CONCEPT_DIAGNOSIS:
        tx.run("""
            MATCH (c:Concept {id:$concept_id})
            MATCH (d:Diagnosis {id:$diagnosis_id})
            MERGE (c)-[:RELATES_TO {relation:$relation}]->(d)
        """, concept_id=cd["concept"], diagnosis_id=cd["diagnosis"], relation=cd["relation"])
    return len(CONCEPT_DIAGNOSIS)

def seed_questions(tx):
    for q in QUESTIONS:
        tx.run("""
            MERGE (q:Question {id:$id})
            SET q.concept_id=$concept_id, q.type=$type,
                q.question=$question, q.options=$options,
                q.correct=$correct, q.explanation=$explanation,
                q.level=$level
        """, **q)
        tx.run("""
            MATCH (q:Question {id:$q_id})
            MATCH (c:Concept {id:$c_id})
            MERGE (q)-[:TESTS]->(c)
        """, q_id=q["id"], c_id=q["concept_id"])
    return len(QUESTIONS)

print("\n── Katman 4 yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_concepts)
    print(f"✓ {n} Concept")
with driver.session() as session:
    n = session.execute_write(seed_prerequisites)
    print(f"✓ {n} PREREQUISITE_OF")
with driver.session() as session:
    n = session.execute_write(seed_concept_diagnosis)
    print(f"✓ {n} RELATES_TO")
with driver.session() as session:
    n = session.execute_write(seed_questions)
    print(f"✓ {n} Question")

driver.close()
print(f"\n✓ Katman 4 tamamlandı — {len(CONCEPTS)} concept, {len(QUESTIONS)} soru")

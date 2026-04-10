from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

# ── 18 YENİ TANI ─────────────────────────────────────────────────────────────

DIAGNOSES = [
    {
        "id": "klatskin_tumor",
        "name": "Hilar Kolanjiyokarsinom (Klatskin Tümörü)",
        "name_en": "Perihilar Cholangiocarcinoma",
        "organ": "liver",
        "icd10": "C24.0",
        "risk_level": "yuksek",
        "lirads": None,
        "source": "EASL 2022, AJR Hilar CCA 2008, PMC 3731524",
        "report_template": "Hepatik hilus düzeyinde, safra yolu bifürkasyonunu tutan, periduktüel infiltratif kitle izlenmektedir. İntahepatik safra yollarında bilateral dilatasyon mevcuttur. Bismuth-Corlette sınıflamasına göre [tip] ile uyumludur. MRCP ile rezektabilite değerlendirmesi ve MDT önerilir.",
        "differentials": ["icc", "psc", "benign_stricture"]
    },
    {
        "id": "psc",
        "name": "Primer Sklerozan Kolanjit (PSK)",
        "name_en": "Primary Sclerosing Cholangitis",
        "organ": "liver",
        "icd10": "K83.0",
        "risk_level": "orta",
        "lirads": None,
        "source": "EASL PSC Guidelines 2022, ACG 2024",
        "report_template": "İntra ve ekstrahepatik safra yollarında yaygın, boncuk dizisi görünümünde striktür ve dilatasyon alanları izlenmektedir. Bulgular primer sklerozan kolanjit ile uyumludur. Kolanjiyokarsinom gelişimi açısından klinik takip önerilir.",
        "differentials": ["klatskin_tumor", "igg4_cholangitis", "icc"]
    },
    {
        "id": "igg4_cholangitis",
        "name": "IgG4 İlişkili Kolanjit",
        "name_en": "IgG4-Related Cholangiopathy",
        "organ": "liver",
        "icd10": "K83.0",
        "risk_level": "orta",
        "lirads": None,
        "source": "EASL 2022, Radiology Key IgG4",
        "report_template": "Safra yolu duvarında diffüz kalınlaşma ve enhancement izlenmektedir. IgG4 ilişkili kolanjit ile uyumlu bulgular mevcuttur. Serum IgG4 düzeyi ve steroid yanıtı için klinik değerlendirme önerilir.",
        "differentials": ["psc", "klatskin_tumor", "icc"]
    },
    {
        "id": "choledochal_cyst",
        "name": "Koledok Kisti",
        "name_en": "Choledochal Cyst",
        "organ": "liver",
        "icd10": "Q44.4",
        "risk_level": "orta",
        "lirads": None,
        "source": "EASL 2022, ACG 2024, Todani Sınıflaması",
        "report_template": "Ekstrahepatik safra yolunda kistik dilatasyon izlenmektedir. Todani sınıflamasına göre [tip] ile uyumludur. Kolanjiyokarsinom gelişim riski nedeniyle cerrahi konsültasyon önerilir.",
        "differentials": ["simple_cyst", "caroli_disease", "icc"]
    },
    {
        "id": "mucin_cystic_neoplasm",
        "name": "Musinöz Kistik Neoplazm (MCN)",
        "name_en": "Mucinous Cystic Neoplasm",
        "organ": "liver",
        "icd10": "D13.4",
        "risk_level": "orta",
        "lirads": None,
        "source": "ACG 2024, WHO Classification 2019",
        "report_template": "Karaciğer [segment]'de kalın duvarlı, septasyonlu, mural nodül içeren büyük kistik lezyon izlenmektedir. Musinöz kistik neoplazm ile uyumlu bulgular mevcuttur. Cerrahi rezeksiyon değerlendirmesi için MDT önerilir.",
        "differentials": ["simple_cyst", "hydatid_cyst", "abscess"]
    },
    {
        "id": "hepatoblastoma",
        "name": "Hepatoblastom",
        "name_en": "Hepatoblastoma",
        "organ": "liver",
        "icd10": "C22.2",
        "risk_level": "yuksek",
        "lirads": None,
        "source": "Radiology Key, Pediatric Radiology",
        "report_template": "Karaciğerde heterojen, kalsifikasyon içerebilen büyük kitle izlenmektedir. Pediyatrik yaş grubu ve AFP yüksekliği göz önünde bulundurulduğunda hepatoblastom ile uyumludur. Pediyatrik onkoloji MDT önerilir.",
        "differentials": ["hcc", "metastasis"]
    },
    {
        "id": "hemangioendothelioma",
        "name": "Epiteloid Hemanjiyoendotelyoma (EHE)",
        "name_en": "Epithelioid Hemangioendothelioma",
        "organ": "liver",
        "icd10": "C22.3",
        "risk_level": "yuksek",
        "lirads": None,
        "source": "Radiology Key EHE, RadioGraphics",
        "report_template": "Karaciğerde multipl, periferal yerleşimli, kapsüler retraksiyon gösteren nodüller izlenmektedir. Epiteloid hemanjiyoendotelyoma ile uyumlu bulgular mevcuttur. MDT ve biyopsi önerilir.",
        "differentials": ["metastasis", "icc", "angiosarcoma"]
    },
    {
        "id": "angiosarcoma",
        "name": "Karaciğer Anjiyosarkomu",
        "name_en": "Hepatic Angiosarcoma",
        "organ": "liver",
        "icd10": "C22.3",
        "risk_level": "yuksek",
        "lirads": None,
        "source": "Radiology Key, WHO 2019",
        "report_template": "Karaciğerde multipl, heterojen, kanama içerebilen hipervasküler kitleler izlenmektedir. Karaciğer anjiyosarkomu ile uyumlu bulgular mevcuttur. Biyopsi ve MDT önerilir.",
        "differentials": ["hemangioma", "hemangioendothelioma", "metastasis"]
    },
    {
        "id": "liver_lymphoma",
        "name": "Primer Karaciğer Lenfoması",
        "name_en": "Primary Hepatic Lymphoma",
        "organ": "liver",
        "icd10": "C83.3",
        "risk_level": "yuksek",
        "lirads": None,
        "source": "Radiology Key, ACG 2024",
        "report_template": "Karaciğerde hipodens, minimal enhancement gösteren kitle/kitleler izlenmektedir. Primer karaciğer lenfoması ile uyumlu bulgular mevcuttur. Biyopsi ve hematoloji konsültasyonu önerilir.",
        "differentials": ["metastasis", "abscess", "icc"]
    },
    {
        "id": "combined_hcc_icc",
        "name": "Kombine HKH-İCC",
        "name_en": "Combined Hepatocellular-Cholangiocarcinoma",
        "organ": "liver",
        "icd10": "C22.0",
        "risk_level": "yuksek",
        "lirads": "LR-M",
        "source": "LI-RADS v2018, EASL 2022",
        "report_template": "Karma görüntüleme özellikleri (hem HKH hem ICC paterni) gösteren lezyon izlenmektedir. Kombine hepatoselüler-kolanjiyoselüler karsinom ekarte edilemez. Biyopsi ve MDT önerilir.",
        "differentials": ["hcc", "icc"]
    },
    {
        "id": "cavernous_transformation",
        "name": "Portal Ven Kavernöz Transformasyonu",
        "name_en": "Cavernous Transformation of Portal Vein",
        "organ": "liver",
        "icd10": "K76.6",
        "risk_level": "orta",
        "lirads": None,
        "source": "EASL 2018, Radiology Key Portal Vein",
        "report_template": "Portal ven lümeninde trombüs ve çevresinde gelişmiş kollateral venöz yapılar (kavernöz transformasyon) izlenmektedir. Portal hipertansiyon bulguları eşlik etmektedir. Hiperkoagülabilite araştırması önerilir.",
        "differentials": ["portal_hypertension", "hcc"]
    },
    {
        "id": "congestive_hepatopathy",
        "name": "Konjesif Hepatopati",
        "name_en": "Congestive Hepatopathy",
        "organ": "liver",
        "icd10": "K76.1",
        "risk_level": "orta",
        "lirads": None,
        "source": "EASL 2018, Radiology Key",
        "report_template": "Karaciğerde periferik sinüzoidal dilatasyon, mozaik enhancement paterni ve hepatik ven/IVC dilatasyonu izlenmektedir. Konjesif hepatopati ile uyumlu bulgular mevcuttur. Kardiyoloji konsültasyonu önerilir.",
        "differentials": ["budd_chiari", "liver_cirrhosis"]
    },
    {
        "id": "pbc",
        "name": "Primer Biliyer Kolanjit (PBK)",
        "name_en": "Primary Biliary Cholangitis",
        "organ": "liver",
        "icd10": "K74.3",
        "risk_level": "orta",
        "lirads": None,
        "source": "EASL PBC Guidelines 2017, ACG 2024",
        "report_template": "Karaciğerde periportal ödem ve heterojen parankim izlenmektedir. Klinik ve laboratuvar bulgularla (AMA pozitifliği, ALP yüksekliği) primer biliyer kolanjit değerlendirmesi önerilir.",
        "differentials": ["psc", "nash"]
    },
    {
        "id": "nash",
        "name": "Non-alkolik Steatohepatit (NASH)",
        "name_en": "Non-alcoholic Steatohepatitis",
        "organ": "liver",
        "icd10": "K75.81",
        "risk_level": "orta",
        "lirads": None,
        "source": "EASL NAFLD/NASH Guidelines 2016, ACG 2024",
        "report_template": "Karaciğerde diffüz yağlı infiltrasyon ve siroz bulguları izlenmektedir. Non-alkolik steatohepatit zeminine bağlı siroz ile uyumlu bulgular mevcuttur. HKH surveyansı başlanması önerilir.",
        "differentials": ["liver_cirrhosis", "alcoholic_hepatitis"]
    },
    {
        "id": "focal_bile_duct_stricture",
        "name": "Benign Safra Yolu Striktürü",
        "name_en": "Benign Biliary Stricture",
        "organ": "liver",
        "icd10": "K83.1",
        "risk_level": "orta",
        "lirads": None,
        "source": "ACG 2024, EASL 2022",
        "report_template": "Safra yolunda fokal darlık izlenmektedir. Post-operatif/iyatrojenik veya inflamatuar etiyoloji ile uyumludur. Kolanjiyokarsinom ekartasyonu için MRCP ve klinik korelasyon önerilir.",
        "differentials": ["klatskin_tumor", "psc", "igg4_cholangitis"]
    },
    {
        "id": "liver_sarcoidosis",
        "name": "Karaciğer Sarkoidozu",
        "name_en": "Hepatic Sarcoidosis",
        "organ": "liver",
        "icd10": "D86.8",
        "risk_level": "orta",
        "lirads": None,
        "source": "Radiology Key Sarcoidosis, ACG 2024",
        "report_template": "Karaciğerde multipl, küçük hipoekoik/hipodens nodüller izlenmektedir. Mediastinal ve hiler lenfadenopati eşliğinde karaciğer sarkoidozu ile uyumludur. Biyopsi ve solunum/romatoloji konsültasyonu önerilir.",
        "differentials": ["metastasis", "liver_lymphoma", "abscess"]
    },
    {
        "id": "biliary_cystadenoma",
        "name": "Biliyer Kistadenoma / Kistadenokarsinoma",
        "name_en": "Biliary Cystadenoma / Cystadenocarcinoma",
        "organ": "liver",
        "icd10": "D13.4",
        "risk_level": "orta",
        "lirads": None,
        "source": "ACG 2024, WHO 2019",
        "report_template": "Karaciğerde çok lokülüslü, septasyonlu, mural nodül içeren kistik lezyon izlenmektedir. Biliyer kistadenoma/kistadenokarsinoma ile uyumludur. Cerrahi rezeksiyon değerlendirmesi önerilir.",
        "differentials": ["mucin_cystic_neoplasm", "simple_cyst", "hydatid_cyst"]
    },
    {
        "id": "peliosis_hepatis",
        "name": "Peliozis Hepatis",
        "name_en": "Peliosis Hepatis",
        "organ": "liver",
        "icd10": "K76.4",
        "risk_level": "orta",
        "lirads": None,
        "source": "Radiology Key Peliosis, ACG 2024",
        "report_template": "Karaciğerde multipl, değişken boyutlarda, kistik veya solid görünümde lezyonlar izlenmektedir. İlaç/hormon öyküsü ile birlikte peliozis hepatis ile uyumludur. İlaç kesimi ve klinik takip önerilir.",
        "differentials": ["hemangioma", "metastasis", "simple_cyst"]
    },
]

# ── YENİ TANILARA BULGULAR (SUGGESTS ilişkileri) ──────────────────────────────
SUGGESTS = [
    # Klatskin tümörü
    {"finding": "liver_ct_irregular",        "diagnosis": "klatskin_tumor", "weight": 0.6,  "required": False, "source": "EASL 2022"},
    {"finding": "liver_ct_persist_enhance",  "diagnosis": "klatskin_tumor", "weight": 0.75, "required": True,  "source": "EASL 2022"},
    {"finding": "liver_mr_dwi_restrict",     "diagnosis": "klatskin_tumor", "weight": 0.7,  "required": False, "source": "EASL 2022"},
    {"finding": "liver_mr_persist_enhance",  "diagnosis": "klatskin_tumor", "weight": 0.75, "required": True,  "source": "EASL 2022"},

    # PSK
    {"finding": "liver_ct_irregular",        "diagnosis": "psc",           "weight": 0.4,  "required": False, "source": "EASL PSC 2022"},
    {"finding": "liver_mr_t2_mild_hyper",    "diagnosis": "psc",           "weight": 0.4,  "required": False, "source": "EASL PSC 2022"},

    # Hepatoblastom
    {"finding": "liver_ct_calcification",   "diagnosis": "hepatoblastoma", "weight": 0.6,  "required": False, "source": "Pediatric Radiology"},
    {"finding": "liver_ct_aphe",             "diagnosis": "hepatoblastoma", "weight": 0.5,  "required": False, "source": "Pediatric Radiology"},
    {"finding": "liver_mr_t2_mild_hyper",    "diagnosis": "hepatoblastoma", "weight": 0.5,  "required": False, "source": "Pediatric Radiology"},

    # EHE
    {"finding": "liver_ct_capsular_retract", "diagnosis": "hemangioendothelioma", "weight": 0.7, "required": False, "source": "RadioGraphics EHE"},
    {"finding": "liver_ct_peripheral_nod",   "diagnosis": "hemangioendothelioma", "weight": 0.5, "required": False, "source": "RadioGraphics EHE"},
    {"finding": "liver_mr_dwi_restrict",     "diagnosis": "hemangioendothelioma", "weight": 0.5, "required": False, "source": "RadioGraphics EHE"},

    # MCN
    {"finding": "liver_ct_avascular",        "diagnosis": "mucin_cystic_neoplasm", "weight": 0.4, "required": False, "source": "ACG 2024"},
    {"finding": "liver_ct_smooth_border",    "diagnosis": "mucin_cystic_neoplasm", "weight": 0.3, "required": False, "source": "ACG 2024"},

    # Biliyer kistadenoma
    {"finding": "liver_mr_t2_bright",        "diagnosis": "biliary_cystadenoma", "weight": 0.5, "required": False, "source": "ACG 2024"},
    {"finding": "liver_ct_smooth_border",    "diagnosis": "biliary_cystadenoma", "weight": 0.4, "required": False, "source": "ACG 2024"},

    # Konjesif hepatopati
    {"finding": "liver_ct_persist_enhance",  "diagnosis": "congestive_hepatopathy", "weight": 0.5, "required": False, "source": "Radiology Key"},
    {"finding": "liver_mr_t2_mild_hyper",    "diagnosis": "congestive_hepatopathy", "weight": 0.4, "required": False, "source": "Radiology Key"},

    # Lenfoma
    {"finding": "liver_ct_hypodense",        "diagnosis": "liver_lymphoma", "weight": 0.5, "required": False, "source": "Radiology Key"},
    {"finding": "liver_ct_avascular",        "diagnosis": "liver_lymphoma", "weight": 0.4, "required": False, "source": "Radiology Key"},
    {"finding": "liver_mr_dwi_restrict",     "diagnosis": "liver_lymphoma", "weight": 0.6, "required": False, "source": "Radiology Key"},

    # Sarkoidoz
    {"finding": "liver_ct_hypodense",        "diagnosis": "liver_sarcoidosis", "weight": 0.4, "required": False, "source": "Radiology Key"},
    {"finding": "liver_mr_t2_iso",           "diagnosis": "liver_sarcoidosis", "weight": 0.4, "required": False, "source": "Radiology Key"},

    # Kombine HKH-ICC
    {"finding": "liver_ct_aphe",             "diagnosis": "combined_hcc_icc", "weight": 0.5, "required": False, "source": "LI-RADS v2018"},
    {"finding": "liver_ct_persist_enhance",  "diagnosis": "combined_hcc_icc", "weight": 0.5, "required": False, "source": "LI-RADS v2018"},

    # Peliozis
    {"finding": "liver_us_heterogeneous",    "diagnosis": "peliosis_hepatis", "weight": 0.4, "required": False, "source": "Radiology Key"},
    {"finding": "liver_ct_aphe",             "diagnosis": "peliosis_hepatis", "weight": 0.4, "required": False, "source": "Radiology Key"},

    # NASH
    {"finding": "liver_us_heterogeneous",    "diagnosis": "nash",  "weight": 0.4, "required": False, "source": "EASL 2016"},
    {"finding": "liver_ct_hypodense",        "diagnosis": "nash",  "weight": 0.5, "required": False, "source": "EASL 2016"},
    {"finding": "liver_mr_t1_chemshift",     "diagnosis": "nash",  "weight": 0.6, "required": False, "source": "EASL 2016"},
]

# ── YENİ TANILARA AKSİYONLAR ─────────────────────────────────────────────────
DIAGNOSIS_ACTIONS = [
    {"diagnosis": "klatskin_tumor",      "action": "mdt",           "urgency": "kritik", "order": 1},
    {"diagnosis": "klatskin_tumor",      "action": "mrcp",          "urgency": "yuksek", "order": 2},
    {"diagnosis": "klatskin_tumor",      "action": "biopsy",        "urgency": "yuksek", "order": 3},
    {"diagnosis": "klatskin_tumor",      "action": "ca199_cea",     "urgency": "orta",   "order": 4},

    {"diagnosis": "psc",                 "action": "mrcp",          "urgency": "yuksek", "order": 1},
    {"diagnosis": "psc",                 "action": "ca199_cea",     "urgency": "orta",   "order": 2},
    {"diagnosis": "psc",                 "action": "followup_6m_us","urgency": "orta",   "order": 3},

    {"diagnosis": "igg4_cholangitis",    "action": "biopsy",        "urgency": "yuksek", "order": 1},
    {"diagnosis": "igg4_cholangitis",    "action": "mrcp",          "urgency": "yuksek", "order": 2},

    {"diagnosis": "choledochal_cyst",    "action": "mrcp",          "urgency": "yuksek", "order": 1},
    {"diagnosis": "choledochal_cyst",    "action": "surgical_consult","urgency":"yuksek", "order": 2},

    {"diagnosis": "mucin_cystic_neoplasm","action": "multiphase_mr","urgency": "yuksek", "order": 1},
    {"diagnosis": "mucin_cystic_neoplasm","action": "surgical_consult","urgency":"yuksek","order": 2},

    {"diagnosis": "hepatoblastoma",      "action": "mdt",           "urgency": "kritik", "order": 1},
    {"diagnosis": "hepatoblastoma",      "action": "staging_ct",    "urgency": "kritik", "order": 2},

    {"diagnosis": "hemangioendothelioma","action": "biopsy",        "urgency": "kritik", "order": 1},
    {"diagnosis": "hemangioendothelioma","action": "mdt",           "urgency": "kritik", "order": 2},

    {"diagnosis": "angiosarcoma",        "action": "biopsy",        "urgency": "kritik", "order": 1},
    {"diagnosis": "angiosarcoma",        "action": "mdt",           "urgency": "kritik", "order": 2},

    {"diagnosis": "liver_lymphoma",      "action": "biopsy",        "urgency": "kritik", "order": 1},
    {"diagnosis": "liver_lymphoma",      "action": "mdt",           "urgency": "kritik", "order": 2},

    {"diagnosis": "combined_hcc_icc",    "action": "biopsy",        "urgency": "kritik", "order": 1},
    {"diagnosis": "combined_hcc_icc",    "action": "mdt",           "urgency": "kritik", "order": 2},

    {"diagnosis": "cavernous_transformation","action":"multiphase_ct","urgency":"orta",  "order": 1},
    {"diagnosis": "congestive_hepatopathy",  "action":"multiphase_mr","urgency":"orta",  "order": 1},

    {"diagnosis": "pbc",                 "action": "followup_6m_us","urgency": "orta",   "order": 1},
    {"diagnosis": "nash",                "action": "followup_6m_us","urgency": "orta",   "order": 1},

    {"diagnosis": "focal_bile_duct_stricture","action":"mrcp",      "urgency": "yuksek", "order": 1},
    {"diagnosis": "focal_bile_duct_stricture","action":"biopsy",    "urgency": "yuksek", "order": 2},

    {"diagnosis": "liver_sarcoidosis",   "action": "biopsy",        "urgency": "yuksek", "order": 1},
    {"diagnosis": "biliary_cystadenoma", "action": "surgical_consult","urgency":"yuksek","order": 1},
    {"diagnosis": "peliosis_hepatis",    "action": "ocs_cessation",  "urgency": "yuksek","order": 1},
    {"diagnosis": "peliosis_hepatis",    "action": "followup_6m_us", "urgency": "orta",  "order": 2},
]

# ── DIFFERENTIATES_FROM ───────────────────────────────────────────────────────
DIFFERENTIATIONS = [
    {"from": "klatskin_tumor", "to": "psc",         "key_finding": "Klatskin: fokal kitle + asimetrik dilatasyon. PSK: diffüz boncuk görünümü, bilateral simetrik", "modality": "mrcp"},
    {"from": "klatskin_tumor", "to": "igg4_cholangitis","key_finding": "Klatskin: kitle + CA19-9 yüksek. IgG4: IgG4 serum yüksek, steroid yanıtı var", "modality": "ct_mr"},
    {"from": "mucin_cystic_neoplasm", "to": "biliary_cystadenoma","key_finding": "Pratikte örtüşür — her ikisi de rezeksiyon gerektirir", "modality": "mr"},
    {"from": "hemangioendothelioma",  "to": "metastasis","key_finding": "EHE: kapsüler retraksiyon + periferal yerleşim. Metastaz: bilinen primer", "modality": "ct_mr"},
    {"from": "liver_lymphoma",        "to": "metastasis","key_finding": "Lenfoma: minimal enhancement, DWI kısıtlama, lenfadenopati. Metastaz: bilinen primer", "modality": "ct_mr"},
    {"from": "pbc",                   "to": "psc",     "key_finding": "PBK: AMA pozitif, intrahepatik safra yolları. PSK: intra+ekstrahepatik, IBD ilişkili", "modality": "mrcp"},
    {"from": "congestive_hepatopathy","to": "liver_budd_chiari","key_finding": "Konjesif hepatopati: hepatik venler açık, IVC dilate. Budd-Chiari: hepatik ven oklüzyonu", "modality": "ct_mr"},
]


# ── SEED FONKSİYONLARI ────────────────────────────────────────────────────────

def seed_diagnoses(tx):
    for d in DIAGNOSES:
        tx.run("""
            MERGE (d:Diagnosis {id: $id})
            SET d.name=$name, d.name_en=$name_en, d.organ=$organ,
                d.icd10=$icd10, d.risk_level=$risk_level,
                d.lirads=$lirads, d.source=$source,
                d.report_template=$report_template
        """, **{k: v for k, v in d.items() if k != "differentials"})
    return len(DIAGNOSES)

def seed_suggests(tx):
    for s in SUGGESTS:
        tx.run("""
            MATCH (f:Finding {id: $finding})
            MATCH (d:Diagnosis {id: $diagnosis})
            MERGE (f)-[r:SUGGESTS]->(d)
            SET r.weight=$weight, r.required=$required, r.source=$source
        """, **s)
    return len(SUGGESTS)

def seed_actions(tx):
    for da in DIAGNOSIS_ACTIONS:
        tx.run("""
            MATCH (d:Diagnosis {id: $diagnosis})
            MATCH (a:Action {id: $action})
            MERGE (d)-[r:REQUIRES_ACTION]->(a)
            SET r.urgency=$urgency, r.order=$order
        """, **da)
    return len(DIAGNOSIS_ACTIONS)

def seed_differentiations(tx):
    for diff in DIFFERENTIATIONS:
        tx.run("""
            MATCH (d1:Diagnosis {id: $from})
            MATCH (d2:Diagnosis {id: $to})
            MERGE (d1)-[r:DIFFERENTIATES_FROM]->(d2)
            SET r.key_finding=$key_finding, r.modality=$modality
        """, **diff)
    return len(DIFFERENTIATIONS)


print("\n── Yeni tanılar yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_diagnoses)
    print(f"✓ {n} Diagnosis düğümü")

with driver.session() as session:
    n = session.execute_write(seed_suggests)
    print(f"✓ {n} SUGGESTS ilişkisi")

with driver.session() as session:
    n = session.execute_write(seed_actions)
    print(f"✓ {n} REQUIRES_ACTION ilişkisi")

with driver.session() as session:
    n = session.execute_write(seed_differentiations)
    print(f"✓ {n} DIFFERENTIATES_FROM ilişkisi")

driver.close()
print(f"\n✓ Genişletilmiş tanı listesi tamamlandı — {len(DIAGNOSES)} yeni tanı")

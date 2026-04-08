from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


# ── FINDINGS ──────────────────────────────────────────────────────────────────

FINDINGS = [
    # US Bulgular
    {"id": "liver_us_anechoic",         "name": "Anekoik (tamamen siyah)",              "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 1},
    {"id": "liver_us_hyperechoic",      "name": "Hipereko (beyaz, parlak)",             "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 2},
    {"id": "liver_us_hypoechoic",       "name": "Hipoekoik (koyu)",                     "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 3},
    {"id": "liver_us_isoechoic",        "name": "İzoekoik",                             "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 4},
    {"id": "liver_us_heterogeneous",    "name": "Heterojen / karma",                    "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 5},
    {"id": "liver_us_post_acoustic",    "name": "Posterior akustik güçlenme",           "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 6},
    {"id": "liver_us_smooth_border",    "name": "Düzgün sınır",                         "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 7},
    {"id": "liver_us_irregular_border", "name": "Düzensiz sınır",                       "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 8},
    {"id": "liver_us_halo",             "name": "Halo işareti",                         "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 9},
    {"id": "liver_us_central_scar",     "name": "Santral skar",                         "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 10},
    {"id": "liver_us_calcification",    "name": "Kalsifikasyon",                        "organ": "liver", "modality": "us", "sequence": "bmode",    "display_order": 11},
    {"id": "liver_us_ceus_aphe",        "name": "CEUS: Arteryel hiperenhancement",      "organ": "liver", "modality": "us", "sequence": "ceus",     "display_order": 12},
    {"id": "liver_us_ceus_washout",     "name": "CEUS: Portal washout",                 "organ": "liver", "modality": "us", "sequence": "ceus",     "display_order": 13},
    {"id": "liver_us_ceus_persist",     "name": "CEUS: Persistan enhancement",          "organ": "liver", "modality": "us", "sequence": "ceus",     "display_order": 14},
    {"id": "liver_us_ceus_rim",         "name": "CEUS: Rim tarzı enhancement",          "organ": "liver", "modality": "us", "sequence": "ceus",     "display_order": 15},
    {"id": "liver_us_doppler_central",  "name": "Doppler: Santral arteryel akım",       "organ": "liver", "modality": "us", "sequence": "doppler",  "display_order": 16},
    {"id": "liver_us_doppler_periferal","name": "Doppler: Periferal nodüler akım",      "organ": "liver", "modality": "us", "sequence": "doppler",  "display_order": 17},
    {"id": "liver_us_avascular",        "name": "Doppler: Avasküler",                   "organ": "liver", "modality": "us", "sequence": "doppler",  "display_order": 18},

    # BT Bulgular
    {"id": "liver_ct_hypodense",        "name": "Natif: Hipodens",                      "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 1},
    {"id": "liver_ct_hyperdense",       "name": "Natif: Hiperdens (spontan)",           "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 2},
    {"id": "liver_ct_calcification",    "name": "Natif: Kalsifikasyon",                 "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 3},
    {"id": "liver_ct_water_density",    "name": "Natif: Su dansitesi",                  "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 4},
    {"id": "liver_ct_aphe",             "name": "Arteryel: Hiperenhancement (non-rim)", "organ": "liver", "modality": "ct", "sequence": "arterial", "display_order": 5},
    {"id": "liver_ct_rim_aphe",         "name": "Arteryel: Rim tarzı enhancement",      "organ": "liver", "modality": "ct", "sequence": "arterial", "display_order": 6},
    {"id": "liver_ct_peripheral_nod",   "name": "Arteryel: Periferik nodüler",          "organ": "liver", "modality": "ct", "sequence": "arterial", "display_order": 7},
    {"id": "liver_ct_washout",          "name": "Portal/Geç: Washout",                  "organ": "liver", "modality": "ct", "sequence": "portal",   "display_order": 8},
    {"id": "liver_ct_fill_in",          "name": "Portal/Geç: Santral dolum (fill-in)",  "organ": "liver", "modality": "ct", "sequence": "delayed",  "display_order": 9},
    {"id": "liver_ct_persist_enhance",  "name": "Geç: Persistan enhancement",           "organ": "liver", "modality": "ct", "sequence": "delayed",  "display_order": 10},
    {"id": "liver_ct_capsule",          "name": "Enhancing kapsül",                     "organ": "liver", "modality": "ct", "sequence": "portal",   "display_order": 11},
    {"id": "liver_ct_avascular",        "name": "Enhancement yok (avasküler)",           "organ": "liver", "modality": "ct", "sequence": "arterial", "display_order": 12},
    {"id": "liver_ct_smooth_border",    "name": "Düzgün sınır",                         "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 13},
    {"id": "liver_ct_irregular",        "name": "Düzensiz sınır / lobüle",              "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 14},
    {"id": "liver_ct_satellite",        "name": "Satellit lezyon",                      "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 15},
    {"id": "liver_ct_capsular_retract", "name": "Kapsüler retraksiyon",                 "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 16},
    {"id": "liver_ct_central_scar",     "name": "Santral skar / nekroz",                "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 17},
    {"id": "liver_ct_threshold_growth", "name": "Eşik büyüme (6 ayda ≥%50)",           "organ": "liver", "modality": "ct", "sequence": "native",   "display_order": 18},
    {"id": "liver_ct_vascular_inv",     "name": "Vasküler invazyon",                    "organ": "liver", "modality": "ct", "sequence": "portal",   "display_order": 19},

    # MR Bulgular
    {"id": "liver_mr_t1_hypo",          "name": "T1: Hipointens",                       "organ": "liver", "modality": "mr", "sequence": "t1",       "display_order": 1},
    {"id": "liver_mr_t1_hyper",         "name": "T1: Hiperintens (kanama/yağ)",         "organ": "liver", "modality": "mr", "sequence": "t1",       "display_order": 2},
    {"id": "liver_mr_t1_chemshift",     "name": "T1: Kimyasal kayma sinyal düşümü",     "organ": "liver", "modality": "mr", "sequence": "t1_ip_op", "display_order": 3},
    {"id": "liver_mr_t2_bright",        "name": "T2: Belirgin parlak (ampul bulb)",     "organ": "liver", "modality": "mr", "sequence": "t2",       "display_order": 4},
    {"id": "liver_mr_t2_mild_hyper",    "name": "T2: Hafif-orta hiperintens",           "organ": "liver", "modality": "mr", "sequence": "t2",       "display_order": 5},
    {"id": "liver_mr_t2_iso",           "name": "T2: İzointens / hipointens",           "organ": "liver", "modality": "mr", "sequence": "t2",       "display_order": 6},
    {"id": "liver_mr_t2_heterogen",     "name": "T2: Heterojen",                        "organ": "liver", "modality": "mr", "sequence": "t2",       "display_order": 7},
    {"id": "liver_mr_dwi_restrict",     "name": "DWI: Kısıtlama var",                   "organ": "liver", "modality": "mr", "sequence": "dwi",      "display_order": 8},
    {"id": "liver_mr_dwi_free",         "name": "DWI: Serbest difüzyon (ADC yüksek)",   "organ": "liver", "modality": "mr", "sequence": "dwi",      "display_order": 9},
    {"id": "liver_mr_aphe",             "name": "Kontrast: APHE (non-rim)",              "organ": "liver", "modality": "mr", "sequence": "arterial", "display_order": 10},
    {"id": "liver_mr_rim_aphe",         "name": "Kontrast: Rim tarzı APHE",             "organ": "liver", "modality": "mr", "sequence": "arterial", "display_order": 11},
    {"id": "liver_mr_washout",          "name": "Kontrast: Washout (portal/geç faz)",   "organ": "liver", "modality": "mr", "sequence": "portal",   "display_order": 12},
    {"id": "liver_mr_peripheral_nod",   "name": "Kontrast: Periferik nodüler dolum",    "organ": "liver", "modality": "mr", "sequence": "arterial", "display_order": 13},
    {"id": "liver_mr_persist_enhance",  "name": "Kontrast: Persistan geç faz",          "organ": "liver", "modality": "mr", "sequence": "delayed",  "display_order": 14},
    {"id": "liver_mr_capsule",          "name": "Kontrast: Enhancing kapsül",           "organ": "liver", "modality": "mr", "sequence": "portal",   "display_order": 15},
    {"id": "liver_mr_avascular",        "name": "Kontrast: Avasküler",                  "organ": "liver", "modality": "mr", "sequence": "arterial", "display_order": 16},
    {"id": "liver_mr_hbp_hyper",        "name": "HBP: Hiperintens (gadoxetat)",         "organ": "liver", "modality": "mr", "sequence": "hbp",      "display_order": 17},
    {"id": "liver_mr_hbp_iso",          "name": "HBP: İzointens (gadoxetat)",           "organ": "liver", "modality": "mr", "sequence": "hbp",      "display_order": 18},
    {"id": "liver_mr_hbp_hypo",         "name": "HBP: Hipointens (gadoxetat)",          "organ": "liver", "modality": "mr", "sequence": "hbp",      "display_order": 19},
]


# ── DIAGNOSES ─────────────────────────────────────────────────────────────────

DIAGNOSES = [
    {
        "id": "hcc",
        "name": "Hepatoselüler Karsinom (HKH)",
        "name_en": "Hepatocellular Carcinoma",
        "organ": "liver",
        "icd10": "C22.0",
        "risk_level": "yuksek",
        "lirads": "LR-5",
        "source": "LI-RADS v2018, AASLD 2023",
        "report_template": "Karaciğer [segment]'de [boyut] mm çaplı, T2'de hafif hiperintens, arteryel fazda non-rim hiperenhancement gösteren, portal/geç fazda washout izlenen lezyon saptanmaktadır. LI-RADS v2018 kriterleri doğrultusunda LR-5 (kesin hepatoselüler karsinom) ile uyumludur. MDT değerlendirmesi önerilir.",
        "differentials": ["icc", "hca", "fnh", "metastasis"]
    },
    {
        "id": "icc",
        "name": "İntrahepatik Kolanjioselüler Karsinom",
        "name_en": "Intrahepatic Cholangiocarcinoma",
        "organ": "liver",
        "icd10": "C22.1",
        "risk_level": "yuksek",
        "lirads": "LR-M",
        "source": "LI-RADS v2018, EASL 2022",
        "report_template": "Karaciğer [segment]'de rim tarzı arteryel enhancement gösteren, geç fazda persistan enhancement izlenen, DWI kısıtlama gösteren lezyon saptanmaktadır. LR-M kriterleri taşıyan bulgular intrahepatik kolanjioselüler karsinom ile uyumludur. Biyopsi ve MDT önerilir.",
        "differentials": ["hcc", "metastasis"]
    },
    {
        "id": "hemangioma",
        "name": "Hemanjiom",
        "name_en": "Hepatic Hemangioma",
        "organ": "liver",
        "icd10": "D18.09",
        "risk_level": "dusuk",
        "lirads": "LR-1",
        "source": "EASL 2016, ACG 2024",
        "report_template": "Karaciğer [segment]'de [boyut] mm çaplı, T2'de belirgin hiperintens (ampul bulb işareti), arteryel fazda periferik nodüler enhancement gösteren ve geç fazda progresif santral dolum izlenen lezyon saptanmaktadır. Bulgular tipik hemanjiom ile uyumludur.",
        "differentials": ["metastasis", "hcc"]
    },
    {
        "id": "simple_cyst",
        "name": "Basit Kist",
        "name_en": "Simple Hepatic Cyst",
        "organ": "liver",
        "icd10": "K76.89",
        "risk_level": "dusuk",
        "lirads": "LR-1",
        "source": "ACG 2024, ACR",
        "report_template": "Karaciğer [segment]'de [boyut] mm çaplı, anekoik / su dansitesinde, ince duvarlı, enhancement göstermeyen kistik lezyon izlenmektedir. Bulgular basit kist ile uyumludur.",
        "differentials": ["hydatid_cyst", "abscess"]
    },
    {
        "id": "fnh",
        "name": "Fokal Nodüler Hiperplazi (FNH)",
        "name_en": "Focal Nodular Hyperplasia",
        "organ": "liver",
        "icd10": "K76.89",
        "risk_level": "dusuk",
        "lirads": "LR-1",
        "source": "EASL 2016, ACG 2024",
        "report_template": "Karaciğer [segment]'de arteryel fazda belirgin hiperenhancement gösteren, portal/geç fazda izosinyal izlenen lezyon mevcuttur. Hepatobiliyer fazda hiper/izointensitesi ile birlikte bulgular FNH ile uyumludur. Takip gerekmemektedir.",
        "differentials": ["hca", "hcc"]
    },
    {
        "id": "hca",
        "name": "Hepatik Adenom",
        "name_en": "Hepatocellular Adenoma",
        "organ": "liver",
        "icd10": "D13.4",
        "risk_level": "orta",
        "lirads": "LR-M",
        "source": "EASL 2016, ACG 2024",
        "report_template": "Karaciğer [segment]'de T1 kimyasal kayma sekansında sinyal düşümü gösteren, arteryel fazda hiperenhancement izlenen, hepatobiliyer fazda hipointens lezyon saptanmaktadır. Bulgular hepatoselüler adenom (HNF-1α subtipi) ile uyumludur. Klinik değerlendirme önerilir.",
        "differentials": ["fnh", "hcc"]
    },
    {
        "id": "metastasis",
        "name": "Karaciğer Metastazı",
        "name_en": "Liver Metastasis",
        "organ": "liver",
        "icd10": "C78.7",
        "risk_level": "yuksek",
        "lirads": "LR-M",
        "source": "ACG 2024, ACR",
        "report_template": "Karaciğer'de çok sayıda, değişken boyutlarda fokal lezyon saptanmaktadır. Klinik bilgi ile birlikte metastatik tutulum ile uyumludur. Evreleme amacıyla toraks-abdomen-pelvis BT önerilir.",
        "differentials": ["hcc", "icc", "hemangioma"]
    },
    {
        "id": "abscess",
        "name": "Karaciğer Apsesi",
        "name_en": "Hepatic Abscess",
        "organ": "liver",
        "icd10": "K75.0",
        "risk_level": "yuksek",
        "lirads": None,
        "source": "ACG 2024",
        "report_template": "Karaciğer [segment]'de heterojen içerikli, düzensiz sınırlı, rim enhancement gösteren lezyon saptanmaktadır. Klinik bulgularla birlikte apse ile uyumludur. Kontrastlı BT ve klinik korelasyon önerilir.",
        "differentials": ["simple_cyst", "metastasis", "icc"]
    },
    {
        "id": "hydatid_cyst",
        "name": "Hidatik Kist",
        "name_en": "Hydatid Cyst",
        "organ": "liver",
        "icd10": "B67.0",
        "risk_level": "orta",
        "lirads": None,
        "source": "WHO 2003, ACG 2024",
        "report_template": "Karaciğer [segment]'de kalsifik duvarlı, iç membran / kız kesecik içeren kistik lezyon izlenmektedir. Ekinokokkoz ile uyumlu bulgular mevcuttur. Seroloji ve MDT önerilir.",
        "differentials": ["simple_cyst", "abscess"]
    },
]


# ── FINDING → DIAGNOSIS ilişkileri (SUGGESTS / EXCLUDES) ─────────────────────
# weight: 0-1 (tanıya katkısı)
# required: bu bulgu olmadan tanı düşünülmez
# source: kaynak kılavuz

SUGGESTS = [
    # HKH
    {"finding": "liver_ct_aphe",          "diagnosis": "hcc", "weight": 0.85, "required": True,  "source": "LI-RADS v2018"},
    {"finding": "liver_ct_washout",        "diagnosis": "hcc", "weight": 0.85, "required": True,  "source": "LI-RADS v2018"},
    {"finding": "liver_ct_capsule",        "diagnosis": "hcc", "weight": 0.6,  "required": False, "source": "LI-RADS v2018"},
    {"finding": "liver_ct_threshold_growth","diagnosis": "hcc","weight": 0.6,  "required": False, "source": "LI-RADS v2018"},
    {"finding": "liver_mr_aphe",           "diagnosis": "hcc", "weight": 0.85, "required": True,  "source": "LI-RADS v2018"},
    {"finding": "liver_mr_washout",        "diagnosis": "hcc", "weight": 0.85, "required": True,  "source": "LI-RADS v2018"},
    {"finding": "liver_mr_capsule",        "diagnosis": "hcc", "weight": 0.6,  "required": False, "source": "LI-RADS v2018"},
    {"finding": "liver_mr_hbp_hypo",       "diagnosis": "hcc", "weight": 0.5,  "required": False, "source": "LI-RADS v2018"},
    {"finding": "liver_mr_t2_mild_hyper",  "diagnosis": "hcc", "weight": 0.4,  "required": False, "source": "LI-RADS v2018"},
    {"finding": "liver_mr_dwi_restrict",   "diagnosis": "hcc", "weight": 0.5,  "required": False, "source": "LI-RADS 2024"},
    {"finding": "liver_us_ceus_aphe",      "diagnosis": "hcc", "weight": 0.8,  "required": True,  "source": "CEUS LI-RADS 2017"},
    {"finding": "liver_us_ceus_washout",   "diagnosis": "hcc", "weight": 0.8,  "required": True,  "source": "CEUS LI-RADS 2017"},

    # ICC
    {"finding": "liver_ct_rim_aphe",       "diagnosis": "icc", "weight": 0.8,  "required": True,  "source": "LI-RADS v2018 LR-M"},
    {"finding": "liver_ct_persist_enhance","diagnosis": "icc", "weight": 0.7,  "required": False, "source": "EASL 2022"},
    {"finding": "liver_ct_capsular_retract","diagnosis":"icc", "weight": 0.65, "required": False, "source": "EASL 2022"},
    {"finding": "liver_ct_satellite",      "diagnosis": "icc", "weight": 0.5,  "required": False, "source": "EASL 2022"},
    {"finding": "liver_mr_rim_aphe",       "diagnosis": "icc", "weight": 0.8,  "required": True,  "source": "LI-RADS v2018 LR-M"},
    {"finding": "liver_mr_persist_enhance","diagnosis": "icc", "weight": 0.7,  "required": False, "source": "EASL 2022"},
    {"finding": "liver_mr_dwi_restrict",   "diagnosis": "icc", "weight": 0.65, "required": False, "source": "EASL 2022"},
    {"finding": "liver_mr_t2_mild_hyper",  "diagnosis": "icc", "weight": 0.4,  "required": False, "source": "EASL 2022"},

    # Hemanjiom
    {"finding": "liver_us_hyperechoic",    "diagnosis": "hemangioma", "weight": 0.7,  "required": False, "source": "EASL 2016"},
    {"finding": "liver_us_smooth_border",  "diagnosis": "hemangioma", "weight": 0.4,  "required": False, "source": "EASL 2016"},
    {"finding": "liver_us_post_acoustic",  "diagnosis": "hemangioma", "weight": 0.3,  "required": False, "source": "EASL 2016"},
    {"finding": "liver_ct_peripheral_nod", "diagnosis": "hemangioma", "weight": 0.85, "required": True,  "source": "EASL 2016"},
    {"finding": "liver_ct_fill_in",        "diagnosis": "hemangioma", "weight": 0.85, "required": True,  "source": "EASL 2016"},
    {"finding": "liver_mr_t2_bright",      "diagnosis": "hemangioma", "weight": 0.9,  "required": True,  "source": "EASL 2016"},
    {"finding": "liver_mr_peripheral_nod", "diagnosis": "hemangioma", "weight": 0.85, "required": True,  "source": "EASL 2016"},
    {"finding": "liver_mr_dwi_free",       "diagnosis": "hemangioma", "weight": 0.6,  "required": False, "source": "EASL 2016"},

    # Basit Kist
    {"finding": "liver_us_anechoic",       "diagnosis": "simple_cyst", "weight": 0.85, "required": True,  "source": "ACG 2024"},
    {"finding": "liver_us_post_acoustic",  "diagnosis": "simple_cyst", "weight": 0.7,  "required": True,  "source": "ACG 2024"},
    {"finding": "liver_us_avascular",      "diagnosis": "simple_cyst", "weight": 0.6,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_ct_water_density",  "diagnosis": "simple_cyst", "weight": 0.85, "required": True,  "source": "ACG 2024"},
    {"finding": "liver_ct_avascular",      "diagnosis": "simple_cyst", "weight": 0.8,  "required": True,  "source": "ACG 2024"},
    {"finding": "liver_ct_smooth_border",  "diagnosis": "simple_cyst", "weight": 0.5,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_mr_t2_bright",      "diagnosis": "simple_cyst", "weight": 0.8,  "required": True,  "source": "ACG 2024"},
    {"finding": "liver_mr_dwi_free",       "diagnosis": "simple_cyst", "weight": 0.7,  "required": True,  "source": "ACG 2024"},
    {"finding": "liver_mr_avascular",      "diagnosis": "simple_cyst", "weight": 0.8,  "required": True,  "source": "ACG 2024"},

    # FNH
    {"finding": "liver_ct_aphe",           "diagnosis": "fnh", "weight": 0.6,  "required": True,  "source": "EASL 2016"},
    {"finding": "liver_ct_central_scar",   "diagnosis": "fnh", "weight": 0.65, "required": False, "source": "EASL 2016"},
    {"finding": "liver_us_central_scar",   "diagnosis": "fnh", "weight": 0.5,  "required": False, "source": "EASL 2016"},
    {"finding": "liver_us_doppler_central","diagnosis": "fnh", "weight": 0.6,  "required": False, "source": "EASL 2016"},
    {"finding": "liver_mr_aphe",           "diagnosis": "fnh", "weight": 0.6,  "required": True,  "source": "EASL 2016"},
    {"finding": "liver_mr_hbp_hyper",      "diagnosis": "fnh", "weight": 0.95, "required": False, "source": "EASL 2016"},
    {"finding": "liver_mr_hbp_iso",        "diagnosis": "fnh", "weight": 0.7,  "required": False, "source": "EASL 2016"},
    {"finding": "liver_mr_t2_mild_hyper",  "diagnosis": "fnh", "weight": 0.4,  "required": False, "source": "EASL 2016"},

    # Adenom
    {"finding": "liver_mr_t1_chemshift",   "diagnosis": "hca", "weight": 0.85, "required": False, "source": "EASL 2016"},
    {"finding": "liver_mr_aphe",           "diagnosis": "hca", "weight": 0.6,  "required": True,  "source": "EASL 2016"},
    {"finding": "liver_mr_hbp_hypo",       "diagnosis": "hca", "weight": 0.75, "required": False, "source": "EASL 2016"},
    {"finding": "liver_mr_t2_mild_hyper",  "diagnosis": "hca", "weight": 0.5,  "required": False, "source": "EASL 2016"},

    # Metastaz
    {"finding": "liver_us_halo",           "diagnosis": "metastasis", "weight": 0.7,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_us_heterogeneous",  "diagnosis": "metastasis", "weight": 0.5,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_ct_irregular",      "diagnosis": "metastasis", "weight": 0.5,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_ct_satellite",      "diagnosis": "metastasis", "weight": 0.6,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_ct_rim_aphe",       "diagnosis": "metastasis", "weight": 0.5,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_mr_dwi_restrict",   "diagnosis": "metastasis", "weight": 0.5,  "required": False, "source": "ACG 2024"},

    # Apse
    {"finding": "liver_us_heterogeneous",  "diagnosis": "abscess", "weight": 0.5,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_us_irregular_border","diagnosis":"abscess", "weight": 0.6,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_us_ceus_rim",       "diagnosis": "abscess", "weight": 0.75, "required": False, "source": "EFSUMB 2020"},
    {"finding": "liver_ct_irregular",      "diagnosis": "abscess", "weight": 0.5,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_mr_t2_mild_hyper",  "diagnosis": "abscess", "weight": 0.4,  "required": False, "source": "ACG 2024"},
    {"finding": "liver_mr_dwi_restrict",   "diagnosis": "abscess", "weight": 0.6,  "required": False, "source": "ACG 2024"},

    # Hidatik Kist
    {"finding": "liver_ct_calcification",  "diagnosis": "hydatid_cyst", "weight": 0.7,  "required": False, "source": "WHO 2003"},
    {"finding": "liver_us_heterogeneous",  "diagnosis": "hydatid_cyst", "weight": 0.4,  "required": False, "source": "WHO 2003"},
    {"finding": "liver_mr_t2_bright",      "diagnosis": "hydatid_cyst", "weight": 0.5,  "required": False, "source": "WHO 2003"},
]


# ── EXCLUDES ilişkileri ────────────────────────────────────────────────────────

EXCLUDES = [
    {"finding": "liver_ct_rim_aphe",       "diagnosis": "hcc",        "weight": 0.9,  "reason": "Rim APHE LR-M kriteridir, HKH dışı maligniteye işaret eder"},
    {"finding": "liver_mr_rim_aphe",       "diagnosis": "hcc",        "weight": 0.9,  "reason": "Rim APHE LR-M kriteridir"},
    {"finding": "liver_ct_washout",        "diagnosis": "hemangioma", "weight": 0.8,  "reason": "Hemanjiomda washout görülmez"},
    {"finding": "liver_mr_washout",        "diagnosis": "hemangioma", "weight": 0.8,  "reason": "Hemanjiomda washout görülmez"},
    {"finding": "liver_mr_hbp_hyper",      "diagnosis": "hcc",        "weight": 0.7,  "reason": "HBP hiperintensitesi FNH'yi destekler, HKH'ya karşı"},
    {"finding": "liver_mr_hbp_hyper",      "diagnosis": "metastasis", "weight": 0.8,  "reason": "HBP hiperintensitesi hepatosit aktivitesini gösterir"},
    {"finding": "liver_ct_avascular",      "diagnosis": "hcc",        "weight": 0.85, "reason": "HKH hipervaskülerdir"},
    {"finding": "liver_ct_avascular",      "diagnosis": "hemangioma", "weight": 0.7,  "reason": "Hemanjiom periferik nodüler enhancement gösterir"},
    {"finding": "liver_mr_washout",        "diagnosis": "fnh",        "weight": 0.75, "reason": "FNH'da washout görülmez — HKH'dan ayırt edici"},
    {"finding": "liver_mr_washout",        "diagnosis": "hca",        "weight": 0.5,  "reason": "Adenomda washout nadir"},
]


# ── ClinicalContext ağırlık modifikasyonları ──────────────────────────────────

CONTEXT_MODIFIERS = [
    {"context": "cirrhosis",          "finding": "liver_ct_aphe",  "diagnosis": "hcc", "multiplier": 2.0,  "reason": "Siroz zemininde APHE, HKH riskini dramatik artırır"},
    {"context": "cirrhosis",          "finding": "liver_mr_aphe",  "diagnosis": "hcc", "multiplier": 2.0,  "reason": "Siroz zemininde APHE, HKH riskini dramatik artırır"},
    {"context": "cirrhosis",          "finding": "liver_us_ceus_aphe","diagnosis":"hcc","multiplier": 1.8, "reason": "Siroz zemini"},
    {"context": "chronic_hbv",        "finding": "liver_ct_aphe",  "diagnosis": "hcc", "multiplier": 1.7,  "reason": "Kronik HBV, sirotik olmasa bile HKH riski taşır"},
    {"context": "chronic_hbv",        "finding": "liver_mr_aphe",  "diagnosis": "hcc", "multiplier": 1.7,  "reason": "Kronik HBV riski"},
    {"context": "known_malignancy",   "finding": "liver_ct_irregular","diagnosis":"metastasis","multiplier":2.5,"reason":"Bilinen malignite → metastaz önce düşün"},
    {"context": "known_malignancy",   "finding": "liver_us_halo",  "diagnosis": "metastasis","multiplier":2.5,"reason":"Bilinen malignite → metastaz"},
    {"context": "normal_background",  "finding": "liver_us_hyperechoic","diagnosis":"hemangioma","multiplier":1.8,"reason":"Normal KC'de hipereko → hemanjiom"},
    {"context": "young_female_ocs",   "finding": "liver_mr_aphe",  "diagnosis": "hca", "multiplier": 2.0,  "reason": "OKS + genç kadın → adenom riski"},
    {"context": "young_female_asymp", "finding": "liver_mr_aphe",  "diagnosis": "fnh", "multiplier": 1.8,  "reason": "Genç asemptomatik kadın → FNH riski"},
]


# ── Diagnosis → Action ilişkileri ─────────────────────────────────────────────

DIAGNOSIS_ACTIONS = [
    # HKH
    {"diagnosis": "hcc", "action": "mdt",           "urgency": "kritik", "order": 1},
    {"diagnosis": "hcc", "action": "afp",            "urgency": "yuksek", "order": 2},
    {"diagnosis": "hcc", "action": "staging_ct",     "urgency": "kritik", "order": 3},

    # ICC
    {"diagnosis": "icc", "action": "biopsy",         "urgency": "kritik", "order": 1},
    {"diagnosis": "icc", "action": "mdt",             "urgency": "kritik", "order": 2},
    {"diagnosis": "icc", "action": "mrcp",            "urgency": "yuksek", "order": 3},
    {"diagnosis": "icc", "action": "ca199_cea",       "urgency": "orta",   "order": 4},

    # Hemanjiom
    {"diagnosis": "hemangioma", "action": "no_followup",    "urgency": "elektif", "order": 1},
    {"diagnosis": "hemangioma", "action": "multiphase_mr",  "urgency": "orta",    "order": 2},

    # Basit Kist
    {"diagnosis": "simple_cyst", "action": "no_followup",   "urgency": "elektif", "order": 1},

    # FNH
    {"diagnosis": "fnh", "action": "gadoxetate_mr",         "urgency": "orta",    "order": 1},
    {"diagnosis": "fnh", "action": "no_followup",           "urgency": "elektif", "order": 2},

    # Adenom
    {"diagnosis": "hca", "action": "gadoxetate_mr",         "urgency": "yuksek",  "order": 1},
    {"diagnosis": "hca", "action": "ocs_cessation",         "urgency": "yuksek",  "order": 2},
    {"diagnosis": "hca", "action": "surgical_consult",      "urgency": "yuksek",  "order": 3},
    {"diagnosis": "hca", "action": "followup_6m_us",        "urgency": "orta",    "order": 4},

    # Metastaz
    {"diagnosis": "metastasis", "action": "staging_ct",     "urgency": "kritik",  "order": 1},
    {"diagnosis": "metastasis", "action": "mdt",             "urgency": "kritik",  "order": 2},
    {"diagnosis": "metastasis", "action": "biopsy",          "urgency": "yuksek",  "order": 3},

    # Apse
    {"diagnosis": "abscess", "action": "multiphase_ct",     "urgency": "kritik",  "order": 1},
    {"diagnosis": "abscess", "action": "surgical_consult",  "urgency": "kritik",  "order": 2},

    # Hidatik Kist
    {"diagnosis": "hydatid_cyst", "action": "hydatid_serology", "urgency": "orta", "order": 1},
    {"diagnosis": "hydatid_cyst", "action": "mdt",               "urgency": "orta", "order": 2},
]


# ── Diagnosis → Diagnosis (DIFFERENTIATES_FROM) ───────────────────────────────

DIFFERENTIATIONS = [
    {"from": "hcc",        "to": "icc",        "key_finding": "HKH: non-rim APHE + washout. ICC: rim APHE + persistan geç faz + kapsüler retraksiyon", "modality": "ct_mr"},
    {"from": "hcc",        "to": "metastasis",  "key_finding": "HKH: tekil, siroz zemini, washout. Metastaz: çoklu, bilinen primer, hipovasküler patern", "modality": "ct_mr"},
    {"from": "hemangioma", "to": "metastasis",  "key_finding": "Hemanjiom: T2 ampul bulb, periferik nodüler fill-in. Metastaz: target işareti, bilinen primer", "modality": "mr"},
    {"from": "fnh",        "to": "hca",         "key_finding": "FNH: HBP hiperintens, santral skar. Adenom: HBP hipointens, kimyasal kayma (HNF-1α)", "modality": "mr"},
    {"from": "fnh",        "to": "hcc",         "key_finding": "FNH: washout yok, HBP hiperintens. HKH: washout var, HBP hipointens, siroz zemini", "modality": "mr"},
    {"from": "simple_cyst","to": "hydatid_cyst","key_finding": "Basit kist: ince duvar, septa yok. Hidatik: kalsifik duvar, kız kesecikler, iç membran", "modality": "ct_mr"},
    {"from": "abscess",    "to": "metastasis",  "key_finding": "Apse: klinik (ateş, CRP), honeycomb US, rim enhancement. Metastaz: bilinen primer, soğuk klinik", "modality": "ct"},
]


# ── SEED FONKSİYONLARI ────────────────────────────────────────────────────────

def seed_findings(tx):
    for f in FINDINGS:
        tx.run("""
            MERGE (f:Finding {id: $id})
            SET f.name = $name,
                f.organ = $organ,
                f.modality = $modality,
                f.sequence = $sequence,
                f.display_order = $display_order
        """, **f)

        # Finding → Modality ilişkisi
        tx.run("""
            MATCH (f:Finding {id: $finding_id})
            MATCH (m:Modality {id: $modality_id})
            MERGE (m)-[:HAS_FINDING]->(f)
        """, finding_id=f["id"], modality_id=f["modality"])

    print(f"✓ {len(FINDINGS)} Finding düğümü oluşturuldu")


def seed_diagnoses(tx):
    for d in DIAGNOSES:
        tx.run("""
            MERGE (d:Diagnosis {id: $id})
            SET d.name = $name,
                d.name_en = $name_en,
                d.organ = $organ,
                d.icd10 = $icd10,
                d.risk_level = $risk_level,
                d.lirads = $lirads,
                d.source = $source,
                d.report_template = $report_template
        """, **{k: v for k, v in d.items() if k != "differentials"})

    print(f"✓ {len(DIAGNOSES)} Diagnosis düğümü oluşturuldu")


def seed_relationships(tx):
    # SUGGESTS
    for s in SUGGESTS:
        tx.run("""
            MATCH (f:Finding {id: $finding})
            MATCH (d:Diagnosis {id: $diagnosis})
            MERGE (f)-[r:SUGGESTS]->(d)
            SET r.weight = $weight,
                r.required = $required,
                r.source = $source
        """, **s)

    # EXCLUDES
    for e in EXCLUDES:
        tx.run("""
            MATCH (f:Finding {id: $finding})
            MATCH (d:Diagnosis {id: $diagnosis})
            MERGE (f)-[r:EXCLUDES]->(d)
            SET r.weight = $weight,
                r.reason = $reason
        """, **e)

    # CONTEXT_MODIFIERS
    for m in CONTEXT_MODIFIERS:
        tx.run("""
            MATCH (c:ClinicalContext {id: $context})
            MATCH (d:Diagnosis {id: $diagnosis})
            MERGE (c)-[r:MODIFIES_WEIGHT]->(d)
            SET r.finding_id = $finding,
                r.multiplier = $multiplier,
                r.reason = $reason
        """, **m)

    # DIAGNOSIS_ACTIONS
    for da in DIAGNOSIS_ACTIONS:
        tx.run("""
            MATCH (d:Diagnosis {id: $diagnosis})
            MATCH (a:Action {id: $action})
            MERGE (d)-[r:REQUIRES_ACTION]->(a)
            SET r.urgency = $urgency,
                r.order = $order
        """, **da)

    # DIFFERENTIATES_FROM
    for diff in DIFFERENTIATIONS:
        tx.run("""
            MATCH (d1:Diagnosis {id: $from})
            MATCH (d2:Diagnosis {id: $to})
            MERGE (d1)-[r:DIFFERENTIATES_FROM]->(d2)
            SET r.key_finding = $key_finding,
                r.modality = $modality
        """, **diff)

    print(f"✓ {len(SUGGESTS)} SUGGESTS ilişkisi")
    print(f"✓ {len(EXCLUDES)} EXCLUDES ilişkisi")
    print(f"✓ {len(CONTEXT_MODIFIERS)} MODIFIES_WEIGHT ilişkisi")
    print(f"✓ {len(DIAGNOSIS_ACTIONS)} REQUIRES_ACTION ilişkisi")
    print(f"✓ {len(DIFFERENTIATIONS)} DIFFERENTIATES_FROM ilişkisi")


# ── ÇALIŞTIR ──────────────────────────────────────────────────────────────────

with driver.session() as session:
    print("\n── Karaciğer Finding'leri yükleniyor...")
    session.execute_write(seed_findings)

    print("── Karaciğer Diagnosis'leri yükleniyor...")
    session.execute_write(seed_diagnoses)

    print("── İlişkiler yükleniyor...")
    session.execute_write(seed_relationships)

driver.close()

print("\n✓ Karaciğer bilgi grafı başarıyla oluşturuldu.")
print(f"  Bulgular : {len(FINDINGS)}")
print(f"  Tanılar  : {len(DIAGNOSES)}")
print(f"  İlişkiler: {len(SUGGESTS) + len(EXCLUDES) + len(CONTEXT_MODIFIERS) + len(DIAGNOSIS_ACTIONS) + len(DIFFERENTIATIONS)}")

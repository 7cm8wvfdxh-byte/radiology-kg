from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

CONCEPTS = [

    # ── KATMAN 3: TAM TANI KRİTERLERİ ────────────────────────────────────────

    {
        "id": "lirads_major_features_full",
        "name": "LI-RADS Majör Özellikler — Tam Kriter Seti",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "LI-RADS v2018'de 5 majör özellik HKH tanısını belirler: non-rim APHE, non-periferik washout, enhancing kapsül, eşik büyüme ve boyut. Her özelliğin kesin tanımı ve sınırı bilinmeli.",
        "why_matters": "Majör özellikleri yüzeysel bilmek yetmez. 'APHE var' demek değil — non-rim mi rim mi? Washout non-periferik mi periferik mi? Bu ayrımlar LR-5 ile LR-M arasındaki farkı belirler.",
        "key_points": [
            "APHE (non-rim): arteriyel fazda lezyon çevre parankimden belirgin parlak — RIM değil",
            "Washout (non-periferik): portal/geç fazda lezyon çevreden koyu — PERİFERİK değil",
            "Enhancing kapsül: portal/geç fazda lezyon çevresinde düzgün ince enhancement",
            "Eşik büyüme: ≤6 ayda ≥%50 boyut artışı (2018 değişiklik: alt sınır kaldırıldı)",
            "Boyut: ≥10 mm LI-RADS uygulanabilir; <10 mm → LR-3 maksimum",
            "LR-5 kuralı: APHE + (washout VEYA kapsül VEYA eşik büyüme) + boyuta göre",
            "Hiçbir yardımcı özellik majör özellik kullanılarak LR-5'e yükseltemez"
        ],
        "source": "ACR LI-RADS v2018, Chernyak Radiology 2018, PMC 6677371"
    },
    {
        "id": "lirads_ancillary_features",
        "name": "LI-RADS Yardımcı Özellikler (Ancillary Features)",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Yardımcı özellikler majör özelliklerin yetersiz kaldığı durumlarda kategoriyi 1 basamak yükseltir veya düşürür. LR-5'e yükseltmek için KULLANILAMAZlar.",
        "why_matters": "LR-3 lezyonda yardımcı özellikler LR-4'e yükseltebilir → takip sıklığı değişir. Yardımcı özellikleri bilmemek borderline vakaları kaçırmak demek.",
        "key_points": [
            "MALİGNİTE GENEL: DWI kısıtlama, hafif-orta T2 hiperintensite, corona enhancement",
            "HKH ÖZGÜN: lezyon içi yağ (çevreden fazla), eşik büyüme (subthreshold)",
            "HKH ÖZGÜN: mozaik mimari, nodül-içinde-nodül, HBP hipointensite",
            "BENİGN: HBP hiperintensite, kesin hemanjiom bulguları, kist kriterleri",
            "Kullanım kuralı: 1 basamak yükselt VEYA düşür — LR-5 olamaz",
            "DWI kısıtlama LI-RADS 2024'te ek AF olarak resmileşti",
            "HBP hipointensitesi: yüksek sensitivite (%94) ama düşük spesifisite"
        ],
        "source": "RadioGraphics LI-RADS 2018 Ancillary Features, PMC 8340355, Kierans 2025"
    },
    {
        "id": "lirads_lr_categories_decision",
        "name": "LI-RADS Karar Ağacı — Hangi Lezyon Hangi Kategori?",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "LI-RADS kategorisi boyut + majör özellik kombinasyonuna göre belirlenir. Pratik karar ağacı: önce boyut, sonra APHE durumu, sonra ek majör özellikler.",
        "why_matters": "Teorik bilgi ile pratik uygulama arasındaki köprü bu karar ağacı. Vakaya bakınca otomatik düşünmen gereken akış.",
        "key_points": [
            "<10 mm: APHE + 1 majör özellik → maksimum LR-3",
            "10-19 mm: APHE + washout → LR-5 (v2018 kritik değişiklik — öncesinde LR-4)",
            "10-19 mm: APHE + 1 majör özellik (kapsül/büyüme) → LR-5",
            "10-19 mm: sadece APHE → LR-4",
            "≥20 mm: APHE + 1 majör özellik → LR-5",
            "≥20 mm: sadece APHE → LR-4",
            "Rim APHE VEYA periferik washout → LR-M (HKH dışı malignite)"
        ],
        "source": "ACR LI-RADS v2018 Core, Radiology Assistant LI-RADS"
    },
    {
        "id": "hcc_bclc_staging",
        "name": "HKH Evreleme — BCLC Sistemi ve Tedavi Algoritması",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "BCLC (Barcelona Clinic Liver Cancer) sistemi HKH'de global standart evreleme ve tedavi algoritmasıdır. Tümör karakteristikleri + karaciğer fonksiyonu + performans durumu birlikte değerlendirilir.",
        "why_matters": "Radyolog LR-5 dediğinde klinisyen BCLC evresi sorar. Evreyi bilmeden tedaviye yönlendiremezsin. Rezeksiyon mu? Ablasyon mu? Transplantasyon mu? BCLC belirler.",
        "key_points": [
            "BCLC 0 (çok erken): <2 cm, tek, Child-Pugh A → rezeksiyon veya ablasyon",
            "BCLC A (erken): 1-3 nodül ≤3 cm veya tek ≤5 cm, Child-Pugh A-B → rezeksiyon/transplant/ablasyon",
            "BCLC B (orta): çok nodüllü, portal invazyon yok → TACE",
            "BCLC C (ileri): portal invazyon veya ekstrahepatik yayılım → sistemik tedavi (sorafenib/atezolizumab)",
            "BCLC D (terminal): ağır karaciğer disfonksiyonu → palyatif",
            "Milan kriterleri: transplant için — tek ≤5 cm veya ≤3 nodül her biri ≤3 cm",
            "Down-staging: TACE ile Milan kriterlerine indirme sonrası transplant mümkün"
        ],
        "source": "EASL 2018, AASLD 2023, Llovet Nature Reviews 2021"
    },
    {
        "id": "dysplastic_nodule_hcc",
        "name": "Displastik Nodül → HKH Dönüşümü — Multistep Karsinogenez",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Siroz zemininde rejenerasyon nodülü → düşük dereceli displastik nodül → yüksek dereceli displastik nodül → erken HKH → gelişmiş HKH. Her adımda görüntüleme bulguları değişir.",
        "why_matters": "Displastik nodülü HKH'dan ayırt etmek klinik pratiğin en zor sorusudur. Multistep karsinogenezi anlamak bu ayırımı kolaylaştırır.",
        "key_points": [
            "Rejenerasyon nodülü: portal ve arteryel kanlanmalı — T2 izointens, T1 değişken",
            "Düşük dereceli DN: benign görünüm — T2 hafif hipointens, siderotik olabilir",
            "Yüksek dereceli DN: arteryel kanlanma artmaya başlar — APHE minimal/yok",
            "Erken HKH: APHE var ama washout yok — LR-4 kategori",
            "Gelişmiş HKH: APHE + washout + kapsül — LR-5",
            "Nodül-içinde-nodül: HKH'nın DN içinde gelişmesi — yardımcı özellik",
            "DWI kısıtlama: DN-HKH dönüşümünde erken işaret (sensitivite %59)"
        ],
        "source": "LI-RADS v2018, Radiology AJR 2023, PubMed 31599447"
    },
    {
        "id": "icc_full_criteria",
        "name": "İntrahepatik Kolanjiyoselüler Karsinom — Tam Tanı Kriterleri",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "ICC karaciğerin ikinci en sık primer malign tümörü. LR-M kriterleri taşır. Erken evrede rezeksiyon mümkün, geç evrede prognoz kötü. HKH'dan kesin ayırım tedavi planını değiştirir.",
        "why_matters": "ICC'yi HKH olarak raporlamak yanlış tedaviye yol açar. HKH → transplant/ablasyon. ICC → sadece rezeksiyon, transplant endikasyonu yok.",
        "key_points": [
            "LR-M kriterleri: rim APHE + periferik washout + kapsüler retraksiyon + satellit",
            "Geç faz persistan enhancement: fibröz stroma içinde kontrast kalır",
            "DWI belirgin kısıtlama: düşük ADC değeri",
            "MR T2: heterojen, orta derecede hiperintens",
            "Satellit lezyon ve safra yolu dilatasyonu eşlik edebilir",
            "Vasküler invazyon: HKH'da portal ven, ICC'de hepatik ven daha sık",
            "Biyopsi gerekli: LR-M → biyopsisiz tedavi başlanamaz",
            "CA 19-9 yüksek, AFP genellikle normal"
        ],
        "source": "LI-RADS v2018 LR-M, EASL 2022 ICC, Radiology Key"
    },
    {
        "id": "hemangioma_variants",
        "name": "Hemanjiom Varyantları — Atipik Formlar ve Tuzaklar",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Tipik hemanjiomun yanı sıra flash fill, sklerotik, dev ve pediyatrik varyantlar farklı görünüm gösterir. Atipik hemanjiom HKH veya metastaz ile karışabilir — tuzakları bilmek şart.",
        "why_matters": "Flash fill hemanjiom arteryel fazda HKH gibi görünür — fark nedir? Sklerotik hemanjiom ICC gibi görünebilir. Bu ayrımları bilmeden gereksiz biyopsi yapılır.",
        "key_points": [
            "Flash fill hemanjiom: tüm fazlarda eşanlı dolum — çok küçük (<1.5 cm) lezyonlarda",
            "Flash fill vs HKH: flash fill'de washout YOK, tüm fazlarda yüksek sinyal",
            "Sklerotik hemanjiom: fibröz doku dominant — T2'de az parlak, geç faz enhancement",
            "Sklerotik vs ICC: ICC'de DWI kısıtlama belirgin, kapsüler retraksiyon var",
            "Dev hemanjiom (>10 cm): santral heterojenite (tromboz/fibrozis), periferde klasik",
            "T2 ampul bulb: tüm varyantlarda en güvenilir bulgu — BOS kadar parlak",
            "Hipointens hemanjiom: T1 hiperintens içerik (trombüs, protein) — T2'de yine parlak"
        ],
        "source": "EASL 2016, ACG 2024, Radiology Key Hemangioma Variants"
    },
    {
        "id": "adenoma_subtypes_full",
        "name": "Hepatik Adenom Subtipleri — 4 Tip Tam Kriterleri",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Hepatik adenomun 4 moleküler subtipi vardır: HNF-1α inaktive, inflamatuar, β-katenin aktive, SSH/unclassified. Her subtipin MR görünümü ve klinik riski farklıdır.",
        "why_matters": "β-katenin aktive subtipin malignite riski var — biyopsi gerektirir. HNF-1α'yı yanlış tanımlamak gereksiz cerrahi doğurabilir. Subtipler tedavi kararını değiştirir.",
        "key_points": [
            "HNF-1α inaktive (%30-40): T1 kimyasal kayma sinyal düşümü (yağ), HBP hipointens",
            "İnflamatuar (%40-50): T2 belirgin parlak (atoll işareti), sinüzoidal dilatasyon",
            "β-katenin aktive (%10-15): görüntüleme özgün değil, malignite riski → biyopsi",
            "SSH/unclassified (%5-10): özgün özellik yok",
            "Tüm tipler: arteryel hiperenhancement + portal fazda izodans (washout yok)",
            "HBP: tüm tipler hipointens — FNH'dan bu şekilde ayırılır",
            "Boyut ≥5 cm → kanama riski artmış, cerrahi değerlendirme",
            "OKS kesimi + 6 ay MR takip: ≥5 cm ise gerileme bekle, gerilemezse cerrahi"
        ],
        "source": "EASL 2016, ACG 2024, Radiology ACG Adenoma Guidelines"
    },
    {
        "id": "cyst_characterization_full",
        "name": "Kistik Karaciğer Lezyonları — Tam Karakterizasyon",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Basit kist, komplike kist, musinöz kistik neoplazm, hidatik kist ve kistik metastaz farklı yönetim gerektirir. Her birinin görüntüleme kriterleri net olmalı.",
        "why_matters": "Basit kistte takip gereksizken musinöz kistik neoplazm rezeksiyon gerektirebilir. Hidatik kiste girişim anaflaksi riski taşır. Ayırım hayati.",
        "key_points": [
            "Basit kist: anekoik/su dansitesi + ince duvar + septa yok + enhancement yok",
            "Komplike kist: kanama (T1 parlak) veya enfeksiyon (debris, duvar kalın)",
            "Musinöz kistik neoplazm (MCN): kadın, tek, büyük, septasyonlu, duvar nodülleri",
            "Hidatik kist: kalsifik duvar + kız kesecikler + iç membran + dekolman (nilüfer çiçeği)",
            "Hidatik WHO sınıflaması: CE1-5 (aktif→inaktif→kalsifiye)",
            "Kistik metastaz: bilinen primer + solid komponent + enhancement",
            "BT HU <20 = sıvı içerik; HU 20-40 = protein/kanama şüphesi → MR"
        ],
        "source": "ACG 2024, WHO Hidatik Kist 2003, EASL, Radiology Key"
    },
    {
        "id": "metastasis_patterns_full",
        "name": "Karaciğer Metastazları — Primer Tümöre Göre Paternler",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Karaciğer metastazının görüntüleme paterni primer tümöre göre değişir. Hipovasküler vs hipervasküler ayrımı hem tanı hem de tetkik seçimini etkiler.",
        "why_matters": "NET metastazını kolorektal metastaz gibi değerlendirmek tetkik protokolünü yanlış seçmek demek. Hipervasküler metastaz portal fazda kaybolur — arteryel faz gerekir.",
        "key_points": [
            "Hipovasküler (en sık): kolorektal, meme, akciğer, pankreas → portal fazda hipodens",
            "Hipervasküler: NET, böbrek hücreli, tiroid, melanom, meme bazı alt tipleri",
            "Target/bull's eye işareti: periferik enhancement + merkez nekroz — portal fazda",
            "Kalsifiye metastaz: kolorektal mucinöz, osteosarkom, over",
            "Kistik metastaz: over, pankreas, NET mucinöz",
            "Diffüz milier metastaz: meme, melanom, küçük hücreli akciğer",
            "Portal fazda en belirgin: hipovasküler metastaz burada en iyi görünür",
            "DWI: metastazlar diffüzyon kısıtlar — küçük lezyonların tespitini artırır"
        ],
        "source": "ACG 2024, Radiology Key Metastasis, EASL"
    },
    {
        "id": "liver_abscess_types",
        "name": "Karaciğer Apseleri — Piyojenik vs Amipli vs Mantar",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Piyojenik apse en sık, genellikle biliyer veya portal kökenli. Amipli apse tropik bölgelerde, seyahat öyküsü. Her ikisinin görüntüleme ve klinik özellikleri farklıdır.",
        "why_matters": "Apseyi nekrotik tümörle karıştırmak hayati hata. Klinik entegrasyon (ateş, CRP, seyahat öyküsü) görüntülemeyi tamamlar. Drenaj planı radyolog çağırır.",
        "key_points": [
            "Piyojenik apse: biliyer (kolanjit), portal (apandisit, divertikülit) veya hematojen",
            "Kriptojenik (%20-30): kaynak bulunamaz",
            "Görüntüleme: kalın rim enhancement + merkez avasküler + DWI kısıtlama",
            "Küme işareti (cluster sign): birleşen multiloküler apselerin karakteristik görünümü",
            "Amipli apse: sağ lob tutulumu sık, E. histolytica, tek büyük lezyon",
            "Amipli: seroloji pozitif, ince duvar, US'de homojen hipoekoik (mayonez benzetmesi)",
            "CEUS'te honeycomb görünüm: piyojenik apsenin karakteristik bulgusu",
            "Fungal apse: immünosuprese hastada, çok küçük (<1 cm) multipl lezyon"
        ],
        "source": "ACG 2024, EASL, Radiology Key Liver Abscess, EFSUMB CEUS 2020"
    },
]

# ── ÖNKOŞUL İLİŞKİLERİ ───────────────────────────────────────────────────────
PREREQUISITES = [
    # LI-RADS tam kriter için temel lazım
    {"from": "concept_lirads",              "to": "lirads_major_features_full"},
    {"from": "concept_aphe",               "to": "lirads_major_features_full"},
    {"from": "concept_washout",            "to": "lirads_major_features_full"},
    {"from": "lirads_major_features_full", "to": "lirads_ancillary_features"},
    {"from": "concept_dwi",               "to": "lirads_ancillary_features"},
    {"from": "concept_hbp",               "to": "lirads_ancillary_features"},
    {"from": "lirads_ancillary_features",  "to": "lirads_lr_categories_decision"},
    {"from": "lirads_major_features_full", "to": "lirads_lr_categories_decision"},

    # BCLC için LI-RADS + siroz
    {"from": "concept_lirads",             "to": "hcc_bclc_staging"},
    {"from": "liver_cirrhosis_imaging",    "to": "hcc_bclc_staging"},
    {"from": "concept_hcc_pathophysiology","to": "hcc_bclc_staging"},

    # Displastik nodül
    {"from": "liver_cirrhosis_imaging",    "to": "dysplastic_nodule_hcc"},
    {"from": "lirads_major_features_full", "to": "dysplastic_nodule_hcc"},
    {"from": "concept_dwi",               "to": "dysplastic_nodule_hcc"},
    {"from": "concept_hbp",               "to": "dysplastic_nodule_hcc"},

    # ICC
    {"from": "concept_icc_vs_hcc",        "to": "icc_full_criteria"},
    {"from": "lirads_major_features_full", "to": "icc_full_criteria"},
    {"from": "concept_dwi",               "to": "icc_full_criteria"},

    # Hemanjiom varyantları
    {"from": "concept_hemangioma_pathophysiology", "to": "hemangioma_variants"},
    {"from": "contrast_dynamics_interactive",      "to": "hemangioma_variants"},

    # Adenom subtipleri
    {"from": "concept_fnh_vs_adenoma",    "to": "adenoma_subtypes_full"},
    {"from": "concept_hbp",              "to": "adenoma_subtypes_full"},
    {"from": "mr_physics_t1_t2",         "to": "adenoma_subtypes_full"},

    # Kist karakterizasyonu
    {"from": "liver_biliary_anatomy",     "to": "cyst_characterization_full"},
    {"from": "ct_physics_hu",            "to": "cyst_characterization_full"},
    {"from": "mr_physics_t1_t2",         "to": "cyst_characterization_full"},

    # Metastaz
    {"from": "contrast_dynamics_interactive", "to": "metastasis_patterns_full"},
    {"from": "liver_ct_protocol",         "to": "metastasis_patterns_full"},

    # Apse
    {"from": "liver_systematic_reading",  "to": "liver_abscess_types"},
    {"from": "concept_dwi",              "to": "liver_abscess_types"},
]

# ── CONCEPT → DIAGNOSIS ───────────────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "lirads_major_features_full",   "diagnosis": "hcc",       "relation": "DEFINES_CRITERIA"},
    {"concept": "lirads_ancillary_features",    "diagnosis": "hcc",       "relation": "SUPPORTS_DIAGNOSIS"},
    {"concept": "lirads_lr_categories_decision","diagnosis": "hcc",       "relation": "CATEGORIZES"},
    {"concept": "hcc_bclc_staging",             "diagnosis": "hcc",       "relation": "STAGES"},
    {"concept": "dysplastic_nodule_hcc",        "diagnosis": "hcc",       "relation": "PRECURSOR_OF"},
    {"concept": "icc_full_criteria",            "diagnosis": "icc",       "relation": "DEFINES_CRITERIA"},
    {"concept": "hemangioma_variants",          "diagnosis": "hemangioma","relation": "DEFINES_CRITERIA"},
    {"concept": "adenoma_subtypes_full",        "diagnosis": "hca",       "relation": "DEFINES_CRITERIA"},
    {"concept": "cyst_characterization_full",   "diagnosis": "simple_cyst","relation": "DEFINES_CRITERIA"},
    {"concept": "cyst_characterization_full",   "diagnosis": "hydatid_cyst","relation": "DEFINES_CRITERIA"},
    {"concept": "metastasis_patterns_full",     "diagnosis": "metastasis", "relation": "DEFINES_CRITERIA"},
    {"concept": "liver_abscess_types",          "diagnosis": "abscess",    "relation": "DEFINES_CRITERIA"},
]

# ── SORULAR ───────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_lirads5_10_19mm",
        "concept_id": "lirads_lr_categories_decision",
        "type": "multiple_choice",
        "question": "10-19 mm boyutundaki bir nodülde non-rim APHE ve non-periferik washout saptanıyor. LI-RADS kategorisi nedir?",
        "options": ["LR-3", "LR-4", "LR-5", "LR-M"],
        "correct": 2,
        "explanation": "LI-RADS v2018 kritik değişikliği: 10-19 mm nodülde APHE + washout = LR-5. Eski versiyonda (v2017 öncesi) bu kombinasyon LR-4 idi. v2018 ile AASLD 2018 kılavuzu uyumu sağlandı. Bu boyutta APHE + washout biyopsisiz HKH tanısı koymaya yeterlidir.",
        "level": 3
    },
    {
        "id": "q_ancillary_upgrade",
        "concept_id": "lirads_ancillary_features",
        "type": "multiple_choice",
        "question": "LR-3 kategorisindeki bir lezyon yardımcı özellikler kullanılarak hangi kategoriye yükseltilebilir?",
        "options": ["LR-2", "LR-4", "LR-5", "LR-M"],
        "correct": 1,
        "explanation": "Yardımcı özellikler maksimum 1 basamak yükseltir veya düşürür ve LR-5'e yükseltmek için kullanılamaz. LR-3'te yardımcı özellik varsa → LR-4 olur. LR-4'te yardımcı özellik varsa → LR-4 kalır (LR-5 olamaz). Bu kural özgüllüğü korumak için konulmuştur.",
        "level": 3
    },
    {
        "id": "q_bclc_staging",
        "concept_id": "hcc_bclc_staging",
        "type": "multiple_choice",
        "question": "Sirozlu hastada 4 cm tek HKH, portal invazyon yok, Child-Pugh A. BCLC evresi ve uygun tedavi nedir?",
        "options": [
            "BCLC 0 — ablasyon",
            "BCLC A — rezeksiyon veya transplantasyon değerlendirmesi",
            "BCLC B — TACE",
            "BCLC C — sorafenib"
        ],
        "correct": 1,
        "explanation": "BCLC A: tek nodül ≤5 cm veya 2-3 nodül her biri ≤3 cm, portal invazyon yok, Child-Pugh A-B. Tedavi: karaciğer rezervi yeterliyse rezeksiyon (tercih), yoksa transplantasyon (Milan kriterlerine giriyor), veya radyofrekans ablasyon. Milan kriterleri: tek ≤5 cm veya ≤3 nodül her biri ≤3 cm.",
        "level": 3
    },
    {
        "id": "q_flash_fill_hemangioma",
        "concept_id": "hemangioma_variants",
        "type": "multiple_choice",
        "question": "Flash fill hemanjiomun HKH'dan en önemli ayırt edici özelliği nedir?",
        "options": [
            "Boyutu küçük olması",
            "Portal/geç fazda washout GÖRÜLMEMESİ",
            "T1'de hiperintens olması",
            "Arteryel fazda enhancement göstermemesi"
        ],
        "correct": 1,
        "explanation": "Flash fill hemanjiom arteryel fazda tüm lezyonu eşanlı dolduğu için HKH'ya benzer. Kritik fark: portal ve geç fazlarda hemanjiom KAN HAVUZU ile eş sinyal kalır — washout olmaz. HKH'da ise portal/geç fazda washout görülür. T2'de ampul bulb işareti de hemanjioma işaret eder.",
        "level": 3
    },
    {
        "id": "q_adenoma_hbp",
        "concept_id": "adenoma_subtypes_full",
        "type": "multiple_choice",
        "question": "Gadoxetat MR'da hepatobiliyer fazda hipointens görünen lezyon — FNH mi, Adenom mu?",
        "options": [
            "FNH — hepatositler yoktur",
            "Adenom — OATP1B3 ekspresyonu bozuktur",
            "Belirsiz — HBP her ikisini de ayırt edemez",
            "HKH — HBP her zaman hipointenstir"
        ],
        "correct": 1,
        "explanation": "FNH normal hepatositler içerir ve OATP1B3 eksprese eder → HBP'de hiperintens veya izointens. Adenom'da ise hepatosit fonksiyonu ve OATP1B3 ekspresyonu bozuktur → HBP'de hipointens. Bu ayrım %95+ özgüllükle FNH-adenom tanısını koyar. HKH da hipointens ama APHE+washout ile ayrılır.",
        "level": 3
    },
    {
        "id": "q_icc_lrm",
        "concept_id": "icc_full_criteria",
        "type": "multiple_choice",
        "question": "LR-M kategorisinin klinik önemi nedir?",
        "options": [
            "Kesinlikle benign — takip gerekmiyor",
            "Kesin HKH — biyopsisiz tedavi başlanabilir",
            "HKH dışı malignite şüphesi — biyopsi ve MDT gerekli",
            "Belirsiz — 3 ayda tekrar görüntüleme yeterli"
        ],
        "correct": 2,
        "explanation": "LR-M: 'probably or definitely malignant, not HCC specific.' Rim APHE, periferik washout, kapsüler retraksiyon bu kategoriye işaret eder. Kolanjioselüler karsinom (ICC) en önemli ayırıcı tanı. LR-M'de HKH'dan farklı olarak biyopsisiz tedavi başlanamaz — patoloji doğrulaması gerekli. Yönetim tamamen farklı: ICC'de transplant endikasyonu yoktur.",
        "level": 3
    },
    {
        "id": "q_hydatid_who",
        "concept_id": "cyst_characterization_full",
        "type": "multiple_choice",
        "question": "Hidatik kist hangi görüntüleme bulgusu ile basit kistden en kolay ayrılır?",
        "options": [
            "Büyük boyutu",
            "Kalsifik duvar, iç membran veya kız kesecikler",
            "Posterior akustik güçlenme",
            "T2'de parlak sinyal"
        ],
        "correct": 1,
        "explanation": "Hidatik kistin patognomik bulguları: kalsifik duvar (WHO CE3-5), iç membran dekolmanı (nilüfer çiçeği - water lily sign), kız kesecikler (balık yumurtası görünümü). Basit kist ince duvarlıdır, iç membran ve kalsifikasyon yoktur. Tedavi yaklaşımı tamamen farklı: hidatik kiste perkutan girişim anaflaksi riski taşır — seroloji önce.",
        "level": 3
    },
    {
        "id": "q_metastasis_protocol",
        "concept_id": "metastasis_patterns_full",
        "type": "multiple_choice",
        "question": "NET (nöroendokrin tümör) karaciğer metastazlarını değerlendirmek için hangi BT protokolü tercih edilir?",
        "options": [
            "Sadece portal venöz faz yeterli",
            "Sadece natif faz",
            "Arteryel faz + Portal venöz faz (hipervasküler protokol)",
            "Geç faz yeterli"
        ],
        "correct": 2,
        "explanation": "NET metastazları hipervaskülerdir — arteryel fazda parlak görünür. Portal venöz fazda karaciğer parankimi yüksek dansitede olduğunda lezyon kaybolabilir. Bu nedenle hipervasküler protokol (arteryel + portal venöz faz) gerekir. Kolorektal gibi hipovasküler metastazlar için portal venöz faz tek başına yeterlidir.",
        "level": 3
    },
    {
        "id": "q_dysplastic_dwi",
        "concept_id": "dysplastic_nodule_hcc",
        "type": "multiple_choice",
        "question": "Siroz zemininde 15 mm lezyon: APHE var, washout yok, DWI kısıtlama var. En uygun yönetim nedir?",
        "options": [
            "LR-1 — kesinlikle benign, takip gerekmez",
            "LR-3 — 6 ayda MR kontrolü",
            "LR-4 (APHE tekbaşına) + DWI ile yardımcı özellik → LR-4 kalır, 3 ayda MR/BT",
            "LR-5 — biyopsisiz tedavi başla"
        ],
        "correct": 2,
        "explanation": "APHE tek başına 10-19 mm'de LR-4. DWI kısıtlama yardımcı özellik — LR-4'ü LR-5'e yükseltemez (ancillary features LR-5 yapamaz). Sonuç: LR-4, 3 ayda CT veya MR kontrolü önerilir. Eğer 3 ayda büyüme olursa eşik büyüme = LR-5. Bu örnekte LI-RADS sisteminin neden majör özellik sınırını koruduğunu anlamak kritik.",
        "level": 3
    },
]


# ── SEED ──────────────────────────────────────────────────────────────────────

def seed_concepts(tx):
    for c in CONCEPTS:
        tx.run("""
            MERGE (c:Concept {id: $id})
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

print("\n── Katman 3 yükleniyor...")
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
print(f"\n✓ Katman 3 tamamlandı — {len(CONCEPTS)} concept, {len(QUESTIONS)} soru")

from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

CONCEPTS = [

    # ── KATMAN 5: NADİR VARYANTLAR VE TUZAKLAR ───────────────────────────────

    {
        "id": "pitfall_pseudolesion",
        "name": "Karaciğer Psödolezyonları — Gerçek Olmayan Lezyonlar",
        "organ": "liver",
        "level": 5,
        "category": "technique",
        "summary": "Radyolojik incelemede gerçek lezyon gibi görünen ama aslında anatomik varyant veya artefakt olan durumlar. Bunları bilmemek gereksiz biyopsi ve yanlış tanıya yol açar.",
        "why_matters": "Deneyimli radyolog ile acemiyi ayıran en önemli fark psödolezyonları tanımaktır. Her arteryel enhancement gerçek lezyon değildir.",
        "key_points": [
            "AV şant: kama şekilli, portal fazda kaybolan arteryel enhancement — damar kökenli",
            "Fokal yağlı infiltrasyon: düzgün sınırsız, damarları iter değil içinden geçer",
            "Fokal yağ sparing: yağlı karaciğerde hiperekoik alan — lezyon değil, korunmuş alan",
            "Periportal ödem: portal triad çevresinde halo — ödem/lenfatik, kontrast almaz",
            "Üçüncü giriş etkisi (third inflow): safra kesesi fossası/falciform lig. çevresinde",
            "Parankimal perfüzyon değişikliği: portal ven dalı tıkanıklığı → segmental enhancement",
            "Reji hepatik arter kaynaklı pseudolezyon: hepatik arterin vena cava'ya direkt drenajı"
        ],
        "source": "Radiology Key Pseudolesions, RadioGraphics, ACR"
    },
    {
        "id": "pitfall_burnout_metastasis",
        "name": "Burn-out Tümör — Kendiliğinden Gerileyen Metastaz/HKH",
        "organ": "liver",
        "level": 5,
        "category": "pathology",
        "summary": "Karaciğer lezyonunun tedavi olmaksızın fibrozis, kalsifikasyon veya nekroz ile gerilediği nadir durum. Skar veya kalsifikasyon olarak kalabilir — aktif lezyon sanılabilir.",
        "why_matters": "Burn-out HKH veya metastaz rezidüel skar bırakır. Bunu aktif lezyon olarak raporlamak gereksiz tedaviye yol açar. Öyküyle korelasyon şart.",
        "key_points": [
            "Burn-out HKH: siroz zemininde fibrotik skar — T2 hipointens, enhancement yok",
            "Burn-out metastaz: kolorektal tedavi sonrası kalsifik skar — radyolojik yanıt",
            "Kalsifiye metastaz: tedavi sonrası → musinöz kolorektal, over, NET",
            "Önceki görüntülemelerle karşılaştırma zorunlu",
            "Aktif lezyon ayırımı: enhancement yoksa ve küçülüyorsa — burn-out",
            "Klinik bağlam kritik: kemoterapi almış hasta + kalsifik odak = responder"
        ],
        "source": "Radiology Key, ACG 2024, RadioGraphics Liver Pitfalls"
    },
    {
        "id": "pitfall_hemangioma_traps",
        "name": "Hemanjiom Tuzakları — Atipik Formlar",
        "organ": "liver",
        "level": 5,
        "category": "pathology",
        "summary": "Sklerotik hemanjiom, hipointens hemanjiom ve irrite olmuş hemanjiom atipik görünümler gösterir. ICC, metastaz veya HKH ile karışabilir.",
        "why_matters": "Atipik hemanjiomlar MR'da bile zor olabilir. T2'nin parlak olmadığı hemanjiom — başka tanı düşündürür. Bu tuzakları bilmek gereksiz biyopsiyi önler.",
        "key_points": [
            "Sklerotik hemanjiom: fibrozis dominant — T2 az parlak, geç faz persistent enhancement",
            "Hipointens hemanjiom: T1 hiperintens içerik (trombüs/protein) ama T2 hâlâ parlak",
            "İrrite/kasıntılı hemanjiom: çevre inflammasyon → perilesional ödem",
            "Hızlı dolan hemanjiom (flash fill): arteryel fazda tüm dolar — washout YOK",
            "Dev hemanjiom >10 cm: santral heterojenite, periferde klasik patern",
            "Tuzak: T2 ampul bulb YOKSA hemanjiom güvensiz — MR+CEUS değerlendirme",
            "CEUS: flash fill bile olsa gerçek zamanlı periferik nodüler dolum gösterir"
        ],
        "source": "EASL 2016, ACG 2024, RadioGraphics Hemangioma Variants"
    },
    {
        "id": "pitfall_hcc_mimics",
        "name": "HKH Taklitçileri — Yanlış LR-5 Tuzakları",
        "organ": "liver",
        "level": 5,
        "category": "pathology",
        "summary": "LR-5 kriterlerini karşılayan ama HKH olmayan lezyonlar: adenom, FNH (atipik), hipervasküler metastaz, ICC (erken), arteryovenöz malformasyon.",
        "why_matters": "Yanlış LR-5 tanısı yanlış tedaviye yol açar. LI-RADS sistemi >%95 özgüllük hedefler ama %100 değil. Atipik durumlarda biyopsi şart olabilir.",
        "key_points": [
            "Adenom: APHE + portal fazda isodans (washout yok) — LR-4 olabilir ama LR-5 değil",
            "ICC erken evre: bazen non-rim APHE gösterebilir → dikkatli",
            "Hipervasküler metastaz: APHE + washout OLUR (NET, RCC) — klinik bağlam",
            "Atipik FNH: washout gösteren vaka rapor edilmiş — nadiren LR-4/5 benzer",
            "Arteryovenöz malformasyon: büyük, multipl, damarla bağlantılı",
            "LR-5 ≠ %100 HKH: %95+ PPV ama biyopsi düşünülmeli atipik durumlarda",
            "Non-siroz LI-RADS uygulaması: daha düşük PPV, yanlış pozitif riski artmış"
        ],
        "source": "LI-RADS v2018, AASLD 2023, Radiology Key HCC Mimics"
    },
    {
        "id": "pitfall_focal_fat",
        "name": "Fokal Yağlı İnfiltrasyon ve Fokal Yağ Sparing — Lezyon Taklidi",
        "organ": "liver",
        "level": 5,
        "category": "pathology",
        "summary": "Diffüz yağlı karaciğerde fokal korunmuş alan (yağ sparing) veya fokal yağ birikimi lezyon gibi görünür. Her ikisi de benign — yönetim gerekmez.",
        "why_matters": "Yağlı karaciğerde US'de fokal hiperekoik alan ile metastaz veya HKH karışabilir. MR kimyasal kayma bu tuzağı çözer.",
        "key_points": [
            "Fokal yağ birikimi: damarları itmez, lobüler olmayan, düzgün sınır yok",
            "Fokal yağ sparing: safra kesesi fossası, falciform ligament, portal triad çevresi tipik",
            "MR in/out phase: yağ içeren bölgede out-phase'de sinyal düşümü — tanısal",
            "BT: yağ içeren bölge düşük HU, sparing normali kitlesi gibi görünür",
            "Doppler US: damarlar normal anatomik seyirde — lezyon değil",
            "Yağ sparing nedeni: lokal venöz drenaj farklılığı (3. giriş etkisi)",
            "Takip ve biyopsi gereksiz — MR ile kesin tanı"
        ],
        "source": "Radiology Key, ACG 2024, Radiopaedia Focal Fat"
    },
    {
        "id": "pitfall_periportal_tracking",
        "name": "Periportal İzlenme — Laserasyon mı, Ödem mi?",
        "organ": "liver",
        "level": 5,
        "category": "technique",
        "summary": "Portal triad çevresinde düşük dansiteli/sinyal alan: lenfatik genişleme, ödem, akut karaciğer hasarı veya travma sonrası görülebilir. Lezyon veya laserasyon sanılabilir.",
        "why_matters": "Travma BT'sinde periportal izlenmeyi laserasyon zannetmek AAST grade yükseltmeye ve gereksiz girişime yol açar. Doğru yorumlama kritik.",
        "key_points": [
            "Periportal düşük dansite: portal triad etrafında halo — lenfatik/ödem",
            "Travmada periportal izlenme: hipovolemik şok veya lenfatik yaralanma",
            "Laserasyon ayırımı: laserasyon lineer/yıldız şekilli, periportal dağılım göstermez",
            "Akut hepatit: periportal ödem yaygın — genç hastada düşün",
            "Konjestif hepatopati: periportal ödem + periferik sinüzoidal dilatasyon",
            "Aşırı IV sıvı: periportal ödem + diffüz karaciğer ödemi",
            "Safra yolu sızıntısı: post-op/travma → periportal sıvı koleksiyonu"
        ],
        "source": "RadioGraphics CT Blunt Trauma, Radiology Key, ACR"
    },
    {
        "id": "pitfall_mri_artifacts",
        "name": "Karaciğer MR Artefaktları — Tanıyı Bozan Durumlar",
        "organ": "liver",
        "level": 5,
        "category": "technique",
        "summary": "Gadoxetat arteryel faz artefaktı, nefes hareketi artefaktı, susceptibility artefaktı ve kimyasal kayma artefaktları yanlış tanıya yol açabilir.",
        "why_matters": "Artefaktı lezyon sanmak veya lezyonu artefakt sanmak — ikisi de tehlikeli. Teknik kaliteyi değerlendirme raporun ilk adımı.",
        "key_points": [
            "Gadoxetat arteryel faz artefaktı: %2-18 vakada geçici dispne → blurring",
            "Çözüm: yavaş enjeksiyon (1 mL/sn), triple arteryel faz, oksijen",
            "Nefes hareketi: hepatik ven/portal ven hayalet artefaktı — psödolezyon",
            "Susceptibility artefaktı: demir (hemokromatoz, siderotik nodül) sinyal kaybı",
            "Kimyasal kayma yanlış yorumu: in-phase'de yağ maskelenir, out-phase'de görünür",
            "Flow artefakt: hepatik vende yavaş akım → filling defect sanılır → trombüs taklidi",
            "Teknik kalite değerlendirmesi: LR-NC kategorisi — artefakt nedeniyle kategori verilemez"
        ],
        "source": "AJR Gadoxetate Part 1, ESGAR Consensus, Radiology Key MR Artifacts"
    },
    {
        "id": "pitfall_small_hcc_detection",
        "name": "Küçük HKH Tespiti — <2 cm Lezyonlarda Zorluklar",
        "organ": "liver",
        "level": 5,
        "category": "pathology",
        "summary": "2 cm altı HKH'da LI-RADS majör özellikleri daha az sıklıkla görülür. Erken HKH'nın displastik nodülden ayrımı radyolojik açıdan en zor sorudur.",
        "why_matters": "Erken HKH'nın tespiti en iyi tedavi şansı demek. <2 cm'de LR-5 kriterlerinin duyarlılığı düşer. Ek sekanslar ve takip protokolü kritik.",
        "key_points": [
            "<1 cm HKH: APHE sıklığı düşük, washout nadir — DWI kısıtlama en güvenilir bulgu",
            "1-2 cm HKH: APHE %88, washout %61, kapsül %33 — LR-4 sık",
            "Erken HKH: portalize yağ içerebilir, T2 hafif hiperintens, HBP hipointens başlar",
            "Gadoxetat MR: <2 cm HKH tespitinde ECA-MR'dan üstün",
            "DWI yüksek b değeri (b800): küçük lezyonlarda arka plan baskılanır, lezyon öne çıkar",
            "Surveyans US limitasyonu: <1 cm lezyonlarda duyarlılık çok düşük",
            "Takip protokolü: LR-3 → 3-6 ay MR, LR-4 → 3 ay MR/BT"
        ],
        "source": "LI-RADS 2024, AJR 2023 Small HCC, AASLD 2023"
    },
]

# ── ÖNKOŞULLAR ────────────────────────────────────────────────────────────────
PREREQUISITES = [
    {"from": "contrast_dynamics_interactive",  "to": "pitfall_pseudolesion"},
    {"from": "liver_ct_protocol",              "to": "pitfall_pseudolesion"},
    {"from": "liver_systematic_reading",       "to": "pitfall_pseudolesion"},

    {"from": "metastasis_patterns_full",       "to": "pitfall_burnout_metastasis"},
    {"from": "hcc_bclc_staging",              "to": "pitfall_burnout_metastasis"},

    {"from": "hemangioma_variants",           "to": "pitfall_hemangioma_traps"},
    {"from": "contrast_dynamics_interactive",  "to": "pitfall_hemangioma_traps"},
    {"from": "mr_physics_t1_t2",              "to": "pitfall_hemangioma_traps"},

    {"from": "lirads_lr_categories_decision", "to": "pitfall_hcc_mimics"},
    {"from": "dd_hypervascular_lesion",       "to": "pitfall_hcc_mimics"},
    {"from": "adenoma_subtypes_full",         "to": "pitfall_hcc_mimics"},

    {"from": "liver_fatty_infiltration",      "to": "pitfall_focal_fat"},
    {"from": "mr_physics_t1_t2",             "to": "pitfall_focal_fat"},
    {"from": "ct_physics_hu",                "to": "pitfall_focal_fat"},

    {"from": "liver_trauma_findings",         "to": "pitfall_periportal_tracking"},
    {"from": "liver_systematic_reading",      "to": "pitfall_periportal_tracking"},

    {"from": "liver_mr_protocol",            "to": "pitfall_mri_artifacts"},
    {"from": "liver_contrast_gadolinium",    "to": "pitfall_mri_artifacts"},
    {"from": "mr_physics_t1_t2",            "to": "pitfall_mri_artifacts"},

    {"from": "dysplastic_nodule_hcc",        "to": "pitfall_small_hcc_detection"},
    {"from": "lirads_ancillary_features",    "to": "pitfall_small_hcc_detection"},
    {"from": "concept_dwi",                 "to": "pitfall_small_hcc_detection"},
    {"from": "liver_mr_protocol",           "to": "pitfall_small_hcc_detection"},
]

# ── CONCEPT → DIAGNOSIS ───────────────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "pitfall_pseudolesion",        "diagnosis": "hcc",        "relation": "PITFALL_FOR"},
    {"concept": "pitfall_burnout_metastasis",  "diagnosis": "metastasis", "relation": "PITFALL_FOR"},
    {"concept": "pitfall_hemangioma_traps",    "diagnosis": "hemangioma", "relation": "PITFALL_FOR"},
    {"concept": "pitfall_hcc_mimics",          "diagnosis": "hcc",        "relation": "PITFALL_FOR"},
    {"concept": "pitfall_focal_fat",           "diagnosis": "hcc",        "relation": "PITFALL_FOR"},
    {"concept": "pitfall_small_hcc_detection", "diagnosis": "hcc",        "relation": "PITFALL_FOR"},
    {"concept": "pitfall_mri_artifacts",       "diagnosis": "hcc",        "relation": "TECHNIQUE_PITFALL"},
]

# ── SORULAR ───────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_pseudolesion_wedge",
        "concept_id": "pitfall_pseudolesion",
        "type": "multiple_choice",
        "question": "Arteryel fazda kama şeklinde, portal fazda tamamen kaybolan enhancement görüldüğünde LI-RADS kategorisi ne olur?",
        "options": [
            "LR-4 — APHE var, takip gerekli",
            "LR-5 — APHE + boyut uygun",
            "LR-1 — arteryovenöz şant, psödolezyon, gerçek lezyon değil",
            "LR-M — atipik enhancement"
        ],
        "correct": 2,
        "explanation": "Arteryovenöz şant (psödolezyon): kama şekilli, portal fazda tamamen kaybolan arteryel enhancement. Gerçek nodüler lezyon değil — LR-1. Portal fazda kayboluyor çünkü portal kan gelince arteryel kontrast dilüe oluyor. HKH'da washout görülür ama arteryel fazdan tamamen kaybolmaz, nodüler şekil alır.",
        "level": 5
    },
    {
        "id": "q_focal_fat_sparing",
        "concept_id": "pitfall_focal_fat",
        "type": "multiple_choice",
        "question": "Diffüz yağlı karaciğerde safra kesesi fossası yakınında US'de hiperekoik alan görülüyor. Ne düşünürsün?",
        "options": [
            "Metastaz — biyopsi",
            "HKH — multifazik BT",
            "Fokal yağ sparing — MR kimyasal kayma ile konfirmasyon, takip gerekmez",
            "Hemanjiom — MR T2"
        ],
        "correct": 2,
        "explanation": "Diffüz yağlı karaciğerde safra kesesi fossası ve falciform ligament çevresinde fokal yağ sparing tipiktir. 3. giriş etkisi (third inflow) bu bölgeleri yağ birikiminden korur. Hiperekoik değil — yağsız karaciğer parankimi çevreden daha ekojen görünür. MR in/out phase ile kesin tanı — out-phase'de yağlı alan sinyal düşürür, sparing alanı düşürmez.",
        "level": 5
    },
    {
        "id": "q_gadoxetate_artifact",
        "concept_id": "pitfall_mri_artifacts",
        "type": "multiple_choice",
        "question": "Gadoxetat MR'da arteryel fazda karaciğer görüntüsü bulanık (blurring). En olası neden ve çözüm?",
        "options": [
            "Hasta hareketi — sediasyon",
            "Gadoxetat'ın geçici dispne/nefes tutma güçlüğü artefaktı — yavaş enjeksiyon veya triple arteryel faz",
            "Kontrastın fazla verilmesi — doz azalt",
            "MR cihazının yetersizliği — yüksek Tesla lazım"
        ],
        "correct": 1,
        "explanation": "Gadoxetat ile %2-18 vakada geçici dispne görülür — bu nefes tutma güçlüğüne yol açar ve arteryel faz görüntüsünü bozar. Çözümler: (1) yavaş enjeksiyon 1 mL/sn, (2) triple arteryel faz ile en iyi faz seçimi, (3) enjeksiyon öncesi oksijen, (4) gadoxetatı %50 seyreltme. Bu artefakt LR-NC kategorisine yol açabilir.",
        "level": 5
    },
    {
        "id": "q_small_hcc_sequence",
        "concept_id": "pitfall_small_hcc_detection",
        "type": "multiple_choice",
        "question": "<1 cm HKH için en güvenilir tek MR bulgusu hangisidir?",
        "options": [
            "Arteryel hiperenhancement",
            "Enhancing kapsül",
            "DWI kısıtlama",
            "HBP hipointensitesi"
        ],
        "correct": 2,
        "explanation": "<1 cm HKH'da APHE sıklığı düşer, washout nadir, kapsül nadiren görülür. DWI kısıtlama bu boyutta en güvenilir bağımsız yardımcı özellik (adjusted odds ratio 11.50). HBP hipointensitesi yüksek sensitivite ama düşük spesifisite gösterir. AJR 2023 çalışması: <1 cm HKH için modifiye LI-RADS'a DWI eklenmesi sensitiviteyi artırdı.",
        "level": 5
    },
    {
        "id": "q_burnout_lesion",
        "concept_id": "pitfall_burnout_metastasis",
        "type": "multiple_choice",
        "question": "Kolorektal kanser kemoterapisi alan hastada önceki BT'de 2 cm metastaz vardı. Yeni BT'de aynı lokalizasyonda kalsifik odak var. Yorum?",
        "options": [
            "Yeni lezyon — biyopsi gerekli",
            "Kalsifiye metastaz — progresyon",
            "Burn-out tümör — radyolojik yanıt, aktif lezyon değil",
            "Hidatik kist — seroloji"
        ],
        "correct": 2,
        "explanation": "Kemoterapi sonrası bilinen metastaz lokalizasyonunda kalsifikasyon → burn-out/calcified metastasis = radyolojik yanıt işareti. Mucinöz kolorektal kanser metastazları kalsifiye olabilir. Aktif lezyon değil — enhancement yok. Önceki görüntülemelerle karşılaştırma ve klinik yanıt değerlendirmesi (CEA düzeyi) ile teyit edilir.",
        "level": 5
    },
    {
        "id": "q_sclerosed_hemangioma",
        "concept_id": "pitfall_hemangioma_traps",
        "type": "multiple_choice",
        "question": "MR'da T2'de hafif hiperintens, geç fazda persistan enhancement gösteren lezyon. T2 ampul bulb işareti yok. Öncelikli tanı?",
        "options": [
            "Tipik hemanjiom — takip gerekmez",
            "Sklerotik hemanjiom veya ICC — CEUS veya biyopsi değerlendirmesi",
            "HKH — LR-4",
            "Adenom — gadoxetat MR"
        ],
        "correct": 1,
        "explanation": "T2 ampul bulb yoksa hemanjiom güvensiz tanı. Sklerotik hemanjiom: fibrozis dominant → T2'de az parlak, geç faz persistan enhancement (fibröz stroma). ICC da geç fazda persistan enhancement + DWI kısıtlama gösterebilir. Ayırım: sklerotik hemanjiomda DWI kısıtlama yok veya hafif, ICC'de belirgin. CEUS veya MR takibi ile doğrulama.",
        "level": 5
    },
    {
        "id": "q_periportal_trauma",
        "concept_id": "pitfall_periportal_tracking",
        "type": "multiple_choice",
        "question": "Trafik kazası sonrası BT'de karaciğerde belirgin laserasyon yok, portal triad çevresinde düşük dansiteli halo var. AAST grade kaç?",
        "options": [
            "Grade III — ciddi laserasyon",
            "Grade I — periportal izlenme izole AAST Grade I bulgusudur",
            "Grade IV — portal ven yaralanması",
            "Travma yok — normal varyant"
        ],
        "correct": 1,
        "explanation": "İzole periportal düşük dansite (periportal blood tracking/ödem) AAST 2018'de Grade I bulgusu olarak tanımlanmıştır. Laserasyon değil — portal triad çevresinde ödem veya lenfatik. Grade yükseltmek için parankimal laserasyon, hematom veya vasküler yaralanma gerekir. Bu hastada nonoperatif yönetim uygundur.",
        "level": 5
    },
    {
        "id": "q_hcc_mimic_net",
        "concept_id": "pitfall_hcc_mimics",
        "type": "multiple_choice",
        "question": "Sirozlu olmayan hastada 3 cm lezyon: APHE + washout var. LI-RADS uygulanabilir mi ve tanı ne olabilir?",
        "options": [
            "LR-5 — kesin HKH, biyopsi gerekmez",
            "LI-RADS siroz olmayan hastaya uygulanamaz — ayırıcı tanı: NET metastazı, RCC metastazı veya HKH, biyopsi gerekli",
            "LR-M — ICC",
            "LR-1 — benign"
        ],
        "correct": 1,
        "explanation": "LI-RADS yalnızca riskli hastalara uygulanır: siroz, kronik HBV veya önceki HKH. Sirozlu olmayan hastada APHE + washout gösteren lezyon HKH olabilir ama hipervasküler metastaz (NET, RCC, tiroid) da bu paterni gösterir. Biyopsisiz tedavi başlanamaz. PPV çok daha düşük. Bu vaka LI-RADS dışı — klinik bağlam ve biyopsi ile yönetim.",
        "level": 5
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

print("\n── Katman 5 yükleniyor...")
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
print(f"\n✓ Katman 5 tamamlandı — {len(CONCEPTS)} concept, {len(QUESTIONS)} soru")

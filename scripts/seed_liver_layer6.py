from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

CONCEPTS = [

    # ── KATMAN 6: MULTİMODAL KORELASYON VE RAPORLAMA ─────────────────────────

    {
        "id": "multimodal_us_to_ct_mr",
        "name": "US → BT/MR Geçiş Algoritması — Ne Zaman İleri Tetkik?",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "US'de saptanan lezyonun BT veya MR ile değerlendirilmesi için karar algoritması. Her US bulgusu ileri tetkik gerektirmez — doğru seçim gereksiz radyasyon ve maliyeti önler.",
        "why_matters": "US'de 'kitle var' demek yetmez. BT mi MR mı? Ne zaman? Bu kararı doğru vermek hem hasta yönetimi hem kaynak kullanımı açısından kritik.",
        "key_points": [
            "US-3 (pozitif surveyans) → Multifazik BT veya MR — 4-6 hafta içinde",
            "Tipik hemanjiom + normal KC + <3 cm → İleri tetkik gerekmez",
            "Basit kist kriterleri → İleri tetkik gerekmez",
            "İndeterminate solid lezyon → Kontrastlı MR tercih (doku karakterizasyonu üstün)",
            "Onkoloji hastası + yeni lezyon → Hızlı değerlendirme, BT evreleme",
            "Genç kadın + solid lezyon → Gadoxetat MR (FNH/adenom ayırımı)",
            "Siroz + yeni nodül → LI-RADS algoritması, multifazik BT veya MR"
        ],
        "source": "ACR LI-RADS US v2024, EASL 2018, ACG 2024"
    },
    {
        "id": "multimodal_ct_to_mr",
        "name": "BT'den MR'a Geçiş — Hangi Durumda MR Gerekli?",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "BT ile karakterize edilemeyen lezyonlarda MR problem-solving rolü üstlenir. MR'ın BT'ye üstünlükleri ve hangi sorulara cevap verdiği net olmalı.",
        "why_matters": "BT'de LR-3 veya LR-4 lezyon → MR yükseltir mi? BT'de kistik ama atipik lezyon → MR ne söyler? Bu geçiş kararı günlük pratikte çok sık sorulur.",
        "key_points": [
            "BT'de LR-3/4 → MR daha yüksek duyarlılık: HBP + DWI ile upgrade olabilir",
            "BT'de hemanjiom şüpheli → MR T2 ampul bulb konfirmasyonu",
            "BT'de FNH vs adenom ayırımı imkânsız → Gadoxetat MR tanısal",
            "BT'de kistik lezyon + atipik → MR DWI + kontrast solid komponent gösterir",
            "BT'de ICC vs HKH belirsiz → MR DWI + geç faz persistan enhancement",
            "MR kontrendike (pace-maker, klaustrofobi) → CEUS problem-solving",
            "MR sensitivitesi HKH: %61-82 vs BT %48-66 (meta-analiz)"
        ],
        "source": "ESGAR 2024, LI-RADS v2018, EASL 2018, PMC MRI Management 2024"
    },
    {
        "id": "multimodal_ceus_role",
        "name": "CEUS'un Rolü — Problem-Solving ve BT/MR Alternatifi",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "Kontrast madde kontrendikasyonunda veya BT/MR belirsizliğinde CEUS güçlü alternatif. Gerçek zamanlı arteryel faz değerlendirmesi CEUS'un en önemli avantajı.",
        "why_matters": "Böbrek yetmezliği veya gadolinyum allerjisi olan hastada CEUS hayat kurtarır. Ayrıca BT/MR'da indeterminate lezyonların %88'ini çözer.",
        "key_points": [
            "CEUS avantajı: gerçek zamanlı arteryel faz — AV şant artefaktı yok",
            "BT/MR indeterminate lezyonların %88'ini çözer (Salama 2024)",
            "HKH CEUS LI-RADS: APHE + geç hafif washout (>60 sn) = LR-5",
            "ICC: APHE + erken belirgin washout (<60 sn) = LR-M",
            "Bu washout zamanlaması CEUS'a özgü — BT/MR'dan farklı",
            "Hemanjiom: periferik nodüler + progresif dolum, persistan geç faz",
            "Kontrast allerjisi veya böbrek yetmezliği → CEUS ilk tercih"
        ],
        "source": "CEUS LI-RADS 2017, EFSUMB 2020, Salama 2024, AJR CEUS Review"
    },
    {
        "id": "multimodal_reporting_structured",
        "name": "Yapılandırılmış Karaciğer Raporu — Standart Format",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "Karaciğer radyoloji raporunun yapılandırılmış formatı: teknik bilgi → bulgu → lezyon tanımı → yorum → öneri. Standart format iletişimi ve kaliteyi artırır.",
        "why_matters": "İyi rapor yazmak radyolojinin en önemli çıktısı. Yapılandırılmamış rapor klinisyen için işe yaramaz. LI-RADS kategorisi mutlaka belirtilmeli.",
        "key_points": [
            "Teknik: modalite, kontrast tipi/dozu, fazlar, kalite değerlendirmesi",
            "Karaciğer zemini: boyut, kontur, parankim (siroz, steatoz?)",
            "Vasküler yapılar: portal ven, hepatik venler — trombüs?",
            "Safra yolları: dilatasyon? Lokalizasyon?",
            "Fokal lezyon: segment, boyut, morfoloji, enhancement paterni, LI-RADS kategorisi",
            "Öneri: 'MDT değerlendirmesi önerilir' / '3 ayda multifazik MR kontrolü'",
            "LI-RADS raporlama şablonu: ACR web sitesinde ücretsiz"
        ],
        "source": "ACR LI-RADS Reporting Template, ESGAR 2024, RadioGraphics"
    },
    {
        "id": "multimodal_treatment_response",
        "name": "Lokal Tedavi Sonrası Görüntüleme — LI-RADS TRA",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "Ablasyon, TACE, TARE sonrası LI-RADS TRA (Treatment Response Assessment) algoritması kullanılır. Viable tümör tespiti tedavinin yeterliliğini değerlendirir.",
        "why_matters": "Ablasyon sonrası lezyonun 'tedavi edildi mi?' sorusu radyologun cevaplaması gereken en kritik sorulardan biri. LI-RADS TRA v2024 bu değerlendirmeyi standardize eder.",
        "key_points": [
            "LR-TR Nonviable: enhancement yok veya tedaviye özgün enhancement",
            "LR-TR Equivocal: belirsiz — 3 ayda tekrar değerlendirme",
            "LR-TR Viable: nodüler APHE veya washout — canlı tümör",
            "TACE sonrası: lipiodol yoğunluğu ablasyon zonu sınırlarını tanımlar",
            "Ablasyon marjı: minimal 5 mm güvenli sınır önerilir",
            "Erken reaktif enhancement: post-ablasyon 1 ay içinde perilesional — canlı değil",
            "LI-RADS TRA 2024: radyasyon vs non-radyasyon tedavi ayrı algoritmalar"
        ],
        "source": "LI-RADS TRA v2024, Radiology 2024, EASL 2018"
    },
    {
        "id": "multimodal_surveillance_strategy",
        "name": "HKH Surveyans Stratejisi — Kim, Ne Zaman, Nasıl?",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "HKH surveyansı kimlere yapılır, hangi aralıkta, hangi modalite ile? Surveyansın amacı erken HKH tespiti — kürledilebilir evrede yakalamak.",
        "why_matters": "Surveyansı eksik yapmak HKH'yı geç evrede yakalamak demek. Fazla yapmak gereksiz kaygı ve maliyet. Kılavuz bazlı strateji şart.",
        "key_points": [
            "Hedef popülasyon: siroz (her etiyoloji) + kronik HBV (belirli kriterler)",
            "Standart: 6 ayda bir US + AFP — AASLD 2023, EASL 2018",
            "Abbreviated MRI (AMRI): non-kontrast T1 + DWI — US'e alternatif, daha sensitif",
            "US limitasyonu: obezite, gaz, operatör bağımlılık — VIS-C skoru kötü ise AMRI",
            "AFP tek başına yetersiz: %30-40 HKH AFP üretmez",
            "LI-RADS US Surveillance v2024: US-1/2/3 kategorileri",
            "US-3 → 4-6 hafta içinde multifazik BT veya MR"
        ],
        "source": "AASLD 2023, EASL 2018, ACR LI-RADS US v2024, JACR 2025"
    },
    {
        "id": "multimodal_mdt_radiology",
        "name": "MDT'de Radyoloji — Karaciğer Tümör Kurulu",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "Multidisipliner tümör kurulunda radyologun rolü: tanıyı doğrulamak, evreyi bildirmek, tedavi seçeneğini planlamak. Radyolog pasif değil aktif katılımcı.",
        "why_matters": "MDT'de 'LR-5, segment VI, 3 cm' demek yetmez. Vasküler anatomi, cerrahi sınır, ablasyon planlaması, biliyer anatomi — bunları radyolog sunar.",
        "key_points": [
            "Cerrahi rezeksiyon planlaması: segment lokalizasyonu, vasküler ilişki, güvenli sınır",
            "Ablasyon planlaması: lezyon boyutu, lokalizasyon, komşu yapılar",
            "Transplantasyon değerlendirmesi: Milan kriterleri karşılanıyor mu?",
            "TACE için vasküler anatomi: hepatik arter varyasyonları (Michel sınıflaması)",
            "Radyolog preoperatif bildirim: 'Segment VIII lezyonu, sağ hepatik ven komşuluğu'",
            "Evreleme bildirimi: BCLC evre, portal invazyon, ekstrahepatik yayılım",
            "MDT kararı: radyoloji + onkoloji + cerrahi + gastroenteroloji birlikte"
        ],
        "source": "EASL 2018, AASLD 2023, Liver MDT Guidelines"
    },
    {
        "id": "multimodal_liver_mr_sequences_guide",
        "name": "Karaciğer MR Sekans Rehberi — Her Sekans Ne Soruyu Cevaplar?",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "Karaciğer MR'ında her sekansın klinik sorusu vardır. Hangi sekans hangi tanıyı destekler veya ekarte eder? Pratik rehber.",
        "why_matters": "MR raporu yazarken hangi sekansı neden değerlendirdiğini bilmek sistematik okumayı sağlar. 'T2 baktım parlak' değil, 'T2 ampul bulb işareti hemanjiom kriteridir' demek.",
        "key_points": [
            "T1 in/out phase: yağ (kimyasal kayma), kanama (T1 parlak), adenom HNF-1α",
            "T2 FS: hemanjiom (ampul bulb), kist (parlak), HKH (hafif parlak)",
            "DWI + ADC: malignite kısıtlar, kist serbest, apse kısıtlar",
            "Arteryel faz: APHE değerlendirmesi — gadoxetat için yavaş enjeksiyon",
            "Portal venöz faz: washout, metastaz, portal ven değerlendirme",
            "Geç faz: kapsül, ICC persistan enhancement, hemanjiom fill-in",
            "HBP (gadoxetat, 15-20 dk): FNH hiperintens, adenom/HKH hipointens",
            "MRCP: safra yolu anatomisi, Caroli, PSK, safra taşı"
        ],
        "source": "ESGAR Consensus, AJR Gadoxetate, LI-RADS v2018, MRCP Guidelines"
    },
]

# ── ÖNKOŞULLAR ────────────────────────────────────────────────────────────────
PREREQUISITES = [
    {"from": "liver_systematic_reading",      "to": "multimodal_us_to_ct_mr"},
    {"from": "us_physics_liver",              "to": "multimodal_us_to_ct_mr"},
    {"from": "liver_ct_protocol",            "to": "multimodal_us_to_ct_mr"},
    {"from": "concept_lirads",               "to": "multimodal_us_to_ct_mr"},

    {"from": "multimodal_us_to_ct_mr",       "to": "multimodal_ct_to_mr"},
    {"from": "liver_mr_protocol",            "to": "multimodal_ct_to_mr"},
    {"from": "lirads_lr_categories_decision","to": "multimodal_ct_to_mr"},

    {"from": "multimodal_ct_to_mr",          "to": "multimodal_ceus_role"},
    {"from": "liver_contrast_iodinated",     "to": "multimodal_ceus_role"},

    {"from": "liver_systematic_reading",     "to": "multimodal_reporting_structured"},
    {"from": "lirads_lr_categories_decision","to": "multimodal_reporting_structured"},
    {"from": "liver_anatomy_segments",       "to": "multimodal_reporting_structured"},

    {"from": "hcc_bclc_staging",             "to": "multimodal_treatment_response"},
    {"from": "lirads_lr_categories_decision","to": "multimodal_treatment_response"},
    {"from": "liver_ct_protocol",            "to": "multimodal_treatment_response"},

    {"from": "concept_lirads",               "to": "multimodal_surveillance_strategy"},
    {"from": "liver_physiology_function",    "to": "multimodal_surveillance_strategy"},
    {"from": "us_physics_liver",             "to": "multimodal_surveillance_strategy"},

    {"from": "hcc_bclc_staging",             "to": "multimodal_mdt_radiology"},
    {"from": "liver_congenital_vascular",    "to": "multimodal_mdt_radiology"},
    {"from": "multimodal_reporting_structured","to": "multimodal_mdt_radiology"},

    {"from": "liver_mr_protocol",            "to": "multimodal_liver_mr_sequences_guide"},
    {"from": "mr_physics_t1_t2",             "to": "multimodal_liver_mr_sequences_guide"},
    {"from": "concept_dwi",                 "to": "multimodal_liver_mr_sequences_guide"},
    {"from": "concept_hbp",                 "to": "multimodal_liver_mr_sequences_guide"},
]

# ── CONCEPT → DIAGNOSIS ───────────────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "multimodal_us_to_ct_mr",         "diagnosis": "hcc",        "relation": "TECHNIQUE_FOR"},
    {"concept": "multimodal_ct_to_mr",            "diagnosis": "hcc",        "relation": "TECHNIQUE_FOR"},
    {"concept": "multimodal_ct_to_mr",            "diagnosis": "fnh",        "relation": "TECHNIQUE_FOR"},
    {"concept": "multimodal_ceus_role",           "diagnosis": "hcc",        "relation": "TECHNIQUE_FOR"},
    {"concept": "multimodal_treatment_response",  "diagnosis": "hcc",        "relation": "FOLLOW_UP_FOR"},
    {"concept": "multimodal_surveillance_strategy","diagnosis": "hcc",       "relation": "PREVENTION_FOR"},
    {"concept": "multimodal_mdt_radiology",       "diagnosis": "hcc",        "relation": "MANAGEMENT_FOR"},
    {"concept": "multimodal_mdt_radiology",       "diagnosis": "icc",        "relation": "MANAGEMENT_FOR"},
]

# ── SORULAR ───────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_us3_next_step",
        "concept_id": "multimodal_us_to_ct_mr",
        "type": "multiple_choice",
        "question": "Sirozlu hastada 6 aylık US surveyansında yeni 12 mm hipoekoik lezyon saptandı (US-3). Sonraki adım?",
        "options": [
            "6 ay sonra US tekrar",
            "Hemen biyopsi",
            "4-6 hafta içinde multifazik BT veya dinamik kontrastlı MR",
            "AFP bakılması yeterli"
        ],
        "correct": 2,
        "explanation": "US-3 (pozitif) bulgu 4-6 hafta içinde multifazik BT veya dinamik kontrastlı MR ile değerlendirilmelidir. 6 ay beklemek HKH gelişimine fırsat tanır. AFP tek başına yeterli değil — %30-40 HKH AFP üretmez. Biyopsi LR-5 kriterlerini karşılamayan lezyonlarda düşünülebilir ama LI-RADS protokolü önce görüntüleme diyor.",
        "level": 6
    },
    {
        "id": "q_ct_indeterminate_mr",
        "concept_id": "multimodal_ct_to_mr",
        "type": "multiple_choice",
        "question": "BT'de 15 mm, LR-3 lezyon (APHE var, washout yok, kapsül yok). Gadoxetat MR'da APHE var, washout yok, HBP hipointens, DWI kısıtlama var. LI-RADS kategorisi?",
        "options": [
            "LR-3 — değişmedi",
            "LR-4 — DWI kısıtlama + HBP hipointens yardımcı özellik, 1 basamak yükseltir",
            "LR-5 — yardımcı özelliklerle LR-5'e çıkıldı",
            "LR-M — HBP hipointens ICC gösterir"
        ],
        "correct": 1,
        "explanation": "BT'de LR-3 (APHE tek başına, 10-19 mm). MR'da yardımcı özellikler var: DWI kısıtlama + HBP hipointensitesi. Yardımcı özellikler maksimum 1 basamak yükseltir → LR-3'ten LR-4'e. LR-5'e çıkmak için majör özellik gerekli — yardımcı özellikle LR-5 olamaz. Bu hasta 3 ayda MR/BT kontrolü almalıdır.",
        "level": 6
    },
    {
        "id": "q_ceus_washout_timing",
        "concept_id": "multimodal_ceus_role",
        "type": "multiple_choice",
        "question": "CEUS'ta HKH ile ICC arasındaki en önemli ayırıcı bulgu nedir?",
        "options": [
            "Arteryel enhancement olup olmaması",
            "Washout zamanlaması: HKH geç hafif washout (>60 sn), ICC erken belirgin washout (<60 sn)",
            "Lezyon boyutu",
            "Portal fazda sinyal intensitesi"
        ],
        "correct": 1,
        "explanation": "CEUS'ta washout zamanlaması kritik ayırıcı bulgudur. HKH: geç ve hafif washout (>60 saniye sonra) — CEUS LI-RADS LR-5. ICC: erken ve belirgin washout (<60 saniye) — CEUS LI-RADS LR-M. Bu ayrım BT/MR'dan farklıdır çünkü CEUS'ta mikrobalonlar tamamen intravasküler kalır — ekstrasellüler dağılım yok. Bu özellik CEUS'a ICC-HKH ayırımında avantaj sağlar.",
        "level": 6
    },
    {
        "id": "q_report_structure",
        "concept_id": "multimodal_reporting_structured",
        "type": "multiple_choice",
        "question": "Sirozlu hastada 2.5 cm LR-5 lezyon raporlarken mutlaka belirtilmesi gereken bilgiler hangi seçenekte tam verilmiştir?",
        "options": [
            "Sadece 'karaciğerde kitle' yazmak yeterli",
            "Segment, boyut, LI-RADS kategorisi, önerilen aksiyon",
            "Sadece LI-RADS kategorisi",
            "Boyut ve kontrast paterni"
        ],
        "correct": 1,
        "explanation": "Yapılandırılmış raporda fokal lezyon için minimum: (1) Segment lokalizasyonu — cerrahi planlama için, (2) Boyut — evreleme için, (3) LI-RADS kategorisi — standart terminoloji, (4) Önerilen aksiyon — klinisyene yol gösterici. ACR raporlama şablonu bu bilgileri zorunlu kılar. 'Karaciğerde kitle' yetersiz ve klinisyen için işlevsiz.",
        "level": 6
    },
    {
        "id": "q_ablation_response",
        "concept_id": "multimodal_treatment_response",
        "type": "multiple_choice",
        "question": "RFA ablasyonu sonrası 1. ay BT'de ablasyon zonunda perilesional ince rim enhancement var, nodüler enhancement yok. LI-RADS TRA kategorisi?",
        "options": [
            "LR-TR Viable — aktif tümör, retreatment gerekli",
            "LR-TR Equivocal — belirsiz, 3 ayda tekrar",
            "LR-TR Nonviable — perilesional ince rim reaktif, nodüler enhancement yok",
            "LR-TR Nonevaluable — değerlendirilemez"
        ],
        "correct": 2,
        "explanation": "Post-ablasyon erken dönemde (özellikle ilk 3 ay) perilesional ince düzgün rim enhancement — reaktif hiperemi/inflamasyon. Bu LR-TR Nonviable kriteridir. Nodüler, kalın veya irregular enhancement olsaydı LR-TR Viable düşünülürdü. LI-RADS TRA 2024: non-radyasyon tedaviler için kriterler revize edildi, erken reaktif değişiklikler daha net tanımlandı.",
        "level": 6
    },
    {
        "id": "q_surveillance_interval",
        "concept_id": "multimodal_surveillance_strategy",
        "type": "multiple_choice",
        "question": "Child-Pugh B sirotik hasta, HKH öyküsü yok. Hangi surveyans protokolü önerilir?",
        "options": [
            "Yıllık US",
            "6 ayda bir US ± AFP",
            "3 ayda bir multifazik BT",
            "Surveyans gerekmez"
        ],
        "correct": 1,
        "explanation": "AASLD 2023 ve EASL 2018: siroz hastalarında 6 ayda bir US ± AFP standart surveyans. Child-Pugh skoru değil, siroz varlığı belirleyicidir. Yıllık US yetersiz — HKH 6 ayda önemli büyüyebilir. 3 ayda BT — gereksiz radyasyon. US VIS-C (ciddi görüntüleme kısıtlılığı) varsa abbreviated MRI alternatif. AFP tek başına surveyans olarak kullanılamaz.",
        "level": 6
    },
    {
        "id": "q_mdt_radiology_role",
        "concept_id": "multimodal_mdt_radiology",
        "type": "multiple_choice",
        "question": "MDT'de radyologun sunumu sırasında cerrahi ekip için en kritik bilgi hangisidir?",
        "options": [
            "Lezyonun LI-RADS kategorisi",
            "AFP değeri",
            "Segment lokalizasyonu, vasküler komşuluk ve güvenli cerrahi sınır bilgisi",
            "Hastanın Child-Pugh skoru"
        ],
        "correct": 2,
        "explanation": "Cerrah için kritik bilgi: (1) Segment — hangi lob rezeke edilecek, (2) Vasküler komşuluk — hepatik ven, portal ven dallarına mesafe, (3) Güvenli sınır — minimal 1 cm R0 rezeksiyon için, (4) Hepatik arter anatomisi — Michel sınıflamasına göre varyant var mı? Bu bilgiler olmadan cerrah operasyonu planlayamaz. AFP ve Child-Pugh klinisyen sunumudur.",
        "level": 6
    },
    {
        "id": "q_mr_sequence_purpose",
        "concept_id": "multimodal_liver_mr_sequences_guide",
        "type": "multiple_choice",
        "question": "Karaciğer MR'ında adenom HNF-1α subtipini tanımlamak için hangi sekans kritiktir?",
        "options": [
            "T2 FS — yağ içeriği gösterir",
            "T1 kimyasal kayma in/out phase — yağ sinyal düşümü",
            "DWI — hücresellik",
            "HBP — hepatosit fonksiyonu"
        ],
        "correct": 1,
        "explanation": "Adenom HNF-1α subtipi: steatoz dominant → T1 kimyasal kayma out-phase'de belirgin sinyal düşümü. Bu, yağ ve suyun farklı frekanslarda rezonans göstermesi prensibine dayanır. Out-phase'de yağ + su protonları faz dışı → sinyal düşer. HBP hipointens tüm adenom subtipleri için geçerlidir (FNH ayırımı). DWI malignite şüphesinde kullanılır.",
        "level": 6
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

print("\n── Katman 6 yükleniyor...")
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
print(f"\n✓ Katman 6 tamamlandı — {len(CONCEPTS)} concept, {len(QUESTIONS)} soru")

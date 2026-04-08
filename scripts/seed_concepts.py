from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

# ── CONCEPT DÜĞÜMLERİ ────────────────────────────────────────────────────────
# Her concept: id, name, organ, level (1=temel, 2=orta, 3=ileri),
#              category (anatomy/physiology/modality/pathology/technique)

CONCEPTS = [

    # ── SEVİYE 1: TEMEL ──────────────────────────────────────────────────────

    # Anatomi
    {
        "id": "liver_anatomy_segments",
        "name": "Karaciğer Segmentasyonu (Couinaud)",
        "organ": "liver",
        "level": 1,
        "category": "anatomy",
        "summary": "Karaciğer 8 segmente ayrılır. Her segment bağımsız vasküler ve biliyer yapıya sahiptir. Couinaud sınıflaması cerrahi ve radyolojik raporlama için standarttır.",
        "why_matters": "Lezyon lokalizasyonunu doğru raporlamak için segment bilmek zorunludur. 'Sağ lob' demek yeterli değil — segment VI mi, segment VII mi?",
        "key_points": [
            "Segment I (kaudat lob) — portal ve hepatik venden bağımsız",
            "Segment II-IV sol lob, Segment V-VIII sağ lob",
            "Segment IV — kare lob, safra kesesinin solunda",
            "Orta hepatik ven sağ-sol lobu ayırır"
        ],
        "source": "Couinaud 1957, RSNA Anatomy"
    },
    {
        "id": "liver_anatomy_vasculature",
        "name": "Karaciğer Vasküler Anatomisi",
        "organ": "liver",
        "level": 1,
        "category": "anatomy",
        "summary": "Karaciğer çift kanlanır: portal ven (%70-75) ve hepatik arter (%25-30). Hepatik venler IVC'ye drene olur.",
        "why_matters": "Kontrast dinamiğini anlamak için çift kanlanmayı bilmek şart. HKH arterden beslenir — bu yüzden arteryel fazda parlıyor.",
        "key_points": [
            "Portal ven: splenik + superior mezenterik venden oluşur",
            "Hepatik arter: çölyak trunkustan gelir",
            "HKH: arteryel kanlanma dominant — arteryel fazda parlak",
            "Metastaz: portal kanlanma dominant — portal fazda en belirgin"
        ],
        "source": "Gray's Anatomy, Radiology Key"
    },
    {
        "id": "liver_physiology_function",
        "name": "Karaciğer Fonksiyonu ve Hastalık Zemini",
        "organ": "liver",
        "level": 1,
        "category": "physiology",
        "summary": "Karaciğer metabolizma, detoksifikasyon, protein sentezi ve safra üretimi yapar. Siroz, kronik hasara bağlı fibrozis ve nodüler rejenerasyon ile sonuçlanır.",
        "why_matters": "Siroz zemini HKH riskini dramatik artırır. Zemini bilmeden lezyon yorumlamak tehlikelidir.",
        "key_points": [
            "Child-Pugh skoru karaciğer rezervini ölçer",
            "AFP: HKH tarama ve takip markeri",
            "Siroz: nodüler kontur + heterojen parankim + splenomegali",
            "Portal hipertansiyon: asit, özofageal varis, splenomegali"
        ],
        "source": "EASL 2018, AASLD 2023"
    },

    # ── SEVİYE 1: MODALİTE TEMELLERİ ─────────────────────────────────────────

    {
        "id": "us_principles",
        "name": "Ultrasonografi Prensipleri",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "US ses dalgalarının doku yansımasını görüntüler. Ekojenite dokudan dokuya değişir. Gerçek zamanlı, radyasyon yok, operatöre bağımlı.",
        "why_matters": "Karaciğer taramasında ilk basamak. Kist ve hemanjiom tanısında çoğu zaman yeterli.",
        "key_points": [
            "Hipereko: yoğun yapı (yağ, fibrozis, kalsifikasyon)",
            "Hipoekoik: su içeriği fazla veya heterojen",
            "Posterior akustik güçlenme: kistik lezyon işareti",
            "Arka gölge: kalsifikasyon veya taş işareti"
        ],
        "source": "EFSUMB Guidelines 2020"
    },
    {
        "id": "ct_principles",
        "name": "BT Faz Mantığı ve Kontrast Dinamiği",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "İV kontrast karaciğerden arteryel → portal → geç faz sırasıyla geçer. Her faz farklı bilgi verir. Zamanlama kritiktir.",
        "why_matters": "Kontrast fazlarını bilmeden karaciğer lezyonu yorumlanamaz. APHE arteryel fazda değerlendirilir, washout portal/geç fazda.",
        "key_points": [
            "Arteryel faz: 25-35 sn — hipervasküler lezyonlar parlak",
            "Portal venöz faz: 60-70 sn — karaciğer parankimi maksimum",
            "Geç/denge fazı: 3-5 dk — washout burada belirginleşir",
            "Natif (kontrastsız): spontan hiperdensite, kalsifikasyon"
        ],
        "source": "ACR 2023, LI-RADS v2018"
    },
    {
        "id": "mr_principles",
        "name": "MR Sekans Mantığı — Karaciğer",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "MR farklı sekanslar ile doku karakterizasyonu yapar. T1, T2, DWI, kontrast serileri ve hepatobiliyer faz birlikte değerlendirilir.",
        "why_matters": "MR karaciğer lezyonlarında BT'den daha yüksek sensitivite sağlar (%61-82 vs %48-66). Doku karakterizasyonu üstün.",
        "key_points": [
            "T1: yağ ve protein içeriği (hiperintens = yağ/kanama)",
            "T2: su içeriği (parlak = sıvı/hemanjiom/kist)",
            "DWI: hücre yoğunluğu — malign lezyon kısıtlar",
            "Gadoxetat (Primovist): hepatobiliyer faz = hepatosit fonksiyonu"
        ],
        "source": "ESGAR 2024, LI-RADS v2018"
    },

    # ── SEVİYE 2: BULGULAR VE MEKANİZMALAR ───────────────────────────────────

    {
        "id": "concept_aphe",
        "name": "APHE — Arteryel Faz Hiperenhancement",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Arteryel fazda lezyonun çevre parankimden belirgin parlak görünmesi. HKH'nın en önemli majör özelliği.",
        "why_matters": "APHE + washout kombinasyonu LR-5 (kesin HKH) kriteridir. Anlamamak yanlış yoruma yol açar.",
        "key_points": [
            "Non-rim APHE: HKH için tipik (arteryel neovaskülarizasyon)",
            "Rim APHE: LR-M — HKH dışı malignite (ICC, metastaz)",
            "Flash fill: hemanjiomda tüm lezyon eşanlı dolar",
            "APHE olmadan LR-5 kurulamaz"
        ],
        "source": "LI-RADS v2018 Major Features"
    },
    {
        "id": "concept_washout",
        "name": "Washout — Portal/Geç Faz Kontrast Kaybı",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Portal veya geç fazda lezyonun çevre parankimden koyu görünmesi. HKH'da arteryel kanlanma baskın olduğu için portal fazda kontrast hızlı kaybolur.",
        "why_matters": "APHE ile birlikte LR-5 kriteridir. Yanlış pozitif olabilir — rim tarzı washout LR-M'dir.",
        "key_points": [
            "Non-periferik washout: HKH için majör özellik",
            "Periferik washout: ICC ve metastaz — LR-M kriteri",
            "Washout ≠ hipointens olma — çevre parankimden göreceli koyu",
            "Hemanjiomda washout OLMAZ — fill-in devam eder"
        ],
        "source": "LI-RADS v2018, Chernyak 2018"
    },
    {
        "id": "concept_dwi",
        "name": "DWI — Difüzyon Ağırlıklı Görüntüleme",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Su moleküllerinin hareketi ölçülür. Malign lezyonlar yüksek hücre yoğunluğu nedeniyle difüzyonu kısıtlar.",
        "why_matters": "LI-RADS 2024'te viable tümör için ek özellik olarak eklendi. ICC'de belirgin kısıtlama görülür.",
        "key_points": [
            "Kısıtlama: DWI parlak + ADC koyu = gerçek kısıtlama",
            "T2 shine-through: DWI parlak ama ADC de parlak = sahte kısıtlama",
            "Kist: serbest difüzyon — ADC çok yüksek",
            "Apse: merkez kısıtlama — pü yüksek viskozite"
        ],
        "source": "LI-RADS 2024, ESGAR 2024"
    },
    {
        "id": "concept_hbp",
        "name": "Hepatobiliyer Faz (HBP) — Gadoxetat MR",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Gadoxetat (Primovist) hepatositler tarafından alınır. 20 dakikada hepatobiliyer faza girer. Hepatosit içeren lezyonlar hiperintens, içermeyenler hipointens görünür.",
        "why_matters": "FNH ve adenom ayırımında tanısaldır. FNH hiperintens, adenom hipointens — bu tek bulgu tanıyı değiştirebilir.",
        "key_points": [
            "FNH: HBP hiperintens veya izointens (hepatosit var)",
            "Adenom: HBP hipointens (hepatosit fonksiyonu bozuk)",
            "HKH: genellikle hipointens",
            "Gadoxetat 2024 güncellemesinde HBP hipointensitesi ek AF"
        ],
        "source": "EASL 2016, LI-RADS 2024"
    },
    {
        "id": "concept_lirads",
        "name": "LI-RADS Sistemi — Genel Çerçeve",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "ACR tarafından geliştirilen, riskli hastalarda HKH tanısını standardize eden sistem. LR-1'den LR-5'e kadar kategoriler HKH olasılığını ifade eder.",
        "why_matters": "Radyoloji raporlamasında global standart. LI-RADS bilmeden HKH raporu yazmak yetersiz kalır.",
        "key_points": [
            "Sadece riskli hastalara uygulanır (siroz, kronik HBV, önceki HKH)",
            "LR-1: kesinlikle benign. LR-5: kesin HKH (>%95)",
            "LR-M: HKH dışı malignite şüphesi",
            "v2018 → v2024: TRA algoritması güncellendi, DWI eklendi"
        ],
        "source": "ACR LI-RADS v2018, Kierans 2025"
    },

    # ── SEVİYE 3: TANI SPESİFİK ──────────────────────────────────────────────

    {
        "id": "concept_hcc_pathophysiology",
        "name": "HKH Patofiziyolojisi — Neden Bu Bulgular?",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "HKH gelişiminde portal kanlanma azalır, arteryel neovaskülarizasyon artar. Bu değişim APHE + washout paternini açıklar.",
        "why_matters": "Bulguların mekanizmasını anlarsan asla unutmazsın. APHE'nin neden olduğunu bilen rezidan LI-RADS'ı ezberlemez, anlar.",
        "key_points": [
            "Normal hepatosit: %70 portal, %30 arteryel kanlanır",
            "HKH: %80-100 arteryel kanlanır (neovaskülarizasyon)",
            "Arteryel fazda parlak çünkü kontrast arteryel yoldan hızlı giriyor",
            "Portal fazda koyu çünkü portal kanlanma yok, kontrast hızlı çıkıyor"
        ],
        "source": "Llovet 2021 Nature Reviews, AASLD 2023"
    },
    {
        "id": "concept_hemangioma_pathophysiology",
        "name": "Hemanjiom — Neden T2'de Parlak, Neden Fill-in?",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Hemanjiom yavaş akan kan dolu vasküler kanallardan oluşur. T2'de parlak çünkü serbest su; periferik nodüler → fill-in çünkü kontrast dıştan içe yavaş dolar.",
        "why_matters": "Hemanjiom en sık benign karaciğer lezyonu. Tanı kriterleri bilinmeden gereksiz biyopsi yapılır.",
        "key_points": [
            "T2 ampul bulb işareti: serbest akan kan → çok parlak",
            "Periferik nodüler enhancement: büyük damar periferde",
            "Fill-in: kontrast dıştan içe ilerler, geç fazda dolar",
            "Flash fill hemanjiom: küçük, tüm faz eşanlı dolar"
        ],
        "source": "EASL 2016, ACG 2024"
    },
    {
        "id": "concept_fnh_vs_adenoma",
        "name": "FNH vs Adenom — Ayırım Nasıl Yapılır?",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "Her ikisi de genç kadında görülen benign solid lezyonlar. FNH: konjenital vasküler anomali. Adenom: hepatosit proliferasyonu, hormon ilişkili.",
        "why_matters": "Adenom kanama riski taşır, ≥5cm ise cerrahi gerekebilir. FNH takip gerektirmez. Ayırım tedaviyi değiştirir.",
        "key_points": [
            "FNH: HBP hiperintens, santral skar, washout yok",
            "Adenom HNF-1α: kimyasal kayma sinyal düşümü (yağ)",
            "Adenom inflamatuar: T2 parlak, sinüzoidal genişleme",
            "Adenom β-katenin: malignite riski — biyopsi gerekli"
        ],
        "source": "EASL 2016, ACG 2024"
    },
    {
        "id": "concept_icc_vs_hcc",
        "name": "ICC vs HKH — En Kritik Ayırım",
        "organ": "liver",
        "level": 3,
        "category": "pathology",
        "summary": "ICC (intrahepatik kolanjioselüler karsinom) ve HKH birbirinden tamamen farklı tedavi alır. LR-M bulgular ICC'yi düşündürür.",
        "why_matters": "HKH → rezeksiyon/ablasyon/transplant. ICC → sadece rezeksiyon. Yanlış tanı yanlış tedavi demek.",
        "key_points": [
            "ICC: rim APHE + periferik washout + kapsüler retraksiyon",
            "HKH: non-rim APHE + non-periferik washout + enhancing kapsül",
            "ICC: geç faz persistan enhancement (fibröz stroma)",
            "CA 19-9 yüksek ICC'yi destekler, AFP HKH'yı"
        ],
        "source": "LI-RADS v2018 LR-M, EASL 2022"
    },
]

# ── ÖNKOŞUL İLİŞKİLERİ ───────────────────────────────────────────────────────
# (from_concept)-[:PREREQUISITE_OF]->(to_concept)
# Yani: from'u bilmeden to'yu öğrenme

PREREQUISITES = [
    # Anatomi önce
    {"from": "liver_anatomy_segments",    "to": "liver_anatomy_vasculature"},
    {"from": "liver_anatomy_vasculature", "to": "liver_physiology_function"},

    # Modalite temeli
    {"from": "liver_anatomy_vasculature", "to": "ct_principles"},
    {"from": "liver_anatomy_vasculature", "to": "us_principles"},
    {"from": "ct_principles",             "to": "mr_principles"},

    # Bulgular için modalite temeli lazım
    {"from": "ct_principles",             "to": "concept_aphe"},
    {"from": "ct_principles",             "to": "concept_washout"},
    {"from": "mr_principles",             "to": "concept_dwi"},
    {"from": "mr_principles",             "to": "concept_hbp"},

    # LI-RADS için bulgular lazım
    {"from": "concept_aphe",              "to": "concept_lirads"},
    {"from": "concept_washout",           "to": "concept_lirads"},
    {"from": "liver_physiology_function", "to": "concept_lirads"},

    # Patofiziyoloji için temel lazım
    {"from": "liver_anatomy_vasculature", "to": "concept_hcc_pathophysiology"},
    {"from": "concept_aphe",              "to": "concept_hcc_pathophysiology"},
    {"from": "concept_washout",           "to": "concept_hcc_pathophysiology"},

    {"from": "mr_principles",             "to": "concept_hemangioma_pathophysiology"},
    {"from": "ct_principles",             "to": "concept_hemangioma_pathophysiology"},

    {"from": "concept_hbp",               "to": "concept_fnh_vs_adenoma"},
    {"from": "mr_principles",             "to": "concept_fnh_vs_adenoma"},

    {"from": "concept_lirads",            "to": "concept_icc_vs_hcc"},
    {"from": "concept_aphe",              "to": "concept_icc_vs_hcc"},
    {"from": "concept_washout",           "to": "concept_icc_vs_hcc"},
]

# ── Concept → Diagnosis ilişkileri ────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "concept_lirads",              "diagnosis": "hcc",        "relation": "EXPLAINS"},
    {"concept": "concept_hcc_pathophysiology", "diagnosis": "hcc",        "relation": "EXPLAINS"},
    {"concept": "concept_aphe",                "diagnosis": "hcc",        "relation": "KEY_FINDING_FOR"},
    {"concept": "concept_washout",             "diagnosis": "hcc",        "relation": "KEY_FINDING_FOR"},
    {"concept": "concept_hbp",                 "diagnosis": "fnh",        "relation": "KEY_FINDING_FOR"},
    {"concept": "concept_hbp",                 "diagnosis": "hca",        "relation": "KEY_FINDING_FOR"},
    {"concept": "concept_fnh_vs_adenoma",      "diagnosis": "fnh",        "relation": "EXPLAINS"},
    {"concept": "concept_fnh_vs_adenoma",      "diagnosis": "hca",        "relation": "EXPLAINS"},
    {"concept": "concept_icc_vs_hcc",          "diagnosis": "icc",        "relation": "EXPLAINS"},
    {"concept": "concept_icc_vs_hcc",          "diagnosis": "hcc",        "relation": "EXPLAINS"},
    {"concept": "concept_dwi",                 "diagnosis": "icc",        "relation": "KEY_FINDING_FOR"},
    {"concept": "concept_hemangioma_pathophysiology", "diagnosis": "hemangioma", "relation": "EXPLAINS"},
]

# ── SM-2 TEST SORULARI ────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_aphe_definition",
        "concept_id": "concept_aphe",
        "type": "multiple_choice",
        "question": "Arteryel faz hiperenhancement (APHE) hangi zaman diliminde değerlendirilir?",
        "options": ["10-15. saniye", "25-35. saniye", "60-70. saniye", "3-5. dakika"],
        "correct": 1,
        "explanation": "Arteryel faz IV kontrast sonrası 25-35. saniyede görüntülenir. Bu fazda hipervasküler lezyonlar (HKH, FNH, adenom) çevre parankimden belirgin parlak görünür.",
        "level": 2
    },
    {
        "id": "q_washout_meaning",
        "concept_id": "concept_washout",
        "type": "multiple_choice",
        "question": "HKH'da washout neden görülür?",
        "options": [
            "Tümör nekrozu nedeniyle kontrast tutulmaz",
            "Portal kanlanma dominant olduğu için portal fazda kontrast birikir",
            "Arteryel kanlanma dominant olduğu için portal fazda kontrast hızlı çıkar",
            "Fibröz kapsül kontrast geçişini engeller"
        ],
        "correct": 2,
        "explanation": "HKH %80-100 arteryel kanlanır. Portal fazda portal ven katkısı olmadığı için kontrast hızlı uzaklaşır — çevre karaciğer parankimi portal venden kontrast almaya devam ederken tümör koyu kalır.",
        "level": 2
    },
    {
        "id": "q_lirads_application",
        "concept_id": "concept_lirads",
        "type": "multiple_choice",
        "question": "LI-RADS sistemi hangi hasta grubuna uygulanır?",
        "options": [
            "Tüm karaciğer lezyonu olan hastalar",
            "Sadece siroz hastalar",
            "Siroz, kronik HBV veya önceki HKH tanısı olan hastalar",
            "AFP yüksekliği olan tüm hastalar"
        ],
        "correct": 2,
        "explanation": "LI-RADS yalnızca HKH riski taşıyan hastalara uygulanır: siroz (herhangi etiyoloji), kronik HBV (siroz olmasa bile belirli kriterler), önceki HKH tanısı. Düşük riskli hastada LR-5 bile yanlış pozitif olabilir.",
        "level": 2
    },
    {
        "id": "q_hbp_fnh_vs_adenoma",
        "concept_id": "concept_hbp",
        "type": "multiple_choice",
        "question": "Gadoxetat MR hepatobiliyer fazda FNH nasıl görünür?",
        "options": [
            "Belirgin hipointens — hepatosit yoktur",
            "Hiperintens veya izointens — fonksiyonel hepatosit içerir",
            "Periferik rim enhancement gösterir",
            "Değişken sinyal — tanısal değeri yoktur"
        ],
        "correct": 1,
        "explanation": "FNH normal hepatositlerden oluşur. Gadoxetat hepatositler tarafından alındığı için FNH HBP'de hiperintens veya izointens görünür. Adenom ise bozuk hepatosit fonksiyonu nedeniyle hipointens kalır — bu ayırım tanısaldır.",
        "level": 3
    },
    {
        "id": "q_t2_hemangioma",
        "concept_id": "concept_hemangioma_pathophysiology",
        "type": "multiple_choice",
        "question": "Hemanjiomda T2'de neden belirgin parlak sinyal (ampul bulb işareti) görülür?",
        "options": [
            "Tümör hücreleri T2'de her zaman parlaktır",
            "Yavaş akan kanın yüksek su içeriği serbest proton hareketi sağlar",
            "Fibröz stroma T2 sinyalini artırır",
            "Arteryel kanlanma T2 sinyalini etkiler"
        ],
        "correct": 1,
        "explanation": "Hemanjiom yavaş akan kanla dolu vasküler kanallardan oluşur. Serbest su molekülleri T2 relaksasyonunu uzatır — bu yüzden beyin omurilik sıvısı kadar parlak görünür. Bu 'ampul bulb işareti' olarak adlandırılır.",
        "level": 3
    },
    {
        "id": "q_icc_vs_hcc_key",
        "concept_id": "concept_icc_vs_hcc",
        "type": "multiple_choice",
        "question": "Rim tarzı APHE görülen bir lezyonda önce hangi tanı düşünülmelidir?",
        "options": [
            "HKH — rim APHE LR-5 kriteridir",
            "Hemanjiom — periferik dolum tipiktir",
            "HKH dışı malignite (ICC/metastaz) — LR-M kriteridir",
            "FNH — arteryel enhancement tipiktir"
        ],
        "correct": 2,
        "explanation": "Rim APHE LI-RADS v2018'de LR-M kriteridir. HKH için NON-rim APHE gereklidir. Rim APHE + periferik washout kombinasyonu ICC veya metastatik lezyonu düşündürür. Bu ayrımı yapmak tedavi planını tamamen değiştirir.",
        "level": 3
    },
    {
        "id": "q_ct_phases",
        "concept_id": "ct_principles",
        "type": "multiple_choice",
        "question": "Multifazik karaciğer BT'de portal venöz faz ne zaman görüntülenir?",
        "options": ["10-20. saniye", "25-35. saniye", "60-70. saniye", "5-10. dakika"],
        "correct": 2,
        "explanation": "Portal venöz faz 60-70. saniyede görüntülenir. Bu fazda karaciğer parankimi maksimum kontrast tutumundadır. Hipovasküler lezyonlar (metastaz, kist) bu fazda en belirgin görünür. Washout da bu fazda değerlendirilir.",
        "level": 1
    },
    {
        "id": "q_dwi_true_restriction",
        "concept_id": "concept_dwi",
        "type": "multiple_choice",
        "question": "Gerçek difüzyon kısıtlaması nasıl tanınır?",
        "options": [
            "DWI'da parlak sinyal yeterlidir",
            "ADC haritasında parlak sinyal",
            "DWI'da parlak + ADC haritasında koyu sinyal",
            "DWI'da koyu + ADC haritasında parlak sinyal"
        ],
        "correct": 2,
        "explanation": "Gerçek kısıtlama: DWI parlak + ADC koyu. Eğer DWI parlak ama ADC de parlaksa bu 'T2 shine-through' artefaktıdır — gerçek kısıtlama değildir. Bu ayrımı yapmak malign-benign ayırımında kritiktir.",
        "level": 2
    },
]


# ── SEED FONKSİYONLARI ────────────────────────────────────────────────────────

def seed_concepts(tx):
    for c in CONCEPTS:
        tx.run("""
            MERGE (c:Concept {id: $id})
            SET c.name = $name,
                c.organ = $organ,
                c.level = $level,
                c.category = $category,
                c.summary = $summary,
                c.why_matters = $why_matters,
                c.key_points = $key_points,
                c.source = $source
        """, **{k: v for k, v in c.items()})
    return len(CONCEPTS)


def seed_prerequisites(tx):
    for p in PREREQUISITES:
        tx.run("""
            MATCH (c1:Concept {id: $from_id})
            MATCH (c2:Concept {id: $to_id})
            MERGE (c1)-[:PREREQUISITE_OF]->(c2)
        """, from_id=p["from"], to_id=p["to"])
    return len(PREREQUISITES)


def seed_concept_diagnosis(tx):
    for cd in CONCEPT_DIAGNOSIS:
        tx.run("""
            MATCH (c:Concept {id: $concept_id})
            MATCH (d:Diagnosis {id: $diagnosis_id})
            MERGE (c)-[:RELATES_TO {relation: $relation}]->(d)
        """, concept_id=cd["concept"], diagnosis_id=cd["diagnosis"], relation=cd["relation"])
    return len(CONCEPT_DIAGNOSIS)


def seed_questions(tx):
    for q in QUESTIONS:
        tx.run("""
            MERGE (q:Question {id: $id})
            SET q.concept_id = $concept_id,
                q.type = $type,
                q.question = $question,
                q.options = $options,
                q.correct = $correct,
                q.explanation = $explanation,
                q.level = $level
        """, **q)

        # Question → Concept ilişkisi
        tx.run("""
            MATCH (q:Question {id: $q_id})
            MATCH (c:Concept {id: $c_id})
            MERGE (q)-[:TESTS]->(c)
        """, q_id=q["id"], c_id=q["concept_id"])
    return len(QUESTIONS)


# ── ÇALIŞTIR ──────────────────────────────────────────────────────────────────

print("\n── Concept düğümleri yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_concepts)
    print(f"✓ {n} Concept düğümü")

print("── Önkoşul ilişkileri yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_prerequisites)
    print(f"✓ {n} PREREQUISITE_OF ilişkisi")

print("── Concept → Diagnosis ilişkileri yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_concept_diagnosis)
    print(f"✓ {n} RELATES_TO ilişkisi")

print("── Sorular yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_questions)
    print(f"✓ {n} Question düğümü")

driver.close()

print(f"""
✓ Eğitim grafı başarıyla oluşturuldu.
  Concepts   : {len(CONCEPTS)}
  Önkoşullar : {len(PREREQUISITES)}
  Sorular    : {len(QUESTIONS)}
""")

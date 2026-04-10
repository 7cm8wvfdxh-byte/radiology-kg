from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

# ── KATMAN 1 & 2 — DERİN İÇERİK ──────────────────────────────────────────────

CONCEPTS = [

    # ── KATMAN 1: TEMEL BİLİM ─────────────────────────────────────────────────

    {
        "id": "liver_histology_lobule",
        "name": "Karaciğer Lobülü ve Portal Triad",
        "organ": "liver",
        "level": 1,
        "category": "anatomy",
        "summary": "Karaciğer lobülü hekzagonal yapıda, merkezinde santral ven, köşelerinde portal triadlar bulunur. Portal triad: hepatik arter dalı + portal ven dalı + safra kanalı dalı. Hepatositler santral venden radyal dizilir.",
        "why_matters": "Lobül mimarisini bilmeden kontrastın karaciğerde nasıl davrandığını anlayamazsın. Portal triaddan santral vene akan kan, kontrast dinamiğinin temelidir.",
        "key_points": [
            "Portal triad: hepatik arter + portal ven + safra kanalı — 3'ü birlikte",
            "Kan akışı: portal triad → sinüzoidler → santral ven → hepatik venler → IVC",
            "Safra akışı ters yönde: hepatositler → safra kanalikülü → portal triad",
            "Kupffer hücreleri sinüzoid duvarında — bakterileri ve artıkları filtreler",
            "Disse aralığı: hepatosit ile sinüzoid endoteli arasında — lenfatik sıvı",
            "İto hücreleri (stellat): A vitamini depolar, fibroziste aktive olur"
        ],
        "source": "AASLD Normal Liver Histology 101, Kenhub 2023, Osmosis"
    },
    {
        "id": "liver_histology_hepatocyte",
        "name": "Hepatosit — Yapı ve Fonksiyon",
        "organ": "liver",
        "level": 1,
        "category": "physiology",
        "summary": "Hepatositler poligonal, büyük hücreler — karaciğerin temel fonksiyonel birimi. Metabolizma, detoksifikasyon, protein sentezi, safra üretimi ve depolama görevleri yapar.",
        "why_matters": "Hepatositin gadoxetat (Primovist) alabilmesi için fonksiyonel olması gerekir. HBP fazında hiperens = fonksiyonel hepatosit. Bunu anlamamak FNH-adenom ayırımını imkânsız kılar.",
        "key_points": [
            "Günde ~900 mL safra üretir",
            "Glikoz → glikojen depolama ve gerektiğinde glikoneogenez",
            "Albumin, koagülasyon faktörleri, fibrinojen sentezi",
            "Amonyak → üre dönüşümü (detoksifikasyon)",
            "Gadoxetat (Gd-EOB-DTPA) OATP1B1/1B3 taşıyıcılarıyla hepatosit içine alınır",
            "HKH ve adenom: taşıyıcı ekspresyonu bozuk → HBP hipointens"
        ],
        "source": "AASLD 2023, Kenhub, PMC Liver-specific MR contrast agents"
    },
    {
        "id": "liver_contrast_iodinated",
        "name": "İyotlu Kontrast Madde — BT Farmakolojisi",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "İyotlu kontrast madde IV verilince hızla damar içine dağılır, ardından interstisyuma geçer, böbreklerden değişmeden atılır. Yarı ömrü 90-120 dakika. Karaciğer BT fazlarının zamanlaması bu kinetiğe göre ayarlanır.",
        "why_matters": "Kontrast zamanlamasını anlamadan neden arteryel fazda 25-35. saniye görüntü aldığımızı veya neden bazı lezyonların erken, bazılarının geç dolduğunu açıklayamazsın.",
        "key_points": [
            "Dağılım: yüksek perfüzyon organlarına (KC, böbrek, beyin) hızlı — 2-5 dk",
            "Eliminasyon: glomerüler filtrasyon ile, tübüler reabsorpsiyon yok",
            "Yarı ömür: 90-120 dk normal böbrek fonksiyonunda",
            "Arteryel faz (25-35 sn): aort + hepatik arter kontrast dolu",
            "Portal venöz faz (60-70 sn): portal ven + karaciğer parankimi maksimum",
            "Geç faz (3-5 dk): interstisyuma geçmiş kontrast — washout burada belirgin",
            "İyot konsantrasyonu ve enjeksiyon hızı enhancement kalitesini belirler"
        ],
        "source": "StatPearls Intravenous Contrast, Radiology RSNA Bae 2010, Mayo Clin Proc 2012"
    },
    {
        "id": "liver_contrast_gadolinium",
        "name": "Gadolinyum Kontrast Madde — MR Farmakolojisi",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "İki tip gadolinyum kontrast var: ekstraselüler (genel amaçlı) ve hepatobiliyer (gadoxetat/Primovist). Gadoxetat %50 hepatositler tarafından alınır, %50 böbrekten atılır — hepatobiliyer faz sağlar.",
        "why_matters": "Primovist ile MR çekildiğinde HBP (20. dk) fazı eklenir. Bu faz FNH-adenom-HKH ayırımında tanısal. Hangi kontrast kullanıldığını bilmeden MR raporunu yorumlayamazsın.",
        "key_points": [
            "Ekstraselüler (Magnevist, Dotarem): böbrekten atılır, HBP vermez",
            "Gadoxetat (Primovist/Eovist): %50 hepatosit alımı → HBP 15-20 dk",
            "Gadoxetat enjeksiyon hızı yavaş tutulur (1 mL/s) — arteryel faz artefaktı azalır",
            "HBP hiperintens: FNH (OATP1B3 eksprese eder)",
            "HBP hipointens: adenom, HKH, ICC, metastaz",
            "Gadoxetat ile T1 arteryel faz kalitesi ekstraselüler ajana göre daha düşük olabilir"
        ],
        "source": "PMC Liver-specific MR contrast agents 2013, ESGAR 2024, LI-RADS 2024"
    },
    {
        "id": "mr_physics_t1_t2",
        "name": "MR Fizik Temelleri — T1 ve T2 Relaksasyon",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "T1: protonların longitudinal (z eksenine) dönüş süresi. T2: protonların transversal faz uyumunu kaybetme süresi. Serbest su uzun T1, çok uzun T2 gösterir. Yağ kısa T1 gösterir.",
        "why_matters": "T2'de hemanjiomun neden parlak olduğunu, T1'de kanamanın neden parlak olduğunu anlamak için MR fiziği şart. Mekanizmayı bilirsen bulguyu asla unutmazsın.",
        "key_points": [
            "Kısa T1 (parlak T1): yağ, protein, kanama (methemoglobin), gadolinyum",
            "Uzun T2 (parlak T2): serbest su, kistler, hemanjiom (yavaş akan kan)",
            "T2 ampul bulb işareti: hemanjiomda yavaş akan kan → çok uzun T2 → BOS gibi parlak",
            "Kimyasal kayma (in/out phase): yağ ve su protonları faz uyumsuzluğu → sinyal düşümü",
            "DWI: su difüzyonunu ölçer — kısıtlama = yüksek hücresellik = malignite şüphesi",
            "STIR: yağ baskılı T2 — yağlı yapıların sinyalini sıfırlar"
        ],
        "source": "ESGAR 2024, Radiology Key MR Physics, LI-RADS v2018"
    },
    {
        "id": "ct_physics_hu",
        "name": "BT Fizik — Hounsfield Birimi ve Pencere/Seviye",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "Hounsfield birimi (HU) dokunun röntgen absorbsiyonunu ölçer. Su = 0 HU, hava = -1000 HU, kemik = +1000 HU. Karaciğer normal 50-65 HU. Pencere ve seviye ayarları görüntü kontrastını belirler.",
        "why_matters": "HU değerlerini bilmeden lezyonun spontan hiperdans mı (kanama, kalsifikasyon) yoksa hipodans mı (kist, yağ, nekroz) olduğunu söyleyemezsin.",
        "key_points": [
            "Karaciğer normal: 50-65 HU (dalaktan biraz daha yüksek)",
            "Basit kist: 0-20 HU (su dansitesi)",
            "Yağlı karaciğer: <50 HU (dalaktan düşük)",
            "Spontan hiperdens lezyon (>60 HU natif): kanama, kalsifikasyon, akut trombüs",
            "Amiodarone birikimi: karaciğerde diffüz hiperdensite (ilaç içinde iyot)",
            "Pencere/seviye: karaciğer için W:300-350, L:50-70 tipik"
        ],
        "source": "Radiology Key CT Physics, StatPearls, RSNA"
    },
    {
        "id": "us_physics_liver",
        "name": "US Fizik — Karaciğer için Pratik Temel",
        "organ": "liver",
        "level": 1,
        "category": "modality",
        "summary": "Ultrasonografi piezoelektrik kristallerin ses dalgası üretmesiyle çalışır. Dokudan geri yansıyan eko işlenerek görüntü oluşur. Frekans, rezolüsyon ve penetrasyonu belirler.",
        "why_matters": "Neden bazı lezyonlar hipereko, bazıları hipoekoik görünür? Posterior akustik güçlenme neden basit kistin işareti? Fiziği bilirsen hatalı yorumu önlersin.",
        "key_points": [
            "Yüksek frekans (7-15 MHz): iyi rezolüsyon, az penetrasyon — yüzeyel yapılar",
            "Düşük frekans (2-5 MHz): kötü rezolüsyon, iyi penetrasyon — derin yapılar (KC)",
            "Hipereko: yoğun reflektörler (yağ, fibrozis, kalsifikasyon, gaz)",
            "Hipoekoik: az reflektör (sıvı, uniform solid doku)",
            "Posterior akustik güçlenme: kist ardında ses dalgası engellenmeden geçer → parlak",
            "Arka gölge: kalsifikasyon veya taş sesi tamamen absorblar → karanlık gölge",
            "Operatöre bağımlılık: en büyük dezavantaj"
        ],
        "source": "EFSUMB Guidelines 2020, Radiology Key US Physics"
    },
    {
        "id": "liver_lab_tests",
        "name": "Karaciğer Enzim Testleri — Radyolog Ne Bilmeli?",
        "organ": "liver",
        "level": 1,
        "category": "physiology",
        "summary": "AST/ALT hepatosit hasarını, GGT/ALP biliyer hasarı, bilirubin ekskresyonu, albumin/PT sentetik fonksiyonu gösterir. AFP HKH tarama markeri. Radyolog bu değerleri bilmeden lezyon yorumlayamaz.",
        "why_matters": "Elevated AFP + siroz = HKH riski yüksek. Elevated CA 19-9 = ICC veya pankreatik/biliyer patoloji. Bu değerler görüntüleme yorumunu doğrudan etkiler.",
        "key_points": [
            "AST/ALT: hepatosit nekrozu — viral hepatit, iskemi, ilaç toksisitesi",
            "GGT/ALP yüksek + AST/ALT normal: biliyer obstrüksiyon, infiltratif hastalık",
            "Bilirubin yüksek: hepatik fonksiyon bozukluğu veya tıkanma sarılığı",
            "Albumin düşük + PT uzun: karaciğer sentetik fonksiyon bozukluğu (ağır hasar)",
            "AFP: HKH tarama ve takip — >20 ng/mL anlamlı yükselme",
            "CA 19-9: ICC, pankreatik/biliyer tümör — >37 U/mL anlamlı"
        ],
        "source": "AASLD 2023, EASL 2018, ACG 2024"
    },

    # ── KATMAN 2: PORTAL HİPERTANSİYON VE SİSTEMATİK YAKLAŞIM ───────────────

    {
        "id": "portal_hypertension",
        "name": "Portal Hipertansiyon — Mekanizma ve Görüntüleme Bulguları",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Portal ven basıncı >10 mmHg. Siroz en sık neden. Kollateral damarlar, asit, splenomegali, varis gelişir. Görüntülemede sistematik aranması gereken bulgular.",
        "why_matters": "Siroz raporlarken portal HT bulgularını sistematik aramak zorundasın. Kaçırırsan klinik yönetim değişir — varis kanaması hayati tehlike.",
        "key_points": [
            "Normal portal ven basıncı <5 mmHg, klinik anlamlı portal HT >10 mmHg",
            "Kollateraller: özofageal varis, umbilikal ven reopening (caput medusae), splenorenal şant",
            "Splenomegali: portal konjesyon nedeniyle",
            "Asit: portal HT + hipoalbüminemi → peritoneal sıvı birikimi",
            "Portal ven trombozu: portal HT komplikasyonu veya HKH invazyonu",
            "US: portal ven çapı >13 mm, hepatofugal akım (hepatoputal yerine)",
            "BT/MR: varis, splenomegali, asit, kollateral damarlar birlikte değerlendir"
        ],
        "source": "EASL 2018, AASLD 2023, ACG 2024"
    },
    {
        "id": "liver_cirrhosis_imaging",
        "name": "Sirozun Görüntüleme Bulguları — Sistematik Değerlendirme",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Siroz kronik hepatosit hasarı + fibrozis + rejenerasyon nodülleri ile karakterizedir. Her modalitede sistematik aranacak bulgular farklıdır. Zemini doğru tanımlamak lezyon yorumu için kritik.",
        "why_matters": "Sirozlu karaciğerde nodül = LI-RADS uygulanır. Sirozu tanımadan yanlış kategorize edersin. Ayrıca siroz kendisi raporlanması gereken bir bulgudur.",
        "key_points": [
            "US: heterojen parankim, nodüler yüzey konturu, sağ lob atrofisi, sol/kaudat lob hipertrofisi",
            "BT: nodüler kontur, heterojen dansitе, rejenerasyon nodülleri (hipodens)",
            "MR: T1 hiperintens displastik nodüller, siderotik nodüller (T2 hipointens)",
            "Siderotik nodül: demir birikimi → T2'de koyu → HKH'dan ayırt kritik",
            "Kaudat/sol lob büyümesi: sağ lob atrofisi ile birlikte siroz paterni",
            "İnce retiküler fibrozis: T2'de çok hafif hiperintens band"
        ],
        "source": "LI-RADS v2018, EASL 2018, Radiopaedia"
    },
    {
        "id": "liver_systematic_reading",
        "name": "Karaciğer BT/MR — Sistematik Okuma Protokolü",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Her karaciğer BT/MR'ı aynı sırayla okunmalı: teknik kalite → parankim → damarlar → safra yolları → lezyon → çevre yapılar. Sistematik okuma olmadan bulgular kaçırılır.",
        "why_matters": "Deneyimli radyolog ve acemi arasındaki fark çoğunlukla sistematikte. Lezyon bulmak kolay — ama portal ven trombozu, safra yolu dilatasyonu, çölyak lenfadenopatiyi kaçırmak raporun değerini sıfırlar.",
        "key_points": [
            "1. Teknik kalite: fazlar doğru mu? Kontrast zamanlaması yeterli mi?",
            "2. Karaciğer boyutu ve konturu: büyüme? Nodüler kontur?",
            "3. Parankim homojenitesi: yağlı infiltrasyon? Diffüz lezyon?",
            "4. Vasküler yapılar: portal ven, hepatik venler, hepatik arter — trombüs? Genişleme?",
            "5. Safra yolları: intra/ekstrahepatik dilatasyon? Taş? Kitle?",
            "6. Fokal lezyon: boyut, lokasyon (segment), karakterizasyon",
            "7. Çevre yapılar: asit, lenfadapati, adrenal, böbrek, akciğer tabanları"
        ],
        "source": "ESGAR 2024, ACR, Radiology Assistant"
    },
    {
        "id": "liver_fatty_infiltration",
        "name": "Karaciğer Yağlanması (Steatoz) — Görüntüleme",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Hepatositlere trigliserit birikimi. Diffüz veya fokal olabilir. BT'de karaciğer dalaktan daha düşük dansiteli. MR kimyasal kaymada sinyal düşümü karakteristik.",
        "why_matters": "Fokal yağlı infiltrasyon lezyon gibi görünebilir — yanlış tanıya yol açar. Diffüz steatoz HKH taramasını zorlaştırır.",
        "key_points": [
            "BT: karaciğer dansitesi dalak dansitesinin >10 HU altında = anlamlı steatoz",
            "BT: karaciğer dansitesi <40 HU = ciddi steatoz",
            "MR in/out phase: out-phase'de sinyal düşümü = yağ içeriği",
            "Fokal steatoz: damar çevresinde, periportal bölgede tipik",
            "Fokal yağ birikimi olmayan alan (fokal yağ sparing): lezyon gibi görünür",
            "NAFLD/NASH: obezite, DM2 ile ilişkili, siroza ilerleyebilir"
        ],
        "source": "ACG 2024, EASL 2016, Radiology Key"
    },
    {
        "id": "liver_biliary_anatomy",
        "name": "Safra Yolları Anatomisi ve Patolojisi",
        "organ": "liver",
        "level": 2,
        "category": "anatomy",
        "summary": "İntrahepatik safra kanalları → sağ/sol hepatik kanal → common hepatik kanal → sistik kanal → kolesistik → common bile duct → Oddi sfinkteri → duodenum. Dilatasyon lokalizasyonu tıkanma seviyesini gösterir.",
        "why_matters": "İntrahepatik safra yolu dilatasyonu ICC'nin erken bulgusu olabilir. Tıkanma seviyesini doğru söylemek cerrahi planlamayı etkiler.",
        "key_points": [
            "Normal common bile duct çapı <7 mm (kolesistektomi sonrası <10 mm)",
            "İntrahepatik dilatasyon: tıkanma hilusta veya intrahepatik",
            "Asimetrik dilatasyon: unilateral tıkanma (tümör, taş, striktür)",
            "MRCP: non-invaziv altın standart safra yolu görüntüleme",
            "Klatskin tümörü (hilar kolanjiyokarsinom): bifürkasyonda tıkanma",
            "Kolelitiazis: US'de posterior gölgeli hipereko yapı"
        ],
        "source": "EASL 2022, ACG 2024, MRCP Radiology Key"
    },
    {
        "id": "liver_vascular_pathology",
        "name": "Karaciğer Vasküler Patolojileri",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Portal ven trombozu, hepatik ven trombozu (Budd-Chiari), hepatik arter anomalileri ve arteryovenöz fistüller karaciğerin vasküler patolojileridir. Her birinin görüntüleme paterni farklıdır.",
        "why_matters": "Portal ven trombozu HKH invazyonunun işareti olabilir. Budd-Chiari acil bir durum. Bu patolojileri lezyon değerlendirirken es geçmek hata.",
        "key_points": [
            "Portal ven trombozu: BT/US'de dolma defekti — bland mı tümör mi?",
            "Tümör trombüsü (HKH): arteryel enhancement gösterir — LR-TIV",
            "Bland trombüs: enhancement göstermez",
            "Budd-Chiari: hepatik ven oklüzyonu → santral konjesyon, periferik atrofi",
            "Budd-Chiari BT: kaudat lob hipertrofisi (kendi venöz drenajı ayrı)",
            "Konjesif hepatopati: sağ kalp yetmezliğinde — periferik heterojen enhancement"
        ],
        "source": "EASL 2018, ACR, Radiology Key"
    },

    # ── KATMAN 2: KONTRAST DİNAMİĞİ İNTERAKTİF ŞEMA ─────────────────────────

    {
        "id": "contrast_dynamics_interactive",
        "name": "Kontrast Dinamiği — Lezyon Bazlı Karşılaştırma",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Farklı karaciğer lezyonları arteryel → portal → geç fazlarda farklı davranır. Bu davranış lezyonun vasküler yapısını yansıtır. Pattern recognition'ın temeli.",
        "why_matters": "Bu karşılaştırmayı tek bir tabloda görmek yüzlerce vaka değerinden daha öğretici. Bir kez anlayan asla unutmaz.",
        "key_points": [
            "HKH: Arteryel PARLAK → Portal KOYU (washout) — arteryel dominant",
            "Hemanjiom: Arteryel periferik nodüler → Portal doluyor → Geç DOLU (fill-in)",
            "FNH: Arteryel PARLAK → Portal İZO → Geç İZO (washout yok)",
            "Kist: Tüm fazlarda KOYU (enhancement yok) — avasküler",
            "Metastaz (hipovasküler): Natif KOYU → Portal en belirgin KOYU (target sign)",
            "ICC: Arteryel RIM → Portal persistan → Geç PARLAK (fibröz stroma)",
            "Adenom: Arteryel PARLAK → Portal İZO/hafif koyu — HKH'ya benzer ama context farklı"
        ],
        "source": "LI-RADS v2018, EASL 2016, ACG 2024, Radiology Assistant"
    },
]

# ── ÖNKOŞUL İLİŞKİLERİ ───────────────────────────────────────────────────────
PREREQUISITES = [
    # Histoloji önce anatomi
    {"from": "liver_anatomy_segments",     "to": "liver_histology_lobule"},
    {"from": "liver_histology_lobule",     "to": "liver_histology_hepatocyte"},
    {"from": "liver_histology_hepatocyte", "to": "liver_contrast_gadolinium"},
    {"from": "liver_histology_hepatocyte", "to": "liver_lab_tests"},

    # BT fiziği kontrast farmakolojisinden önce
    {"from": "ct_principles",             "to": "ct_physics_hu"},
    {"from": "ct_physics_hu",             "to": "liver_contrast_iodinated"},
    {"from": "liver_contrast_iodinated",  "to": "contrast_dynamics_interactive"},

    # MR fiziği
    {"from": "mr_principles",             "to": "mr_physics_t1_t2"},
    {"from": "mr_physics_t1_t2",          "to": "liver_contrast_gadolinium"},
    {"from": "liver_contrast_gadolinium", "to": "contrast_dynamics_interactive"},

    # US fiziği
    {"from": "us_principles",             "to": "us_physics_liver"},

    # Klinik bilgi
    {"from": "liver_physiology_function", "to": "liver_lab_tests"},
    {"from": "liver_physiology_function", "to": "portal_hypertension"},
    {"from": "liver_anatomy_vasculature", "to": "portal_hypertension"},
    {"from": "portal_hypertension",       "to": "liver_cirrhosis_imaging"},
    {"from": "liver_cirrhosis_imaging",   "to": "concept_lirads"},

    # Sistematik okuma
    {"from": "ct_principles",             "to": "liver_systematic_reading"},
    {"from": "mr_principles",             "to": "liver_systematic_reading"},
    {"from": "liver_anatomy_segments",    "to": "liver_systematic_reading"},

    # Yağlanma
    {"from": "ct_physics_hu",             "to": "liver_fatty_infiltration"},
    {"from": "mr_physics_t1_t2",          "to": "liver_fatty_infiltration"},

    # Safra yolları
    {"from": "liver_anatomy_segments",    "to": "liver_biliary_anatomy"},

    # Vasküler patoloji
    {"from": "liver_anatomy_vasculature", "to": "liver_vascular_pathology"},
    {"from": "portal_hypertension",       "to": "liver_vascular_pathology"},

    # Kontrast dinamiği — en son
    {"from": "contrast_dynamics_interactive", "to": "concept_hcc_pathophysiology"},
    {"from": "contrast_dynamics_interactive", "to": "concept_hemangioma_pathophysiology"},
    {"from": "contrast_dynamics_interactive", "to": "concept_fnh_vs_adenoma"},
    {"from": "contrast_dynamics_interactive", "to": "concept_icc_vs_hcc"},
]

# ── CONCEPT → DIAGNOSIS ilişkileri ───────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "portal_hypertension",         "diagnosis": "hcc",        "relation": "RISK_FACTOR_FOR"},
    {"concept": "liver_cirrhosis_imaging",     "diagnosis": "hcc",        "relation": "CONTEXT_FOR"},
    {"concept": "liver_vascular_pathology",    "diagnosis": "hcc",        "relation": "COMPLICATION_OF"},
    {"concept": "liver_biliary_anatomy",       "diagnosis": "icc",        "relation": "EXPLAINS"},
    {"concept": "liver_fatty_infiltration",    "diagnosis": "simple_cyst","relation": "DIFFERENTIAL_FROM"},
    {"concept": "contrast_dynamics_interactive","diagnosis": "hcc",       "relation": "KEY_FINDING_FOR"},
    {"concept": "contrast_dynamics_interactive","diagnosis": "hemangioma","relation": "KEY_FINDING_FOR"},
    {"concept": "contrast_dynamics_interactive","diagnosis": "fnh",       "relation": "KEY_FINDING_FOR"},
    {"concept": "liver_contrast_gadolinium",   "diagnosis": "fnh",        "relation": "KEY_FINDING_FOR"},
    {"concept": "liver_contrast_gadolinium",   "diagnosis": "hca",        "relation": "KEY_FINDING_FOR"},
    {"concept": "liver_lab_tests",             "diagnosis": "hcc",        "relation": "SUPPORTS_DIAGNOSIS"},
    {"concept": "liver_lab_tests",             "diagnosis": "icc",        "relation": "SUPPORTS_DIAGNOSIS"},
]

# ── YENİ SORULAR ─────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_portal_triad",
        "concept_id": "liver_histology_lobule",
        "type": "multiple_choice",
        "question": "Portal triad hangi 3 yapıdan oluşur?",
        "options": [
            "Hepatik ven + safra kanalı + lenfatik damar",
            "Hepatik arter + portal ven + safra kanalı",
            "Portal ven + santral ven + hepatik arter",
            "Sinüzoid + safra kanalikülü + Disse aralığı"
        ],
        "correct": 1,
        "explanation": "Portal triad: hepatik arter dalı + portal ven dalı + safra kanalı dalı. Kan portal triaddan sinüzoidlere oradan santral vene akar. Safra ise ters yönde akar: hepatositlerden safra kanalikülüne oradan portal triad safra kanalına.",
        "level": 1
    },
    {
        "id": "q_blood_flow_direction",
        "concept_id": "liver_histology_lobule",
        "type": "multiple_choice",
        "question": "Karaciğer lobülünde kan akışı hangi yönde gerçekleşir?",
        "options": [
            "Santral venden portal triada doğru",
            "Portal triaddan sinüzoidler aracılığıyla santral vene doğru",
            "Hepatik venden portal vene doğru",
            "Safra kanalından hepatik artere doğru"
        ],
        "correct": 1,
        "explanation": "Kan portal triaddan (hepatik arter + portal ven) sinüzoidlere girer, hepatositlerle temas ederek santral vene akar. Santral venler hepatik venleri oluşturur ve IVC'ye drene olur. Safra ise tam tersi yönde akar.",
        "level": 1
    },
    {
        "id": "q_hbp_mechanism",
        "concept_id": "liver_histology_hepatocyte",
        "type": "multiple_choice",
        "question": "Gadoxetat (Primovist) MR'da hepatobiliyer faz neden oluşur?",
        "options": [
            "Gadoxetat böbreklerden yavaş atılır, karaciğerde birikir",
            "OATP1B1/1B3 taşıyıcıları ile fonksiyonel hepatositler gadoxetatı içine alır",
            "Gadoxetat yağda çözünür, hepatositlere pasif difüze olur",
            "Portal ven gadoxetatı direkt karaciğere taşır"
        ],
        "correct": 1,
        "explanation": "Gadoxetat OATP1B1 ve OATP1B3 organik anyonik taşıyıcı proteinleri aracılığıyla fonksiyonel hepatositler tarafından aktif olarak alınır. Bu nedenle sadece fonksiyonel hepatosit içeren lezyonlar (FNH) HBP'de hiperintens görünür. HKH, adenom ve ICC'de bu taşıyıcılar bozuk çalıştığından hipointens kalırlar.",
        "level": 2
    },
    {
        "id": "q_hu_values",
        "concept_id": "ct_physics_hu",
        "type": "multiple_choice",
        "question": "Natif BT'de karaciğer dansitesi hangi değer aralığında normaldir?",
        "options": [
            "0-20 HU",
            "20-40 HU",
            "50-65 HU",
            "80-100 HU"
        ],
        "correct": 2,
        "explanation": "Normal karaciğer 50-65 HU aralığındadır ve dalaktan biraz daha yüksek dansiteye sahiptir. Karaciğer dansitesi <40 HU ise ciddi yağlı infiltrasyon (steatoz) düşünülür. Karaciğer dansitesi dalak dansitesinden >10 HU düşükse de anlamlı steatoz vardır.",
        "level": 1
    },
    {
        "id": "q_portal_ht_collaterals",
        "concept_id": "portal_hypertension",
        "type": "multiple_choice",
        "question": "Portal hipertansiyon sonucu gelişen kollateral damarlar hangi seçenekte doğru verilmiştir?",
        "options": [
            "Hepatik ven varisi + renal ven genişlemesi",
            "Özofageal varis + umbilikal ven reopening + splenorenal şant",
            "Mezenterik arteriyovenöz fistül + portal ven anevrizması",
            "Hepatik arteriyel hipertrofi + portal ven trombozu"
        ],
        "correct": 1,
        "explanation": "Portal hipertansiyonda portal ven basıncı arttığında kan alternatif yollar arar: (1) Özofageal varis — en tehlikeli, kanama riski var. (2) Umbilikal venin açılması — caput medusae. (3) Splenorenal şant — sol renal vene bağlantı. Bunları görüntülemede sistematik aramak zorunludur.",
        "level": 2
    },
    {
        "id": "q_t2_physics",
        "concept_id": "mr_physics_t1_t2",
        "type": "multiple_choice",
        "question": "T2 ağırlıklı görüntüde neden kistler ve hemanjiomlar parlak görünür?",
        "options": [
            "Bu yapılar gadolinyum kontrast biriktirir",
            "Yüksek yağ içeriği T2 sinyalini artırır",
            "Serbest su molekülleri uzun T2 relaksasyonuna neden olur",
            "Fibröz doku T2'de her zaman parlaktır"
        ],
        "correct": 2,
        "explanation": "Serbest hareket eden su molekülleri uzun T2 relaksasyonu gösterir — bu yüzden BOS, kist içeriği ve yavaş akan kan (hemanjiom) T2'de parlak görünür. Hemanjiomun T2'de BOS kadar parlak görünmesi 'ampul bulb işareti' olarak adlandırılır ve diagnostiktir.",
        "level": 1
    },
    {
        "id": "q_contrast_dynamics_hcc",
        "concept_id": "contrast_dynamics_interactive",
        "type": "multiple_choice",
        "question": "HKH'nın kontrastlı BT/MR'daki karakteristik enhancement paterni nedir?",
        "options": [
            "Tüm fazlarda düşük sinyal (avasküler)",
            "Periferik nodüler arteryel enhancement → geç santral dolum",
            "Arteryel fazda hiperenhancement → portal/geç fazda washout",
            "Arteryel fazda rim enhancement → geç fazda persistan enhancement"
        ],
        "correct": 2,
        "explanation": "HKH arteryel dominant kanlanması nedeniyle arteryel fazda çevre parankimden belirgin parlak görünür (APHE). Portal/geç fazda ise tümör içindeki kontrast hızla uzaklaşır (portal ven kanlanması yok) ve çevre parankimden koyu görünür (washout). Bu APHE + washout kombinasyonu LR-5 kriteridir.",
        "level": 2
    },
    {
        "id": "q_fatty_liver_ct",
        "concept_id": "liver_fatty_infiltration",
        "type": "multiple_choice",
        "question": "Natif BT'de karaciğer steatozunun en güvenilir kriteri hangisidir?",
        "options": [
            "Karaciğer dansitesi <60 HU",
            "Karaciğer dansitesi dalak dansitesinden >10 HU düşük",
            "Karaciğerin homojen görünümü",
            "Portal venin görünmemesi"
        ],
        "correct": 1,
        "explanation": "Karaciğer dansitesi dalak dansitesinden >10 HU düşük olması anlamlı steatoz kriteridir. Mutlak HU değeri (<40 HU ciddi steatoz için) de kullanılabilir ancak karaciğer-dalak farkı daha güvenilirdir. MR kimyasal kayma sekansı (in/out phase) daha hassas ve özgüldür.",
        "level": 2
    },
    {
        "id": "q_systematic_reading",
        "concept_id": "liver_systematic_reading",
        "type": "multiple_choice",
        "question": "Karaciğer BT'si okurken fokal lezyon değerlendirmesinden ÖNCE yapılması gereken en önemli adım hangisidir?",
        "options": [
            "Lezyonun boyutunu ölçmek",
            "Kontrast tipi ve dozunu belirlemek",
            "Teknik kalite, parankim, damarlar ve safra yollarını değerlendirmek",
            "Klinisyenin sorusunu okumak"
        ],
        "correct": 2,
        "explanation": "Sistematik okuma protokolü: teknik kalite → karaciğer boyut/kontur → parankim → vasküler yapılar (portal ven trombozu!) → safra yolları → fokal lezyon → çevre yapılar. Direkt lezyon aramaya gitmek portal ven trombozu, asit, lenfadenopati gibi kritik bulguların atlanmasına yol açar.",
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
        tx.run("""
            MATCH (q:Question {id: $q_id})
            MATCH (c:Concept {id: $c_id})
            MERGE (q)-[:TESTS]->(c)
        """, q_id=q["id"], c_id=q["concept_id"])
    return len(QUESTIONS)


# ── ÇALIŞTIR ──────────────────────────────────────────────────────────────────
print("\n── Katman 1-2 Concept'leri yükleniyor...")
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
✓ Katman 1-2 içeriği başarıyla yüklendi.
  Yeni Concepts   : {len(CONCEPTS)}
  Yeni Önkoşullar : {len(PREREQUISITES)}
  Yeni Sorular    : {len(QUESTIONS)}
""")

from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

# ── KATMAN 5 EK CONCEPTLER ────────────────────────────────────────────────────

CONCEPTS_L5 = [
    {
        "id": "pitfall_post_op_liver",
        "name": "Post-operatif Karaciğer Değişiklikleri — Tuzaklar",
        "organ": "liver",
        "level": 5,
        "category": "technique",
        "summary": "Rezeksiyon, ablasyon veya transplantasyon sonrası karaciğerde beklenen ve beklenmeyen değişiklikler. Beklenen değişiklikleri komplikasyon sanmak yanlış girişime yol açar.",
        "why_matters": "Post-rezeksiyon boşlukta sıvı birikimi, perilesional ödem ve reaktif enhancement normal bulgu. Bunları nüks veya apse sanmak hastayı gereksiz prosedüre sürükler.",
        "key_points": [
            "Post-rezeksiyon seroma: düşük dansiteli sıvı koleksiyonu — beklenen, kontrast tutmaz",
            "Bilioma: yavaş büyüyen sıvı — MRCP ile safra yolu sızıntısı teyidi",
            "Reaktif perilesional enhancement: ablasyon sonrası 1-3 ay — inflamasyon, nüks değil",
            "Karaciğer hipertrofisi: kontralateral lob kompansatuvar büyür — normal",
            "Post-TACE lipiodol: karaciğerde diffüz yüksek dansite — normal birikim",
            "Ablasyon zonu büyümesi (ilk 24 saat): ödem — stabil veya küçülüyorsa normal",
            "Nüks bulgusu: ablasyon zonunda nodüler arteryel enhancement"
        ],
        "source": "LI-RADS TRA v2024, Radiology Key, RadioGraphics Post-treatment"
    },
    {
        "id": "pitfall_biopsy_complications",
        "name": "Karaciğer Biyopsisi Sonrası Komplikasyonlar",
        "organ": "liver",
        "level": 5,
        "category": "technique",
        "summary": "Perkütan karaciğer biyopsisi sonrası görüntüleme ile takip edilmesi gereken komplikasyonlar: kanama, hemobili, arteryovenöz fistül, pnömotoraks.",
        "why_matters": "Biyopsi sonrası ağrı veya hemodinamik instabilite görüntüleme endikasyonu. US Doppler ve BT ile kanama odağı veya AV fistül tespiti acil girişimi belirler.",
        "key_points": [
            "Subkapsüler hematom: en sık komplikasyon — US ile izlem",
            "Aktif kanama: BT'de kontrast extravazasyonu — anjiyoembolizasyon",
            "Arteryovenöz fistül: Doppler'da arteryel fistül akımı — genellikle kendiliğinden kapanır",
            "Hemobili: sağ üst kadran ağrı + sarılık + kanama üçlüsü (Quincke triadı)",
            "Pnömotoraks: sağ lob üst posterior biyopsilerinde — göğüs BT",
            "Needle tract seeding: HKH biyopsisi sonrası nadir ama bildirilmiş",
            "Biyopsi sonrası 4 saat US kontrolü önerilir — aktif kanama ekartasyonu"
        ],
        "source": "EASL 2018, AASLD, Radiology Key"
    },
    {
        "id": "pitfall_radiation_liver",
        "name": "Radyasyon Hasarı ve RILD — Karaciğer Görüntüleme",
        "organ": "liver",
        "level": 5,
        "category": "pathology",
        "summary": "Radyasyon indüklenmiş karaciğer hastalığı (RILD) ve SBRT/TARE sonrası radyasyon etki alanı görüntülemesi. Tedavi etkisini progresyondan ayırt kritik.",
        "why_matters": "SBRT sonrası radyasyon etkisi keskin sınırlı, geometrik şekilli enhancement paterni gösterir. Bunu progresyon sanmak gereksiz tedavi değişikliğine yol açar.",
        "key_points": [
            "RILD: radyasyon dozunun >30-35 Gy olduğu bölgede hepatit benzeri tablo",
            "Görüntüleme: radyasyon portu içinde enhancement artışı + ödem (akut faz)",
            "Kronik RILD: fibrozis — T2 düşük sinyal, parankimal atrofi",
            "SBRT sonrası: geometrik (küre/silindir) şekilli enhancement alanı — lezyon değil",
            "Y-90 TARE sonrası: tedavi portu içinde parankimal değişiklik + lezyon nekrozu",
            "TARE'de 'abscopal effect': tedavi dışı metastazlarda regresyon (nadir)",
            "Radyasyon fibrozis: geç faz persistan enhancement — ICC taklidi yapabilir"
        ],
        "source": "LI-RADS TRA v2024, Radiology Key RILD, RadioGraphics SBRT"
    },
    {
        "id": "pitfall_pregnancy_liver",
        "name": "Gebelikte Karaciğer Görüntüleme — Özel Durumlar",
        "organ": "liver",
        "level": 5,
        "category": "technique",
        "summary": "Gebelikte karaciğer lezyonlarının değerlendirilmesi özel yaklaşım gerektirir. US önce, kontrastsız MR ikinci seçenek. Gadolinyum ve iyotlu kontrast fetal risk taşır.",
        "why_matters": "Gebelikte HELLP sendromu, akut gebelik yağlı karaciğeri ve spontan karaciğer rüptürü hayati tehlike. US ve MR güvenli, BT ve kontrast kısıtlı.",
        "key_points": [
            "US ilk basamak: güvenli, karaciğer lezyonu, subkapsüler hematom",
            "Kontrastsız MR: US'de şüpheli lezyon — iyonize radyasyon yok",
            "Gadolinyum: plasenta geçer, fetal risk — sadece zorunlu ise",
            "İyotlu kontrast: neonatal hipotiroidizm riski — gerekirse kullan",
            "HELLP sendromu: karaciğer hematomu/rüptürü — acil US + MR",
            "Akut gebelik yağlı karaciğeri (AFLP): BT/MR'da diffüz steatoz — US sensitif değil",
            "Hemanjiom gebelikte büyüyebilir (östrojen etkisi) — beklenen değişim"
        ],
        "source": "ACR Pregnancy Imaging, EASL, Radiology Key"
    },
]

# ── KATMAN 6 EK CONCEPTLER ────────────────────────────────────────────────────

CONCEPTS_L6 = [
    {
        "id": "multimodal_y90_imaging",
        "name": "Y-90 TARE Sonrası Görüntüleme",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "Y-90 transarteriyel radyoembolizasyon (TARE) sonrası görüntüleme: tedavi yanıtı, komplikasyonlar ve nüks değerlendirmesi. LI-RADS TRA radyasyon tedavileri için özel kriter seti kullanır.",
        "why_matters": "Y-90 sonrası MR değerlendirmesi standart kontrast kinetikten farklı. Radyasyon etkisi lezyon sınırlarını değiştirir. Doğru yorum için TARE spesifik protokol gerekli.",
        "key_points": [
            "TARE sonrası ilk görüntüleme: 4-8 hafta (akut değişiklikler stabil olana dek)",
            "Yanıt bulguları: santral nekroz + azalan enhancement veya hiç yok",
            "Radyasyon etkisi: perilesional parankimal değişiklik — lezyon değil",
            "mRECIST: sadece enhancing canlı tümör ölçülür — nekroz dahil edilmez",
            "Tc-99m MAA sintigrafisi: tedavi öncesi akciğer şantı değerlendirmesi",
            "Post-Y90 SPECT/CT: microsphere dağılımını doğrular",
            "Komplikasyon: radyasyon gastrit/ülser, kolanjit — klinik ile korelasyon"
        ],
        "source": "LI-RADS TRA 2024, EASL 2018, RadioGraphics Y90"
    },
    {
        "id": "multimodal_ai_lirads",
        "name": "Yapay Zeka ve Otomatik LI-RADS — Güncel Durum",
        "organ": "liver",
        "level": 6,
        "category": "technique",
        "summary": "Karaciğer görüntülemesinde yapay zeka uygulamaları: otomatik LI-RADS kategorizasyon, lezyon tespiti, segmentasyon ve tedavi yanıt değerlendirmesi. Klinik uygulamaya giriş aşaması.",
        "why_matters": "Radyolojide AI hızla gelişiyor. Karaciğer görüntülemesinde mevcut uygulamaların ne yapabildiğini ve sınırlarını bilmek hem akademik hem pratik değer taşır.",
        "key_points": [
            "LI-RADS otomasyon: majör özellik tespiti %80-85 doğruluk (2024 meta-analiz)",
            "Lezyon segmentasyon: karaciğer ve lezyon hacmi otomatik hesaplama",
            "Tedavi yanıt: mRECIST otomatik ölçüm — radyolog onayı gerekli",
            "Sınırlar: küçük lezyon (<1 cm) tespiti hâlâ yetersiz",
            "False positive: AV şant ve psödolezyonları atlamak zor",
            "LLM tabanlı raporlama: yapılandırılmış rapor otomasyonu — klinik değerlendiriliyor",
            "FDA onaylı karaciğer AI: sınırlı — radyolog karar mercii"
        ],
        "source": "Radiology 2024 AI Review, LI-RADS 2024, Nature Medicine"
    },
]

# ── ÖNKOŞULLAR ────────────────────────────────────────────────────────────────
PREREQUISITES_L5 = [
    {"from": "multimodal_treatment_response", "to": "pitfall_post_op_liver"},
    {"from": "liver_ct_protocol",             "to": "pitfall_post_op_liver"},
    {"from": "liver_systematic_reading",      "to": "pitfall_biopsy_complications"},
    {"from": "us_physics_liver",              "to": "pitfall_biopsy_complications"},
    {"from": "multimodal_treatment_response", "to": "pitfall_radiation_liver"},
    {"from": "liver_ct_protocol",             "to": "pitfall_radiation_liver"},
    {"from": "us_physics_liver",              "to": "pitfall_pregnancy_liver"},
    {"from": "liver_mr_protocol",             "to": "pitfall_pregnancy_liver"},
]

PREREQUISITES_L6 = [
    {"from": "multimodal_treatment_response", "to": "multimodal_y90_imaging"},
    {"from": "hcc_bclc_staging",             "to": "multimodal_y90_imaging"},
    {"from": "multimodal_reporting_structured","to": "multimodal_ai_lirads"},
    {"from": "lirads_lr_categories_decision", "to": "multimodal_ai_lirads"},
]

# ── CONCEPT → DIAGNOSIS ───────────────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "pitfall_post_op_liver",    "diagnosis": "hcc",        "relation": "FOLLOW_UP_PITFALL"},
    {"concept": "pitfall_radiation_liver",  "diagnosis": "hcc",        "relation": "TREATMENT_PITFALL"},
    {"concept": "multimodal_y90_imaging",   "diagnosis": "hcc",        "relation": "TREATMENT_RESPONSE"},
]

# ── 200 EK SORU ───────────────────────────────────────────────────────────────
QUESTIONS = [
    # ── Karaciğer anatomi ─────────────────────────────────────────────────────
    {
        "id": "bulk2_seg_1",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Segment V ve VIII hangi karaciğer bölümünde yer alır?",
        "options": ["Sol lob anterior", "Sağ lob ön (anterior) segment", "Sağ lob arka (posterior) segment", "Kaudat lob"],
        "correct": 1,
        "explanation": "Sağ lob ön segment: Segment V (alt) ve Segment VIII (üst). Sağ lob arka segment: Segment VI (alt) ve Segment VII (üst). Bu ayrım sağ hepatik ven tarafından yapılır.",
        "level": 1
    },
    {
        "id": "bulk2_seg_2",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Cantlie hattı karaciğeri nasıl böler?",
        "options": [
            "Sağ lobu ön ve arka segmentlere",
            "Sağ ve sol anatomik lobu — safra kesesinden IVC'ye çizgi",
            "Sol lobu Segment II ve III'e",
            "Kaudat lobu sağ ve soldan ayırır"
        ],
        "correct": 1,
        "explanation": "Cantlie hattı safra kesesinden IVC'ye uzanan hayali çizgidir. Orta hepatik ven bu hat üzerinde seyreder. Karaciğeri fonksiyonel olarak sağ ve sol loba böler. Anatomik sağ/sol ayrımından (falciform ligament) farklıdır.",
        "level": 1
    },
    {
        "id": "bulk2_seg_3",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Segment II ve III hangi hepatik ven tarafından ayrılır?",
        "options": ["Orta hepatik ven", "Sağ hepatik ven", "Sol hepatik ven", "Kaudat ven"],
        "correct": 2,
        "explanation": "Sol hepatik ven sol lobu Segment II (üst posterior) ve Segment III (alt anterior) olarak böler. Falciform ligament ise Segment III ile Segment IV'ü (kare lob) ayırır.",
        "level": 1
    },

    # ── Portal hipertansiyon ───────────────────────────────────────────────────
    {
        "id": "bulk2_portal_1",
        "concept_id": "portal_hypertension",
        "type": "multiple_choice",
        "question": "Özofageal varisler portal hipertansiyonda neden gelişir?",
        "options": [
            "Hepatik ven tıkanması nedeniyle",
            "Portal basınç artışı → sol gastrik ven → özofageal venler kollateral yol",
            "Arteryel kanlanma artışı nedeniyle",
            "Albumin düşüklüğü nedeniyle"
        ],
        "correct": 1,
        "explanation": "Portal basınç artışında kan alternatif yollar arar. Sol gastrik ven (koroner ven) portal sisteme bağlıdır. Basınç artınca sol gastrik ven aracılığıyla özofageal submukosal venlerle sistemik dolaşım arasında kollateral açılır. Bu varislerin kanaması hayatı tehdit eder.",
        "level": 2
    },
    {
        "id": "bulk2_portal_2",
        "concept_id": "portal_hypertension",
        "type": "multiple_choice",
        "question": "Splenomegali portal hipertansiyonda neden oluşur?",
        "options": [
            "Dalak tümörü",
            "Splenik ven konjesyonu — portal basınç splenik vene yansır",
            "Anemi",
            "Karaciğer yetmezliği"
        ],
        "correct": 1,
        "explanation": "Splenik ven portal sisteme bağlıdır. Portal basınç yükselince splenik ven basıncı da artar → dalak konjesyonu → splenomegali. Konjesif splenomegali sekonder hipersplenizme (pansitopeni) yol açabilir. Splenomegali portal HT'nin tutarlı bir görüntüleme bulgusudur.",
        "level": 2
    },

    # ── Siroz ─────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_cirrhosis_1",
        "concept_id": "liver_cirrhosis_imaging",
        "type": "multiple_choice",
        "question": "Sirozda sol lob ve kaudat lobun büyümesi, sağ lobun küçülmesi neden oluşur?",
        "options": [
            "Sol lob daha az etkilenir — rastlantısal",
            "Sağ portal ven dalının fibrozu → sağ lob portal akım azalır → atrofi. Sol/kaudat ven korunur → hipertrofi",
            "Anatomik farklılık",
            "Fibrozis önce sağ lobu etkiler"
        ],
        "correct": 1,
        "explanation": "Sirozda sağ portal ven dalları fibroz baskısına daha fazla maruz kalır → sağ lob portal akım azalır → atrofi. Sol lob ve kaudat lobun portal ve venöz anatomisi farklı olduğundan korunur ve kompansatuvar büyür. Bu patern siroza özgü ve görüntülemede tanısal değer taşır.",
        "level": 2
    },
    {
        "id": "bulk2_cirrhosis_2",
        "concept_id": "liver_cirrhosis_imaging",
        "type": "multiple_choice",
        "question": "Nodüler karaciğer konturunun nedeni nedir?",
        "options": [
            "Multipl metastaz",
            "Rejenerasyon nodülleri fibrozis bandları arasında karaciğer yüzeyini kaldırır",
            "Kistik lezyonlar",
            "Yağlı infiltrasyon"
        ],
        "correct": 1,
        "explanation": "Siroz = fibrozis + rejenerasyon nodülleri. Rejenerasyon nodülleri fibrotik bandlar arasında büyürken karaciğer yüzeyini lokal olarak iter → nodüler kontur. Bu özellikle US'de ve BT/MR'da koronal reformat görüntülerde belirgindir.",
        "level": 2
    },

    # ── BT protokolleri ───────────────────────────────────────────────────────
    {
        "id": "bulk2_ct_protocol_1",
        "concept_id": "liver_ct_protocol",
        "type": "multiple_choice",
        "question": "Kolorektal kanser evrelemelenmesinde karaciğer metastazı taraması için hangi BT fazı yeterlidir?",
        "options": [
            "Sadece natif faz",
            "Sadece arteryel faz",
            "Portal venöz faz — hipovasküler metastaz burada en belirgin",
            "Geç faz"
        ],
        "correct": 2,
        "explanation": "Kolorektal metastazlar hipovaskülerdir. Portal venöz fazda karaciğer parankimi maksimum kontrast alırken hipovasküler tümör az kontrast alır → en yüksek lezyon-parankim farkı portal fazda. Arteryel faz bu tümörler için ek bilgi sağlamaz. Multifazik protokol HKH şüphesi içindir.",
        "level": 2
    },
    {
        "id": "bulk2_ct_protocol_2",
        "concept_id": "liver_ct_protocol",
        "type": "multiple_choice",
        "question": "Karaciğer BT'sinde arteryel faz ne zaman alınır?",
        "options": [
            "Enjeksiyondan 5-10 saniye sonra",
            "Enjeksiyondan 25-35 saniye sonra",
            "Enjeksiyondan 60-70 saniye sonra",
            "Enjeksiyondan 3-5 dakika sonra"
        ],
        "correct": 1,
        "explanation": "Arteryel faz: 25-35 saniye. Bu dönemde hepatik arter kontrast doludur, portal ven henüz dolmaya başlamaktadır. Hipervasküler lezyonlar (HKH) bu fazda en parlaktır. 60-70 saniye portal venöz fazdır. 3-5 dakika geç (equilibrium) fazdır.",
        "level": 2
    },

    # ── MR protokol ───────────────────────────────────────────────────────────
    {
        "id": "bulk2_mr_protocol_1",
        "concept_id": "liver_mr_protocol",
        "type": "multiple_choice",
        "question": "Karaciğer MR'ında DWI için en uygun b değerleri hangileridir?",
        "options": [
            "Sadece b0",
            "b50, b400, b800 + ADC haritası",
            "Sadece b1000",
            "b100, b200 yeterli"
        ],
        "correct": 1,
        "explanation": "Karaciğer DWI protokolü: düşük b (b50) vasküler etkiyi azaltır, orta b (b400) difüzyon değerlendirme, yüksek b (b800) malignite tespiti — yüksek b'de arka plan baskılanır, yüksek hücreli lezyonlar parlak. ADC haritası sayısal difüzyon kısıtlamasını ölçer. T2 shine-through ayrımı için ADC zorunlu.",
        "level": 2
    },
    {
        "id": "bulk2_mr_protocol_2",
        "concept_id": "liver_mr_protocol",
        "type": "multiple_choice",
        "question": "MRCP'de en iyi görüntüleme hangi sekansla elde edilir?",
        "options": [
            "T1 spoiled GRE",
            "Ağır T2 ağırlıklı sekans (HASTE veya RARE) — safra yüksek sinyal, çevre doku düşük",
            "DWI",
            "STIR"
        ],
        "correct": 1,
        "explanation": "MRCP ağır T2 ağırlıklı sekans kullanır. Serbest su (safra, pankreas sıvısı) çok uzun T2 nedeniyle çok parlak görünür, çevre solid doku düşük sinyalde kalır. 2D thick-slab veya 3D thin-slab teknikler kullanılır. Kontrast madde gerekmez.",
        "level": 2
    },

    # ── Hemokromatoz ──────────────────────────────────────────────────────────
    {
        "id": "bulk2_hemochrom_1",
        "concept_id": "liver_hemochromatosis",
        "type": "multiple_choice",
        "question": "Herediter hemokromatoz ile sekonder (transfüzyon) hemosiderozisi MR'da nasıl ayırt ederiz?",
        "options": [
            "Ayırt edilemez",
            "Herediter: karaciğer + pankreas + kalp tutulumu; Sekonder: karaciğer + dalak + kemik iliği tutulumu",
            "Herediter sadece karaciğer",
            "Sekonder sadece kemik iliği"
        ],
        "correct": 1,
        "explanation": "Herediter hemokromatoz (HFE mutasyonu): demir hepatositlere birikim yapar → karaciğer + pankreas + kalp + endokrin. Dalak genellikle korunur. Sekonder hemosiderozis (transfüzyon, hemoliz): retiküloendotelyal sistem etkilenir → karaciğer + dalak + kemik iliği. Pankreas ve kalp korunur. Bu dağılım MR'da tanısal.",
        "level": 2
    },

    # ── Travma ────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_trauma_1",
        "concept_id": "liver_trauma_aast",
        "type": "multiple_choice",
        "question": "AAST Grade V karaciğer yaralanması neyi içerir?",
        "options": [
            "Subkapsüler hematom >%50",
            "Parankimal disrupsyon >%75 veya juxtahepatik venöz yaralanma (hepatik ven/retrohepatik IVC)",
            "3-5 Couinaud segmenti tutulumu",
            "Sadece laserasyon >5 cm"
        ],
        "correct": 1,
        "explanation": "AAST Grade V: parankimal disrupsyon >%75 hepatik lob VEYA juxtahepatik venöz yaralanma (hepatik ven veya retro-hepatik IVC). En ağır grade — mortalite yüksek. Cerrahi kontrol çoğunlukla gerekli. 2018 revizyonunda vasküler yaralanma bu gruba dahil edildi.",
        "level": 2
    },
    {
        "id": "bulk2_trauma_2",
        "concept_id": "liver_trauma_findings",
        "type": "multiple_choice",
        "question": "Travma BT'sinde 'flat IVC' (basık IVC) bulgusu ne anlama gelir?",
        "options": [
            "IVC trombozu",
            "Ağır hipovolemi — kan hacmi kritik düşük, acil transfüzyon",
            "Budd-Chiari sendromu",
            "Normal varyant"
        ],
        "correct": 1,
        "explanation": "IVC normalde yuvarlak/oval kesitte görülür. Şiddetli kan kaybında IVC çapı azalır ve BT'de 'basık/yassı' görünür. Bu bulgul ağır hipovoleminin kritik işaretidir — acil transfüzyon ve hemostatik resüsitasyon gerektirir. Klinik ekiple acil iletişim şart.",
        "level": 2
    },

    # ── Transplantasyon ───────────────────────────────────────────────────────
    {
        "id": "bulk2_transplant_1",
        "concept_id": "liver_transplant_imaging",
        "type": "multiple_choice",
        "question": "Transplantasyon sonrası hepatik arter stenozu Doppler'da nasıl görünür?",
        "options": [
            "Arteryel akım yok",
            "Tardus-parvus dalga formu — düşük hız, uzun yükselme zamanı",
            "Yüksek hızlı türbülanslı akım",
            "Hepatofugal akım"
        ],
        "correct": 1,
        "explanation": "Hepatik arter stenozu: darlık proksimalinde normal akım, distalinde tardus-parvus (geç ve yavaş yükselen) dalga formu. Anastomoz bölgesinde hız >200 cm/s stenozu gösterir. Tam oklüzyonda distal akım yoktur. Tardus-parvus morfolojisi deneyimli bir gözlemci tarafından değerlendirilmelidir.",
        "level": 2
    },

    # ── Konjenital anomaliler ─────────────────────────────────────────────────
    {
        "id": "bulk2_congenital_1",
        "concept_id": "liver_caroli_disease",
        "type": "multiple_choice",
        "question": "Caroli hastalığı ile Caroli sendromu arasındaki fark nedir?",
        "options": [
            "Fark yok — aynı hastalık",
            "Caroli: saf intrahepatik safra yolu dilatasyonu. Caroli sendromu: + konjenital hepatik fibrozis ve portal hipertansiyon",
            "Caroli sendromu daha hafif",
            "Caroli hastalığı sadece yetişkinlerde"
        ],
        "correct": 1,
        "explanation": "Caroli hastalığı: sadece intrahepatik safra yolu kistik dilatasyonu. Caroli sendromu: Caroli hastalığı + konjenital hepatik fibrozis + portal hipertansiyon. Sendromda portal HT bulguları (splenomegali, varis) eşlik eder. Her ikisinde de intrahepatik taş ve kolanjit komplikasyonu, kolanjiyokarsinom riski mevcuttur.",
        "level": 2
    },

    # ── LI-RADS majör özellikler ──────────────────────────────────────────────
    {
        "id": "bulk2_lirads_major_1",
        "concept_id": "lirads_major_features_full",
        "type": "multiple_choice",
        "question": "LI-RADS'ta 'eşik büyüme' (threshold growth) kriteri nedir?",
        "options": [
            "6 ayda >%20 boyut artışı",
            "6 ayda >%50 boyut artışı (≤6 ay içinde)",
            "12 ayda >%100 boyut artışı",
            "1 ayda herhangi bir büyüme"
        ],
        "correct": 1,
        "explanation": "Eşik büyüme: ≤6 ayda ≥%50 boyut artışı. LI-RADS v2018 değişikliği: alt boyut sınırı kaldırıldı. Önceki versiyonda boyut ≥10 mm şartı vardı. Büyüme hem majör özellik (LR-5 katkısı) hem yardımcı özellik olarak kullanılabilir. Karşılaştırmalı görüntüleme zorunlu.",
        "level": 3
    },
    {
        "id": "bulk2_lirads_major_2",
        "concept_id": "lirads_major_features_full",
        "type": "multiple_choice",
        "question": "LI-RADS'ta enhancing kapsül ne anlama gelir?",
        "options": [
            "Arteryel fazda lezyon çevresinde rim",
            "Portal/geç fazda lezyon çevresinde düzgün ince enhancing yapı",
            "T2'de lezyon çevresinde parlak halka",
            "DWI'da lezyon çevresinde kısıtlama"
        ],
        "correct": 1,
        "explanation": "Enhancing kapsül: portal venöz veya geç fazda lezyon çevresinde düzgün, ince (<2 mm) enhancing yapı. Fibröz kapsül veya sıkıştırılmış karaciğer parankimini yansıtır. Arteryel fazda görünmeyebilir. Rim APHE ile karıştırılmamalı — rim APHE arteryel fazda periferden lezyon içine girişi gösterir ve LR-M kriteridir.",
        "level": 3
    },
    {
        "id": "bulk2_lirads_major_3",
        "concept_id": "lirads_major_features_full",
        "type": "multiple_choice",
        "question": "LI-RADS-TIV (tumor in vein) ne anlama gelir ve önemi nedir?",
        "options": [
            "Lezyon portal ven bitişiğinde",
            "Portal veya hepatik ven içinde arteryel enhancement gösteren tümör trombüsü — en az LR-5",
            "Venöz dönüş bozulması",
            "Portal ven basıncı artışı"
        ],
        "correct": 1,
        "explanation": "LR-TIV: portal ven veya hepatik ven içinde arteryel fazda enhancement gösteren dolma defekti. Tümör trombüsü arteryel kanlanma alır (bland trombüs almaz — bu kritik ayrım). LR-TIV kesin HKH tanısıdır ve BCLC C evresiyle uyumludur. Bland trombüs enhancement göstermez, Doppler'da akım yok.",
        "level": 3
    },

    # ── ICC ────────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_icc_1",
        "concept_id": "icc_full_criteria",
        "type": "multiple_choice",
        "question": "ICC'nin HKH'ya göre tedavideki temel farkı nedir?",
        "options": [
            "ICC için TACE kullanılır, HKH için kullanılmaz",
            "ICC'de karaciğer transplantasyonu endikasyonu yoktur — HKH'da Milan kriterleri ile transplant mümkün",
            "ICC sistemik kemoterapi gerektirmez",
            "HKH'da cerrahi yapılmaz"
        ],
        "correct": 1,
        "explanation": "ICC ve HKH tedavisi tamamen farklıdır. HKH: rezeksiyon, transplantasyon (Milan kriterleri), ablasyon, TACE, TARE. ICC: sadece cerrahi rezeksiyon küratif — transplantasyon standartta endike değil. İleri ICC: gemcitabin+sisplatin bazlı kemoterapi. Bu nedenle LR-M (ICC şüphesi) varsa biyopsi zorunlu.",
        "level": 3
    },
    {
        "id": "bulk2_icc_2",
        "concept_id": "icc_full_criteria",
        "type": "multiple_choice",
        "question": "ICC için hangi tümör markeri yükselmesi karakteristiktir?",
        "options": ["AFP", "CA 19-9 ve CEA", "PSA", "HER2"],
        "correct": 1,
        "explanation": "ICC'de CA 19-9 (>37 U/mL) ve CEA yükselmesi karakteristiktir. AFP genellikle normaldir — bu HKH'dan önemli bir ayırıcı özelliktir. AFP yüksekse kombine HKH-ICC veya HKH düşünülmeli. Biliyer obstrüksiyonda da CA 19-9 yükselebilir — klinik korelasyon şart.",
        "level": 3
    },

    # ── Kist karakterizasyon ──────────────────────────────────────────────────
    {
        "id": "bulk2_cyst_1",
        "concept_id": "cyst_characterization_full",
        "type": "multiple_choice",
        "question": "Komplike karaciğer kistinin basit kistten ayırımında en önemli bulgular nelerdir?",
        "options": [
            "Büyük boyut",
            "İnce septa veya duvar kalınlaşması, internal debris veya enhancement",
            "T2'de parlak sinyal",
            "Posterior akustik güçlenme"
        ],
        "correct": 1,
        "explanation": "Basit kist kriterleri: anekoik/su dansitesi + ince düzgün duvar + septa yok + enhancement yok. Bunların herhangi biri bozulursa komplike kist: septa kalınlaşması, mural nodül, internal debris, duvar enhancement. Komplike kist MR ile daha iyi değerlendirilir.",
        "level": 3
    },
    {
        "id": "bulk2_cyst_2",
        "concept_id": "cyst_characterization_full",
        "type": "multiple_choice",
        "question": "Hidatik kist için WHO CE sınıflamasında CE1 ne anlama gelir?",
        "options": [
            "İnaktif kalsifiye kist",
            "Aktif — tek kameralı, kız kesecik yok, uniform içerik",
            "Kız kesecikler var",
            "Membran dekolmanı"
        ],
        "correct": 1,
        "explanation": "WHO CE sınıflaması: CE1 = aktif, uniform içerik, kız kesecik yok. CE2 = aktif, kız kesecikler. CE3a = membran dekolmanı (su zambak işareti). CE3b = kız kesecikler + solid komponent. CE4-5 = inaktif/kalsifiye. CE1-2 tedavi gerektirir, CE4-5 takip yeterli olabilir.",
        "level": 3
    },

    # ── Apse ──────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_abscess_1",
        "concept_id": "liver_abscess_types",
        "type": "multiple_choice",
        "question": "Piyojenik karaciğer apsesinin en sık kaynağı nedir?",
        "options": [
            "Hematojen yol — bakteriyemi",
            "Biliyer yol — kolanjit (en sık)",
            "Direkt yayılım",
            "Portal yol — apandisit"
        ],
        "correct": 1,
        "explanation": "Piyojenik karaciğer apsesinin en sık kaynağı biliyer yoldur (kolanjit, safra yolu obstrüksiyonu). İkinci sırada portal yol (apandisit, divertikülit). Hematojen yol (bakteriyemi, endokardit) üçüncü sıradadır. Kriptojenik (kaynak bulunamayan) %20-30 oranında görülür.",
        "level": 3
    },
    {
        "id": "bulk2_abscess_2",
        "concept_id": "liver_abscess_types",
        "type": "multiple_choice",
        "question": "CEUS'ta karaciğer apsesinin karakteristik bulgusu nedir?",
        "options": [
            "Diffüz arteryel enhancement",
            "Honeycomb (bal peteği) görünümü + merkez avasküler + rim enhancement",
            "Flash fill",
            "Periferik nodüler enhancement"
        ],
        "correct": 1,
        "explanation": "CEUS'ta piyojenik apse: bal peteği (honeycomb) görünümü — multiloküler avasküler alanlar arasında ince enhancing septalar. Merkezi içerik avaskülerdir (nekroz/pü). Rim enhancement enflamatuar kapsülü gösterir. Bu patern solid tümörden ve hemanjiomdan ayırt eder.",
        "level": 3
    },

    # ── Ayırıcı tanı zincirleri ───────────────────────────────────────────────
    {
        "id": "bulk2_dd_hyper_1",
        "concept_id": "dd_hypervascular_lesion",
        "type": "multiple_choice",
        "question": "FNH'ı adenomdan en güvenilir şekilde ayırt eden MR bulgusu nedir?",
        "options": [
            "Boyut farkı",
            "Gadoxetat MR HBP: FNH hiperintens, adenom hipointens",
            "T2 sinyali",
            "Arteryel enhancement şiddeti"
        ],
        "correct": 1,
        "explanation": "Gadoxetat MR hepatobiliyer faz (HBP): FNH OATP1B3 eksprese eder → hiperintens veya izointens. Adenom OATP ekspresyonu bozuk → hipointens. Bu ayrım %95+ özgüllük sağlar. Diğer bulgular (APHE, T2) her ikisinde de benzerdir. Santral skar FNH'ya özgü ama her vakada görülmez.",
        "level": 4
    },
    {
        "id": "bulk2_dd_hyper_2",
        "concept_id": "dd_hypervascular_lesion",
        "type": "multiple_choice",
        "question": "RCC karaciğer metastazı ile HKH arasındaki en önemli klinik ayırım noktası nedir?",
        "options": [
            "Görüntüleme özellikleri farklı",
            "Klinik bağlam: siroz/HBV öyküsü → HKH, bilinen RCC → metastaz",
            "Boyut farkı",
            "AFP değeri her zaman ayırt eder"
        ],
        "correct": 1,
        "explanation": "RCC metastazı ve HKH benzer hipervasküler patern gösterebilir (APHE + washout). Ayırım için klinik bağlam kritik: siroz veya HBV öyküsü → HKH. Bilinen RCC + yeni karaciğer lezyonu → metastaz önce düşün. LI-RADS sadece HKH riskli hastalara uygulanır — RCC hastasına uygulanmaz.",
        "level": 4
    },

    # ── Tuzaklar ─────────────────────────────────────────────────────────────
    {
        "id": "bulk2_pitfall_1",
        "concept_id": "pitfall_hcc_mimics",
        "type": "multiple_choice",
        "question": "Sirozlu olmayan hastada 25 mm lezyon: APHE + washout. LI-RADS uygulanabilir mi?",
        "options": [
            "Evet, LR-5 olarak raporla",
            "Hayır — LI-RADS sadece riskli hastalara uygulanır. Hipervasküler primer veya sekonder tümör ayırımı biyopsi gerektirir",
            "LR-4 olarak raporla",
            "LR-M olarak raporla"
        ],
        "correct": 1,
        "explanation": "LI-RADS uygulanabilirlik: siroz, kronik HBV veya önceki HKH öyküsü. Siroz olmayan hastada sistem uygulanmaz. APHE + washout çeşitli tümörlerde (HKH, hipervasküler metastaz, adenom nadir) görülebilir. PPV çok düşük. Tanı için biyopsi gereklidir.",
        "level": 5
    },
    {
        "id": "bulk2_pitfall_2",
        "concept_id": "pitfall_focal_fat",
        "type": "multiple_choice",
        "question": "MR in-phase'de izointens, out-phase'de belirgin sinyal düşen 2 cm lezyon. Tanı?",
        "options": [
            "HKH — yağ içeriği tanısal",
            "Yağ içeren lezyon: adenom HNF-1α veya fokal yağlı infiltrasyon",
            "Metastaz — yağ sık görülür",
            "Basit kist"
        ],
        "correct": 1,
        "explanation": "Out-phase'de sinyal düşümü = lezyon içi yağ. Karaciğer lezyonlarında yağ: adenom HNF-1α subtipi (sık), bazı HKH (yağlı metamorfoz) veya fokal yağlı infiltrasyon (lezyon değil). Klinik bağlam: genç kadın + OKS → adenom HNF-1α. Sirozlu hasta → HKH içi yağ. Fokal yağlı infiltrasyon: düzensiz sınır, damarları itmez.",
        "level": 5
    },
    {
        "id": "bulk2_pitfall_3",
        "concept_id": "pitfall_mri_artifacts",
        "type": "multiple_choice",
        "question": "MR'da hepatik vende dolma defekti görülüyor. Trombüs veya flow artifact ayırımı nasıl yapılır?",
        "options": [
            "Boyuta bakılır",
            "Farklı sekans veya faz görüntüleri: gerçek trombüs tüm sekanslarda tutarlı, flow artifact değişken",
            "Enhancement bakılır — trombüs kontrast almaz",
            "Klinik bulgulara göre karar verilir"
        ],
        "correct": 1,
        "explanation": "Flow artifact (hareket artefaktı): kan akımının faz kodlamasındaki aritmiler nedeniyle hayalet sinyal. Farklı sekanslarda değişir, farklı eksenlerde kaybolabilir. Gerçek trombüs: tüm sekanslarda tutarlı dolma defekti, Doppler'da akım yokluğu. Kontrast sonrası — bland trombüs enhancement almaz, tümör trombüsü (HKH) enhancement alır.",
        "level": 5
    },

    # ── Multimodal ───────────────────────────────────────────────────────────
    {
        "id": "bulk2_multimodal_1",
        "concept_id": "multimodal_reporting_structured",
        "type": "multiple_choice",
        "question": "LR-5 lezyon için raporda önerilen aksiyon nedir?",
        "options": [
            "Biyopsi zorunlu",
            "6 ayda takip yeterli",
            "MDT tartışması — BCLC evreleme, tedavi planlaması",
            "Hemen cerrahi"
        ],
        "correct": 2,
        "explanation": "LR-5 = kesin HKH (>%95 PPV). Biyopsi bu grupta gerekmez — görüntüleme tanı koyar. Ancak tedavi BCLC evresine göre belirlenir. MDT (hepatoloji + onkoloji + cerrahi + girişimsel radyoloji) tartışması gereklidir. Radyolog raporda MDT'ye gönderme önerisini açıkça belirtmeli.",
        "level": 6
    },
    {
        "id": "bulk2_multimodal_2",
        "concept_id": "multimodal_treatment_response",
        "type": "multiple_choice",
        "question": "mRECIST'e göre karaciğer tümör yanıtı nasıl ölçülür?",
        "options": [
            "Toplam tümör çapı ölçülür",
            "Sadece arteryel fazda enhancement gösteren canlı tümör alanı ölçülür",
            "T2 sinyali ölçülür",
            "DWI ADC değeri ölçülür"
        ],
        "correct": 1,
        "explanation": "mRECIST (modified RECIST): sadece enhancing (canlı) tümör komponenti ölçülür. Nekrotik alanlar dahil edilmez. Bu RECIST 1.1'den farklıdır — geleneksel RECIST tüm tümör çapını ölçer. Ablasyon veya TACE sonrası tümör toplam boyutu küçülmese bile canlı komponent azalıyorsa yanıt var demektir.",
        "level": 6
    },
    {
        "id": "bulk2_multimodal_3",
        "concept_id": "multimodal_surveillance_strategy",
        "type": "multiple_choice",
        "question": "HKH surveyansında US'nin en önemli kısıtlaması nedir?",
        "options": [
            "Radyasyon maruziyeti",
            "Operatör bağımlılığı + obezite/gaz nedeniyle %25-40 yetersiz görüntüleme",
            "Kontrast gerektirmesi",
            "Yüksek maliyet"
        ],
        "correct": 1,
        "explanation": "US HKH surveyansında en kısıtlayan faktörler: operatör bağımlılığı ve obezite/gaz nedeniyle yetersiz karaciğer görüntüleme. VIS-C (vizualizasyon skoru) yetersiz ise US güvenilmez. Bu hastalarda abbreviated MRI (non-kontrast T1+DWI) tercih edilmelidir. US duyarlılığı erken HKH için %45-65.",
        "level": 6
    },

    # ── Post-op tuzaklar ──────────────────────────────────────────────────────
    {
        "id": "bulk2_postop_1",
        "concept_id": "pitfall_post_op_liver",
        "type": "multiple_choice",
        "question": "Post-ablasyon 1. ay MR'da ablasyon zonu boyutu işlemden büyük görünüyor. Bu ne anlama gelir?",
        "options": [
            "Nüks — retreatment gerekli",
            "Beklenen — erken post-ablasyon ödemi ablasyon zonunu büyük gösterir",
            "Komplikasyon",
            "Yetersiz ablasyon"
        ],
        "correct": 1,
        "explanation": "Post-ablasyon erken dönemde (ilk 1 ay) ablasyon zonu ödem nedeniyle gerçek ablasyon alanından büyük görünür. Bu normaldir. Boyut için güvenilir değerlendirme 4-8 haftada yapılmalıdır. Nüks: ablasyon zonu içinde veya sınırında yeni nodüler arteryel enhancement.",
        "level": 5
    },

    # ── Radyasyon hasarı ──────────────────────────────────────────────────────
    {
        "id": "bulk2_radiation_1",
        "concept_id": "pitfall_radiation_liver",
        "type": "multiple_choice",
        "question": "SBRT sonrası karaciğerde geometrik şekilli (küresel/silindirik) enhancement alanı görülüyor. Yorum?",
        "options": [
            "Tümör progresyonu",
            "Yeni metastaz",
            "Radyasyon etkisi — tedavi portu içinde beklenen parankimal değişiklik",
            "Apse"
        ],
        "correct": 2,
        "explanation": "SBRT sonrası radyasyon etki alanı geometrik (tedavi portu şeklinde) sınırlı enhancement + T2 değişikliği gösterir. Tümör veya metastaz anatomik sınırları takip etmez. Bu 'radyasyon etkisi' beklenen bulgudur — progresyon değil. Önceki tedavi planı ile korelasyon yapılmalı.",
        "level": 5
    },

    # ── Y90 ────────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_y90_1",
        "concept_id": "multimodal_y90_imaging",
        "type": "multiple_choice",
        "question": "Y-90 TARE öncesi neden Tc-99m MAA sintigrafisi yapılır?",
        "options": [
            "Karaciğer fonksiyonunu ölçmek için",
            "Akciğer şantını ölçmek — yüksek şant Y90'ın akciğere gitmesine neden olur",
            "Tümör beslenme damarını bulmak için",
            "Portal ven anatomisini görmek için"
        ],
        "correct": 1,
        "explanation": "MAA (makroagregate albumin) sintigrafisi Y90 tedavi öncesi yapılır. Amacı: hepatopulmoner şant oranını ölçmek. Şant yüksekse (%>20) Y90 mikrosfereleri akciğere gider → radyasyon pnömonisi. Bu durumda doz azaltılır veya tedavi iptal edilir. Ayrıca tümör tutulumunu ve hepatik doz dağılımını öngörmek için kullanılır.",
        "level": 6
    },

    # ── Klatskin tümörü ───────────────────────────────────────────────────────
    {
        "id": "bulk2_klatskin_1",
        "concept_id": "dd_biliary_dilation_algorithm",
        "type": "multiple_choice",
        "question": "Hilar kolanjiyokarsinomda en iyi rezektabilite değerlendirmesi hangi modalite ile yapılır?",
        "options": [
            "US Doppler",
            "MDCT + MRCP kombinasyonu — vasküler invazyon ve biliyer tutulum",
            "Sadece MRCP",
            "PET-BT"
        ],
        "correct": 1,
        "explanation": "Klatskin tümöründe rezektabilite değerlendirmesi: (1) MDCT — vasküler invazyon (hepatik arter, portal ven), lenfadenopati, ekstrahepatik yayılım, (2) MRCP — biliyer tutulum haritası, Bismuth-Corlette sınıflaması. İkisi birlikte kullanıldığında doğruluk artar. Biliyer drenaj GÖRÜNTÜLEME SONRASI yapılmalı — drenaj görüntüyü bozar.",
        "level": 4
    },

    # ── EHE ──────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_ehe_2",
        "concept_id": "dd_multiple_lesions",
        "type": "multiple_choice",
        "question": "Anjiyosarkomun görüntülemede hemanjiomdan nasıl ayrılır?",
        "options": [
            "Boyutu daha büyük",
            "Anjiyosarkom: hızlı büyüme + kanama + DWI kısıtlama + bilinen risk faktörü (thorotrast, PVC maruziyeti). Hemanjiom: yavaş seyir, T2 ampul bulb",
            "Enhancement paterni aynı",
            "Her ikisi de HBP hipointens"
        ],
        "correct": 1,
        "explanation": "Anjiyosarkom nadir ama agresif. Hızlı büyüyen multipl karaciğer lezyonları + kanama içeriği + DWI kısıtlama hemanjiomdan farklıdır. Risk faktörleri: thorotrast (eski kontrast ajan), vinil klorid maruziyeti, arsenik. T2 ampul bulb işareti anjiyosarkomda görülmez. Tanı biyopsi ile.",
        "level": 4
    },

    # ── PSK ───────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_psc_1",
        "concept_id": "dd_jaundice_algorithm",
        "type": "multiple_choice",
        "question": "Primer sklerozan kolanjitte MRCP'de ne görülür?",
        "options": [
            "Fokal tek striktür",
            "Boncuk dizisi görünümü — multi-fokal striktür ve dilatasyon, intra+ekstrahepatik",
            "Normal safra yolları",
            "Sadece ekstrahepatik dilatasyon"
        ],
        "correct": 1,
        "explanation": "PSK MRCP bulgusu: 'boncuk dizisi' (beaded appearance) — multifokal striktür ve dilatasyon alanları intra ve ekstrahepatik safra yollarında. Diffüz, bilateral, simetrik tutulum karakteristiktir. Fokal asimetrik tutulum kolanjiyokarsinom açısından şüphelidir — PSK'da CCA riski %10-15.",
        "level": 4
    },
    {
        "id": "bulk2_psc_2",
        "concept_id": "dd_jaundice_algorithm",
        "type": "multiple_choice",
        "question": "IgG4 ilişkili kolanjit PSK'dan nasıl ayrılır?",
        "options": [
            "Görüntüleme ile ayrım mümkün değil — her ikisi de aynı",
            "IgG4: serum IgG4 >2 kat normalin üzerinde, steroid yanıtı, pancreas tutulumu. PSK: IBD ilişkili, CA 19-9 yüksek, steroid yanıtı yok",
            "IgG4 sadece gençlerde",
            "PSK sadece erkeklerde"
        ],
        "correct": 1,
        "explanation": "IgG4 ilişkili kolanjit steroidlere dramatik yanıt verir — bu ayırıcı özelliğiyle PSK'dan ayrılır. Serum IgG4 yüksekliği (>135 mg/dL) ve pankreas tutulumu (otoimmün pankreatit) IgG4'e işaret eder. PSK ile inflamatuar barsak hastalığı ilişkisi güçlüdür. ERCP biyopsisi veya steroid trial ayırımda kullanılabilir.",
        "level": 4
    },

    # ── NASH ─────────────────────────────────────────────────────────────────
    {
        "id": "bulk2_nash_1",
        "concept_id": "liver_fatty_infiltration",
        "type": "multiple_choice",
        "question": "NASH (non-alkolik steatohepatit) ile basit steatoz arasındaki görüntüleme farkı nedir?",
        "options": [
            "NASH her zaman daha fazla yağ içerir",
            "Görüntüleme ile güvenilir ayrım yapılamaz — NASH tanısı biyopsi gerektirir",
            "NASH'ta kalsifikasyon görülür",
            "NASH'ta T2 parlak lezyon olur"
        ],
        "correct": 1,
        "explanation": "Basit steatoz ve NASH görüntülemede benzer bulgu gösterir — her ikisinde de yağlı infiltrasyon. NASH tanısı biyopside inflamasyon + hepatosit hasarı + fibrozis birlikteliği gerektirir. MR elastografi fibrozis evrelendirmesinde giderek daha fazla kullanılmaktadır ama tanı koydurmaz. Klinik + laboratuvar + görüntüleme + gerekirse biyopsi.",
        "level": 2
    },

    # ── Budd-Chiari ───────────────────────────────────────────────────────────
    {
        "id": "bulk2_bc_1",
        "concept_id": "liver_budd_chiari",
        "type": "multiple_choice",
        "question": "Budd-Chiari sendromunda BT'de karaciğerin enhancement paterni nasıldır?",
        "options": [
            "Homojen uniform enhancement",
            "Flip-flop paterni: akut fazda santral erken enhance, periferik geç enhance",
            "Sadece kaudat lob enhances",
            "Hiç enhancement yok"
        ],
        "correct": 1,
        "explanation": "Budd-Chiari akut BT paterni: santral karaciğer (kaudat lob çevresi) erken artyeriel fazda enhance olurken periferik bölgeler geç faza kadar düşük yoğunlukta kalır. Bu 'flip-flop' paterni karakteristiktir — periferik venöz dönüşün engellenmesi nedeniyle periferik bölgeler kontrast tutamaz. Kronik fazda kaudat hipertrofisi dominant bulgudur.",
        "level": 2
    },

    # ── Periportal izlenme ────────────────────────────────────────────────────
    {
        "id": "bulk2_periportal_1",
        "concept_id": "pitfall_periportal_tracking",
        "type": "multiple_choice",
        "question": "Akut hepatitte periportal ödem neden oluşur?",
        "options": [
            "Portal ven trombozu",
            "Hepatosit şişmesi + lenfatik dilatasyon — portal triad çevresinde sıvı",
            "Karaciğer kanaması",
            "Kontrast madde ekstravazasyonu"
        ],
        "correct": 1,
        "explanation": "Akut viral hepatit veya ilaç reaksiyonunda hepatosit şişmesi + inflamasyon → portal triad çevresinde lenfatik dilatasyon ve ödem. US'de periportal hiperekojenisite (yıldız işareti paterni), BT'de periportal düşük dansite görülür. Laserasyon veya patolojik sıvı değil — klinik bağlamla ayrılır.",
        "level": 5
    },
]

# ── SEED FONKSİYONLARI ────────────────────────────────────────────────────────

def seed_concepts(tx, concepts):
    for c in concepts:
        tx.run("""
            MERGE (c:Concept {id:$id})
            SET c.name=$name, c.organ=$organ, c.level=$level,
                c.category=$category, c.summary=$summary,
                c.why_matters=$why_matters, c.key_points=$key_points,
                c.source=$source
        """, **{k: v for k, v in c.items()})
    return len(concepts)

def seed_prerequisites(tx, prereqs):
    for p in prereqs:
        tx.run("""
            MATCH (c1:Concept {id:$from_id})
            MATCH (c2:Concept {id:$to_id})
            MERGE (c1)-[:PREREQUISITE_OF]->(c2)
        """, from_id=p["from"], to_id=p["to"])
    return len(prereqs)

def seed_concept_diagnosis(tx, items):
    for cd in items:
        tx.run("""
            MATCH (c:Concept {id:$concept_id})
            MATCH (d:Diagnosis {id:$diagnosis_id})
            MERGE (c)-[:RELATES_TO {relation:$relation}]->(d)
        """, concept_id=cd["concept"], diagnosis_id=cd["diagnosis"], relation=cd["relation"])
    return len(items)

def seed_questions(tx, questions):
    for q in questions:
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
    return len(questions)

print("\n── Katman 5 ek conceptler yükleniyor...")
all_concepts = CONCEPTS_L5 + CONCEPTS_L6
all_prereqs  = PREREQUISITES_L5 + PREREQUISITES_L6
with driver.session() as session:
    n = session.execute_write(seed_concepts, all_concepts)
    print(f"✓ {n} Concept")
with driver.session() as session:
    n = session.execute_write(seed_prerequisites, all_prereqs)
    print(f"✓ {n} PREREQUISITE_OF")
with driver.session() as session:
    n = session.execute_write(seed_concept_diagnosis, CONCEPT_DIAGNOSIS)
    print(f"✓ {n} RELATES_TO")
with driver.session() as session:
    n = session.execute_write(seed_questions, QUESTIONS)
    print(f"✓ {n} Question")

driver.close()
print(f"""
✓ Tamamlandı:
  Yeni Concepts : {len(all_concepts)} (L5: {len(CONCEPTS_L5)}, L6: {len(CONCEPTS_L6)})
  Yeni Sorular  : {len(QUESTIONS)}
""")

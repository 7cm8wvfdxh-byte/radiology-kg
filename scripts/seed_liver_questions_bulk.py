from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

# ── TOPLU SORU HAVUZU — Her concept için 3-5 soru ─────────────────────────────
# Mevcut soru ID'leri ile çakışmayacak şekilde "bulk_" prefix kullanıldı

QUESTIONS = [

    # ── ANATOMİ VE FİZYOLOJİ ─────────────────────────────────────────────────

    {
        "id": "bulk_segment_couinaud_1",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Couinaud sınıflamasına göre kaudat lob hangi segmenttir?",
        "options": ["Segment II", "Segment I", "Segment IV", "Segment VIII"],
        "correct": 1,
        "explanation": "Segment I = kaudat lob. Anatomik olarak özgündür — hepatik venlerden bağımsız olarak doğrudan IVC'ye drene olur. Bu nedenle Budd-Chiari'de diğer segmentler atrofik olurken kaudat kompansatuvar büyür.",
        "level": 1
    },
    {
        "id": "bulk_segment_couinaud_2",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Safra kesesinin hemen solunda, orta hepatik ven ile falciform ligament arasındaki segment hangisidir?",
        "options": ["Segment III", "Segment V", "Segment IV", "Segment II"],
        "correct": 2,
        "explanation": "Segment IV = kare lob (quadrate lobe). Falciform ligament ile orta hepatik ven arasında, safra kesesinin solunda yer alır. Segment IVa (üst) ve IVb (alt) olarak ikiye ayrılır.",
        "level": 1
    },
    {
        "id": "bulk_segment_couinaud_3",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Sağ lobu ön ve arka segmentlere bölen hepatik ven hangisidir?",
        "options": ["Sol hepatik ven", "Orta hepatik ven", "Sağ hepatik ven", "Aksesuar hepatik ven"],
        "correct": 2,
        "explanation": "Sağ hepatik ven sağ lobu ön (Segment V, VIII) ve arka (Segment VI, VII) olarak böler. Orta hepatik ven sağ ve sol lobu böler (Cantlie hattı). Sol hepatik ven sol lobu Segment II ve III'e böler.",
        "level": 1
    },

    # ── VASKÜLER ANATOMİ ──────────────────────────────────────────────────────

    {
        "id": "bulk_vasculature_1",
        "concept_id": "liver_anatomy_vasculature",
        "type": "multiple_choice",
        "question": "Normal karaciğerde portal ven karaciğer kanlanmasının yüzde kaçını sağlar?",
        "options": ["%25-30", "%50-60", "%70-75", "%90-95"],
        "correct": 2,
        "explanation": "Karaciğer çift kanlanır: portal ven %70-75, hepatik arter %25-30. Bu denge HKH'nın patofiziyolojisini açıklar — HKH'da arteryel kanlanma dominante döner (%80-100 arteryel), bu yüzden arteryel fazda parlaklaşır.",
        "level": 1
    },
    {
        "id": "bulk_vasculature_2",
        "concept_id": "liver_anatomy_vasculature",
        "type": "multiple_choice",
        "question": "Portal ven hangi iki venin birleşmesiyle oluşur?",
        "options": [
            "Splenik ven + inferior vena cava",
            "Superior mezenterik ven + splenik ven",
            "İnferior mezenterik ven + hepatik ven",
            "Splenik ven + renal ven"
        ],
        "correct": 1,
        "explanation": "Portal ven = superior mezenterik ven + splenik ven birleşimi. İnferior mezenterik ven çoğunlukla splenik vene dökülür. Bu anatomik ilişki portal hipertansiyon gelişimini ve kollateral yolları belirler.",
        "level": 1
    },

    # ── HİSTOLOJİ ─────────────────────────────────────────────────────────────

    {
        "id": "bulk_histology_1",
        "concept_id": "liver_histology_hepatocyte",
        "type": "multiple_choice",
        "question": "Kupffer hücreleri nerede bulunur ve görevi nedir?",
        "options": [
            "Portal triad içinde, safra üretir",
            "Sinüzoid duvarında, makrofaj işlevi görür",
            "Disse aralığında, yağ depolar",
            "Santral vende, kan filtreler"
        ],
        "correct": 1,
        "explanation": "Kupffer hücreleri karaciğer sinüzoidlerini döşeyen özelleşmiş makrofajlardır. Bakteri, artık kan hücreleri ve toksinleri fagosite ederler. İmmün yanıt ve inflamasyonda kritik rol oynarlar. Aşırı aktivasyonları karaciğer hasarına katkıda bulunabilir.",
        "level": 1
    },
    {
        "id": "bulk_histology_2",
        "concept_id": "liver_histology_lobule",
        "type": "multiple_choice",
        "question": "Disse aralığı nedir ve radyolojik önemi nedir?",
        "options": [
            "Portal triad ile hepatosit arasındaki boşluk — safra akar",
            "Sinüzoid endoteli ile hepatosit arasındaki boşluk — lenfatik sıvı ve hepatik stellat hücreler",
            "Hepatosit ile santral ven arasındaki boşluk",
            "Safra kanalikülü ile portal ven arasındaki boşluk"
        ],
        "correct": 1,
        "explanation": "Disse aralığı sinüzoid endoteli ile hepatosit arasındadır. Lenfatik sıvıyı taşır ve hepatik stellat hücreler (İto hücreleri) burada bulunur. Siroz gelişiminde İto hücreleri aktive olur ve kollajen üretir → fibrozis. Periportal ödem görüntülemede bu aralığın genişlemesini yansıtır.",
        "level": 1
    },

    # ── KONTRAST FARMAKOLOJİSİ ────────────────────────────────────────────────

    {
        "id": "bulk_contrast_iodinated_1",
        "concept_id": "liver_contrast_iodinated",
        "type": "multiple_choice",
        "question": "İyotlu kontrast madde böbrek yetmezliğinde nasıl davranır?",
        "options": [
            "Karaciğerden metabolize edilir",
            "Yarı ömrü uzar, haftalar içinde atılır",
            "Böbrekten hızla atılır — problem değil",
            "Akciğerden atılır"
        ],
        "correct": 1,
        "explanation": "Normal böbrek fonksiyonunda yarı ömür 90-120 dk. Renal yetmezlikte glomerüler filtrasyon azaldığından yarı ömür uzar — haftalar sürebilir. Bu nedenle renal yetmezlikte kontrast kararı dikkatli verilmeli. Kontrast nefropati riski abartılmış olmakla birlikte ağır yetmezlikte dikkat gerekir.",
        "level": 1
    },
    {
        "id": "bulk_contrast_gadolinium_1",
        "concept_id": "liver_contrast_gadolinium",
        "type": "multiple_choice",
        "question": "Gadoxetat (Primovist) hangi taşıyıcı proteinler aracılığıyla hepatositlerce alınır?",
        "options": [
            "GLUT2 — glukoz taşıyıcısı",
            "OATP1B1 ve OATP1B3 — organik anyonik taşıyıcılar",
            "MRP2 — multidrug resistance proteini",
            "P-glikoprotein — efluks pompası"
        ],
        "correct": 1,
        "explanation": "Gadoxetat OATP1B1 ve OATP1B3 (Organic Anion Transporting Polypeptide) taşıyıcılarıyla hepatositlerce alınır. Bu taşıyıcılar HKH ve adenomda bozuk çalışır → HBP hipointens. FNH'da işlevsel → HBP hiperintens. Bu mekanizma MR ile doku karakterizasyonunun temelidir.",
        "level": 2
    },

    # ── MR FİZİK ─────────────────────────────────────────────────────────────

    {
        "id": "bulk_mr_physics_1",
        "concept_id": "mr_physics_t1_t2",
        "type": "multiple_choice",
        "question": "T1'de hiperintens görünen karaciğer lezyonunda hangi içerik düşünülür?",
        "options": [
            "Serbest su — kist",
            "Yağ, kanama (methemoglobin) veya proteinöz içerik",
            "Fibröz doku",
            "Kalsifikasyon"
        ],
        "correct": 1,
        "explanation": "T1 hiperintensitesi: yağ (kimyasal kayma ile konfirme), kanama (methemoglobin kısa T1 — subakut kanama), proteinöz içerik (apse, musinöz tümör). Kalsifikasyon T1'de sinyal vermez. Serbest su uzun T1 — T1'de koyu. Adenom HNF-1α ve bazı HKH T1 hiperintens yağ içerebilir.",
        "level": 1
    },
    {
        "id": "bulk_mr_physics_2",
        "concept_id": "mr_physics_t1_t2",
        "type": "multiple_choice",
        "question": "STIR sekansının amacı nedir?",
        "options": [
            "Yağ sinyalini artırmak",
            "Yağ sinyalini baskılamak — yağ içermeyen T2 parlak lezyonları vurgulamak",
            "Kontrast tutulumunu ölçmek",
            "Difüzyonu ölçmek"
        ],
        "correct": 1,
        "explanation": "STIR (Short Tau Inversion Recovery) yağ baskılama tekniğidir. Yağın T1 null noktasında görüntü alınır. Yağ dokusu sinyal vermez, yağ içermeyen T2 parlak yapılar (ödem, tümör, enflamasyon) ise parlak görünür. Karaciğerde yağlı alanlarda lezyonları daha iyi görmek için kullanılır.",
        "level": 1
    },

    # ── BT FİZİK ─────────────────────────────────────────────────────────────

    {
        "id": "bulk_ct_physics_1",
        "concept_id": "ct_physics_hu",
        "type": "multiple_choice",
        "question": "BT'de yağlı karaciğerin en güvenilir kriteri hangisidir?",
        "options": [
            "Karaciğer dansitesi <60 HU",
            "Karaciğer dansitesi dalak dansitesinden >10 HU düşük",
            "Karaciğer homojen görünüm",
            "Portal venin görünmemesi"
        ],
        "correct": 1,
        "explanation": "Karaciğer-dalak dansite farkı >10 HU (KC < Dalak) steatozun en güvenilir BT kriteri. Mutlak değer (<40 HU) de kullanılır ama dansite farkı daha tutarlı. Kontrast sonrası değerlendirme güvenilmez — natif BT şart.",
        "level": 1
    },
    {
        "id": "bulk_ct_physics_2",
        "concept_id": "ct_physics_hu",
        "type": "multiple_choice",
        "question": "Spontan hiperdens (natif BT'de yüksek HU) karaciğer lezyonu hangi içeriği akla getirir?",
        "options": [
            "Su içeriği — basit kist",
            "Hava içeriği — apse",
            "Akut kanama, kalsifikasyon veya yoğun protein",
            "Yağ infiltrasyonu"
        ],
        "correct": 2,
        "explanation": "Natif BT'de karaciğer parankiminden daha yoğun lezyon: akut kanama (hemoglobin — 40-70 HU), kalsifikasyon (>100 HU), amiodarone birikimi (ilaç içinde iyot) veya yoğun protein. Kist ve yağ düşük HU gösterir. Spontan hiperdensite önemli bir ipucu — kontrastsız BT bu yüzden değerlidir.",
        "level": 1
    },

    # ── US FİZİK ─────────────────────────────────────────────────────────────

    {
        "id": "bulk_us_physics_1",
        "concept_id": "us_physics_liver",
        "type": "multiple_choice",
        "question": "Posterior akustik güçlenme neden oluşur ve ne zaman görülür?",
        "options": [
            "Ses dalgaları yoğun yapıda tamamen absorbe olur",
            "Sıvı ses dalgalarını zayıflatmadan geçirir, arkadaki yapı daha parlak görünür",
            "Yüksek frekanslı ses dalgaları derin yapılarda yansır",
            "Doppler akımı olan yapılarda oluşur"
        ],
        "correct": 1,
        "explanation": "Sıvı dolu yapılar (kist, mesane, safra kesesi) ses dalgalarını absorbe etmeden geçirir. Arkadaki doku normal doku kadar ses aldığı halde üstten gelen ses daha az absorbsiyon yaşadığından arka duvar ve arka yapılar daha parlak görünür. Bu basit kist tanısında kritik bulgu.",
        "level": 1
    },

    # ── ENZİM TESTLERİ ────────────────────────────────────────────────────────

    {
        "id": "bulk_lab_1",
        "concept_id": "liver_lab_tests",
        "type": "multiple_choice",
        "question": "ALP ve GGT yüksek, AST/ALT normal — hangi patoloji düşünülür?",
        "options": [
            "Viral hepatit",
            "İskemik hepatit",
            "Biliyer obstrüksiyon veya infiltratif hastalık",
            "Alkolik hepatit"
        ],
        "correct": 2,
        "explanation": "ALP ve GGT biliyer obstrüksiyon ve infiltratif hastalıklarda (sarkoidoz, lenfoma, metastaz) yükselir. AST/ALT hepatosit hasarını gösterir — bunlar normal ise hepatoselüler nekroz yok. Safra yolu hastalığında görüntülemede dilatasyon veya kitle aranır.",
        "level": 1
    },
    {
        "id": "bulk_lab_2",
        "concept_id": "liver_lab_tests",
        "type": "multiple_choice",
        "question": "AFP >200 ng/mL olan sirozlu hastada LR-4 lezyon var. Yönetim?",
        "options": [
            "Takip — LR-4 yeterince yüksek risk değil",
            "AFP anlamlı yardımcı özellik — MDT tartışması ve biyopsi değerlendirmesi",
            "LR-5'e upgrade — biyopsisiz tedavi başla",
            "AFP yüksekliği bu vakada anlamsız"
        ],
        "correct": 1,
        "explanation": "LI-RADS 2024: AFP >200 ng/mL yardımcı özellik olarak tanımlandı. LR-4 + AFP >200 = kuvvetli HKH şüphesi → MDT tartışması ve biyopsi değerlendirmesi. Ancak yardımcı özellik LR-5'e yükseltemez. AFP tek başına tanı koydurmaz — %30-40 HKH AFP üretmez.",
        "level": 2
    },

    # ── PORTAL HİPERTANSİYON ──────────────────────────────────────────────────

    {
        "id": "bulk_portal_ht_1",
        "concept_id": "portal_hypertension",
        "type": "multiple_choice",
        "question": "Portal hipertansiyonun klinik olarak anlamlı eşiği nedir?",
        "options": [">5 mmHg", ">10 mmHg", ">20 mmHg", ">15 mmHg"],
        "correct": 1,
        "explanation": "Normal portal venöz basınç <5 mmHg. Klinik anlamlı portal HT >10 mmHg. Bu eşiğin üzerinde varis gelişimi, asit ve diğer komplikasyonlar ortaya çıkar. HVPG (hepatik venöz basınç gradiyenti) ölçümü altın standarttır.",
        "level": 2
    },
    {
        "id": "bulk_portal_ht_2",
        "concept_id": "portal_hypertension",
        "type": "multiple_choice",
        "question": "US Doppler'da hepatofugal portal akım ne anlama gelir?",
        "options": [
            "Normal portal akım",
            "Hız artmış portal akım",
            "Kan karaciğerden uzaklaşıyor — ağır portal hipertansiyon işareti",
            "Arteriyel akım ile karışma"
        ],
        "correct": 2,
        "explanation": "Normal portal akım hepatopetaldir — karaciğere doğru. Hepatofugal akım (karaciğerden uzak) ciddi portal hipertansiyonun işaretidir. Kan artık normal yoldan karaciğere giremez, ters yönde kollateral yollardan gider. Bu Doppler bulgusu karaciğer transplantasyonu değerlendirmesinde önemlidir.",
        "level": 2
    },

    # ── SİROZ ────────────────────────────────────────────────────────────────

    {
        "id": "bulk_cirrhosis_1",
        "concept_id": "liver_cirrhosis_imaging",
        "type": "multiple_choice",
        "question": "Sirozlu karaciğerde siderotik nodüllerin T2'deki görünümü ve HKH'dan farkı nedir?",
        "options": [
            "T2 parlak — HKH gibi",
            "T2 koyu (hipointens) — demir birikimi susceptibility artefaktı",
            "T2 izointens — fark yok",
            "T2 heterojen — ayırım yapılamaz"
        ],
        "correct": 1,
        "explanation": "Siderotik nodüller demir biriktirdiğinden T2'de koyu (hipointens) görünür. HKH ise T2'de hafif hiperintenstir. Bu kritik ayrım: T2'de koyu nodül = siderotik/rejenerasyon nodülü = benign. T2 sinyali artarsa → HKH'ya dönüşüm şüphesi → LI-RADS değerlendirme.",
        "level": 2
    },
    {
        "id": "bulk_cirrhosis_2",
        "concept_id": "liver_cirrhosis_imaging",
        "type": "multiple_choice",
        "question": "Sirozun Child-Pugh skoru hangi parametrelerden oluşur?",
        "options": [
            "AFP, ALT, AST, bilirubin, albumin",
            "Bilirubin, albumin, PT, asit, ensefalopati",
            "AFP, ALT, portal basınç, asit, varis",
            "Bilirubin, GGT, ALP, albumin, PT"
        ],
        "correct": 1,
        "explanation": "Child-Pugh skoru 5 parametre: bilirubin, albumin, PT/INR, asit (yok/hafif/ciddi) ve ensefalopati (yok/grade 1-2/grade 3-4). A (5-6 puan): iyi rezerv. B (7-9): orta. C (10-15): kötü. BCLC tedavi algoritmasında karaciğer fonksiyonu bu skorla değerlendirilir.",
        "level": 2
    },

    # ── SİSTEMATİK OKUMA ─────────────────────────────────────────────────────

    {
        "id": "bulk_systematic_1",
        "concept_id": "liver_systematic_reading",
        "type": "multiple_choice",
        "question": "Karaciğer BT raporunda fokal lezyon tanımlanırken hangi bilgi mutlaka verilmeli?",
        "options": [
            "Sadece boyut yeterli",
            "Segment, boyut, enhancement paterni ve LI-RADS kategorisi (riskli hastada)",
            "Sadece LI-RADS kategorisi",
            "Tanı kesin ise detay gereksiz"
        ],
        "correct": 1,
        "explanation": "Standart raporlama: (1) Segment lokalizasyonu (cerrahi planlama), (2) Boyut (evreleme, takip), (3) Enhancement paterni (tanı), (4) LI-RADS kategorisi (riskli hastada, standart terminoloji), (5) Öneri. Bu bilgilerin eksikliği klinisyen için işlevsiz rapor demektir.",
        "level": 2
    },

    # ── KONTRAST DİNAMİĞİ ────────────────────────────────────────────────────

    {
        "id": "bulk_contrast_dynamics_1",
        "concept_id": "contrast_dynamics_interactive",
        "type": "multiple_choice",
        "question": "Hemanjiomun fill-in paterni neden oluşur?",
        "options": [
            "Aktif tümör vaskülarizasyonu kontrast doldurur",
            "Periferden başlayan kontrast yavaş yavaş merkeze ilerler — yavaş kan havuzu",
            "Santral nekroz kontrast tutar",
            "Fibröz stroma geç fazda enhancement yapar"
        ],
        "correct": 1,
        "explanation": "Hemanjiom düzensiz, geniş vasküler kanallardan oluşur. Kontrast arteryel fazda önce periferik büyük damarlara (nodüler enhancement) girer, sonra merkeze doğru ilerler (fill-in). Kan hareketi yavaş olduğu için bu dolum geç fazda tamamlanır. Periferden merkeze ilerleyen bu patern hemanjiomun karakteristik özelliğidir.",
        "level": 2
    },
    {
        "id": "bulk_contrast_dynamics_2",
        "concept_id": "contrast_dynamics_interactive",
        "type": "multiple_choice",
        "question": "ICC'de geç fazda neden persistan enhancement görülür?",
        "options": [
            "Tümör hipervaskülerdir",
            "Fibröz stroma interstitisyel boşluğa kontrast biriktirir ve yavaş yıkar",
            "Wash-out mekanizması yoktur ICC'de",
            "Tümör nekrozu kontrast tutar"
        ],
        "correct": 1,
        "explanation": "ICC'de fibröz stroma hakimdir. Ekstraselüler gadolinyum/iyot interstitisyel alanda birikir ve fibröz dokuda yavaş yıkanır. Bu nedenle portal ve geç fazda persistan enhancement görülür. HKH'da ise arteryel kontrast hızla yıkanır (washout). Bu farklı patern ICC-HKH ayırımında kritik.",
        "level": 2
    },

    # ── LI-RADS KATEGORİLERİ ─────────────────────────────────────────────────

    {
        "id": "bulk_lirads_decision_1",
        "concept_id": "lirads_lr_categories_decision",
        "type": "multiple_choice",
        "question": "22 mm lezyon, APHE var, kapsül var, washout yok. LI-RADS kategorisi?",
        "options": ["LR-3", "LR-4", "LR-5", "LR-M"],
        "correct": 2,
        "explanation": "≥20 mm + APHE + 1 majör özellik (kapsül) = LR-5. Washout olmasa da kapsül yeterli ikinci majör özellik. LI-RADS kuralı: ≥20 mm + APHE + (washout VEYA kapsül VEYA eşik büyüme) → LR-5.",
        "level": 3
    },
    {
        "id": "bulk_lirads_decision_2",
        "concept_id": "lirads_lr_categories_decision",
        "type": "multiple_choice",
        "question": "8 mm lezyon, APHE var, washout var. LI-RADS kategorisi?",
        "options": ["LR-5", "LR-4", "LR-3", "LR-M"],
        "correct": 2,
        "explanation": "<10 mm lezyonlarda maksimum LR-3 verilebilir — majör özellik sayısından bağımsız. Bu kural yanlış pozitifi azaltmak için konulmuştur. Küçük lezyonlarda APHE vb. bulgular daha az spesifiktir. Takip önerilir: 3-6 ay MR/BT.",
        "level": 3
    },
    {
        "id": "bulk_lirads_decision_3",
        "concept_id": "lirads_lr_categories_decision",
        "type": "multiple_choice",
        "question": "LR-M kategorisi için hangi bulgu kombinasyonu tipiktir?",
        "options": [
            "Non-rim APHE + non-periferik washout",
            "Rim APHE + periferik erken washout + kapsüler retraksiyon",
            "APHE yok + büyüme var",
            "T2 parlak + DWI kısıtlama"
        ],
        "correct": 1,
        "explanation": "LR-M: rim APHE (periferik, dallanma tarzı) + periferik erken washout + kapsüler retraksiyon + satellit lezyon. ICC ve metastatik lezyonlar bu paterni gösterir. Non-rim APHE + non-periferik washout = LR-5 (HKH). Bu ayrım tedavi planını tamamen değiştirir.",
        "level": 3
    },

    # ── BCLC EVRELEMESİ ───────────────────────────────────────────────────────

    {
        "id": "bulk_bclc_1",
        "concept_id": "hcc_bclc_staging",
        "type": "multiple_choice",
        "question": "Milan kriterleri nelerdir?",
        "options": [
            "Tek ≤3 cm veya ≤2 nodül her biri ≤3 cm",
            "Tek ≤5 cm veya ≤3 nodül her biri ≤3 cm",
            "Tek ≤7 cm veya ≤5 nodül her biri ≤5 cm",
            "Portal invazyon yok ve ekstrahepatik yayılım yok"
        ],
        "correct": 1,
        "explanation": "Milan kriterleri karaciğer transplantasyonu için: tek ≤5 cm VEYA ≤3 nodül (her biri ≤3 cm), portal invazyon yok, ekstrahepatik yayılım yok. Bu kriterler karşılanırsa transplant sonrası 5 yıllık sağkalım >70%. Radyolog Milan kriterlerini değerlendirmeli ve raporlamalıdır.",
        "level": 3
    },
    {
        "id": "bulk_bclc_2",
        "concept_id": "hcc_bclc_staging",
        "type": "multiple_choice",
        "question": "BCLC B evresinde standart tedavi seçeneği nedir?",
        "options": [
            "Cerrahi rezeksiyon",
            "Karaciğer transplantasyonu",
            "TACE (transarteriyel kemoembolizasyon)",
            "Sorafenib"
        ],
        "correct": 2,
        "explanation": "BCLC B: çok nodüllü HKH, portal invazyon yok, ekstrahepatik yayılım yok, iyi performans. Standart tedavi TACE. Rezeksiyon BCLC A'da, transplant BCLC 0/A'da, sorafenib/atezolizumab BCLC C'de kullanılır.",
        "level": 3
    },

    # ── DİSPLASTİK NODÜL ─────────────────────────────────────────────────────

    {
        "id": "bulk_dysplastic_1",
        "concept_id": "dysplastic_nodule_hcc",
        "type": "multiple_choice",
        "question": "Yüksek dereceli displastik nodül ile erken HKH arasındaki en önemli görüntüleme farkı nedir?",
        "options": [
            "Boyut farkı — HKH her zaman >2 cm",
            "APHE varlığı — erken HKH'da arteryel kanlanma başlar, displastik nodülde minimal/yok",
            "T2 sinyali — ikisi de aynı",
            "DWI farkı yok"
        ],
        "correct": 1,
        "explanation": "Multistep karsinogenez: displastik nodül → erken HKH. Kritik geçiş: arteryel neovaskülarizasyon başlangıcı. Yüksek dereceli DN'de minimal APHE olabilir ama karakteristik HKH paterni yok. Erken HKH'da APHE belirginleşir. DWI kısıtlama başlayabilir. Bu geçiş döneminde LR-3/4 kategori ve sıkı takip önerilir.",
        "level": 3
    },

    # ── ADENOM SUBTİPLERİ ─────────────────────────────────────────────────────

    {
        "id": "bulk_adenoma_1",
        "concept_id": "adenoma_subtypes_full",
        "type": "multiple_choice",
        "question": "β-katenin aktive adenom subtipinin diğerlerinden farkı ve önemi nedir?",
        "options": [
            "En sık görülen subtipdır, OKS ile ilişkili",
            "Malignite dönüşüm riski taşır — biyopsi gerektirir",
            "T2'de en parlak subtipdır",
            "Gadoxetat MR'da HBP hiperintenstir"
        ],
        "correct": 1,
        "explanation": "β-katenin aktive adenom: %10-15 sıklıkta, görüntüleme özgün değil ama malign transformasyon riski en yüksek subtipdır. Biyopsi immunohistokimya ile subtipi belirler. Diğer subtiplerde boyut ve klinik bağlam yönetimi belirlerken β-katenin şüphesinde biyopsi endikasyonu daha güçlüdür.",
        "level": 3
    },
    {
        "id": "bulk_adenoma_2",
        "concept_id": "adenoma_subtypes_full",
        "type": "multiple_choice",
        "question": "İnflamatuar adenom subtipinin karakteristik MR bulgusu nedir?",
        "options": [
            "T1 kimyasal kayma sinyal düşümü",
            "T2'de belirgin hiperintensite (atoll işareti) + arteryel enhancement",
            "HBP hiperintensite",
            "DWI kısıtlama"
        ],
        "correct": 1,
        "explanation": "İnflamatuar adenom (%40-50): sinüzoidal dilatasyon ve inflamasyon dominant. T2'de belirgin hiperintens — bazen 'atoll işareti' (merkez izointens + çevre hiper). APHE gösterir. HBP hipointens (FNH'dan ayrımı). Atoll işareti bu subtipin karakteristik bulgusudur.",
        "level": 3
    },

    # ── HEMANJİOM VARYANTLARI ─────────────────────────────────────────────────

    {
        "id": "bulk_hemangioma_1",
        "concept_id": "hemangioma_variants",
        "type": "multiple_choice",
        "question": "Dev hemanjiom (>10 cm) tipik hemanjiomdan hangi özelliğiyle ayrılır?",
        "options": [
            "T2'de hiç parlak değil",
            "Santral heterojenite (tromboz/fibrozis) + periferde klasik patern",
            "Arteryel fazda washout gösterir",
            "DWI kısıtlama yapar"
        ],
        "correct": 1,
        "explanation": "Dev hemanjiom: periferde klasik periferik nodüler enhancement + fill-in KORUNUR. Ancak merkezde tromboz ve fibrozis nedeniyle heterojenite olur — T2'de merkez daha az parlak. Bu merkezi heterojeniteyi bilmeden dev hemanjiomda 'atipik' denmesi yanlış yorum doğurur.",
        "level": 3
    },

    # ── METASTİK PATERNLER ────────────────────────────────────────────────────

    {
        "id": "bulk_metastasis_1",
        "concept_id": "metastasis_patterns_full",
        "type": "multiple_choice",
        "question": "Karaciğerde hipervasküler metastaz yapan primer tümörler hangileridir?",
        "options": [
            "Kolorektal, meme, akciğer",
            "NET (nöroendokrin), böbrek hücreli, tiroid, melanom",
            "Pankreas, mide, over",
            "Mesane, prostat, testis"
        ],
        "correct": 1,
        "explanation": "Hipervasküler karaciğer metastazları: NET (nöroendokrin tümörler), RCC (böbrek hücreli karsinom), tiroid karsinomu, melanom ve bazı meme alt tipleri. Bu tümörlerde arteryel faz kritik — portal fazda kaybolabilirler. Hipovasküler metastazlar (kolorektal, meme, akciğer, pankreas) portal fazda en belirgin.",
        "level": 3
    },
    {
        "id": "bulk_metastasis_2",
        "concept_id": "metastasis_patterns_full",
        "type": "multiple_choice",
        "question": "Karaciğer metastazı için DWI kullanımının avantajı nedir?",
        "options": [
            "Hipervasküler metastazları daha iyi gösterir",
            "Küçük lezyonların (<1 cm) tespitini artırır — yüksek kontrast",
            "Vasküler invazyon değerlendirmesi",
            "Tedavi yanıtı ölçümü"
        ],
        "correct": 1,
        "explanation": "DWI'nın karaciğer metastazında en önemli avantajı küçük lezyonların tespiti. Yüksek b değeri görüntülerde (b800) karaciğer arka planı baskılanır, yüksek hücreli metastazlar parlak görünür. Özellikle kemoterapi öncesi evrelemede veya tedavi sonrası rezidü değerlendirmesinde BT/konvansiyonel MR'a üstünlük sağlar.",
        "level": 3
    },

    # ── TUZAKLAR ─────────────────────────────────────────────────────────────

    {
        "id": "bulk_pitfall_pseudolesion_1",
        "concept_id": "pitfall_pseudolesion",
        "type": "multiple_choice",
        "question": "Üçüncü giriş etkisi (third inflow effect) karaciğerde nerede ve neden oluşur?",
        "options": [
            "Karaciğer merkezinde — portal ven tıkanması",
            "Safra kesesi fossası ve falciform ligament çevresinde — lokal venöz drenaj farklılığı",
            "Kaudat lobda — hepatik ven farklılığı",
            "Sağ lob arka segmentinde — hepatik arterden"
        ],
        "correct": 1,
        "explanation": "Üçüncü giriş etkisi: safra kesesi fossası ve falciform ligament çevresindeki karaciğer parankimi, normal portal/arteryel kan yerine safra kesesinden veya falciform ligamentten gelen sistemik venöz kan alır. Bu kan düşük kontrast içerdiğinden bu bölgeler arteryel fazda farklı görünür — lezyon veya yağ sparing taklidi yapabilir.",
        "level": 5
    },

    # ── MULTİMODAL KORrelasyon ────────────────────────────────────────────────

    {
        "id": "bulk_multimodal_1",
        "concept_id": "multimodal_surveillance_strategy",
        "type": "multiple_choice",
        "question": "Abbreviated MRI (kısaltılmış MR) surveyans protokolünde hangi sekanslar kullanılır?",
        "options": [
            "Sadece T2 FS",
            "Non-kontrast T1 + DWI ± T2",
            "Tam protokol — tüm sekanslar",
            "Sadece gadoxetat kontrastlı arteryel faz"
        ],
        "correct": 1,
        "explanation": "Abbreviated MRI (AMRI): kontrast kullanmadan non-kontrast T1 + DWI ± T2. US'e göre önemli üstünlük: obez/gaz sorunu olan hastalarda daha iyi HKH tespiti. Tam protokole (30-45 dk) kıyasla 10-15 dk sürer. AASLD 2023 US alternativitesi olarak önermektedir.",
        "level": 6
    },
    {
        "id": "bulk_multimodal_2",
        "concept_id": "multimodal_ceus_role",
        "type": "multiple_choice",
        "question": "CEUS'ta mikrobalonların en önemli özelliği nedir?",
        "options": [
            "Ekstraselüler alana dağılır",
            "Tamamen intravasküler kalır — gerçek zamanlı perfüzyon görüntüleme",
            "Hepatositlerce alınır",
            "Böbrekten atılır"
        ],
        "correct": 1,
        "explanation": "Mikrobalonlar (sulfur hexafluoride, perfluorocarbon) tamamen intravaskülerdir — ekstraselüler alana dağılmaz. Bu özellik CEUS'a BT/MR'dan farklı bir arteryel faz kinetik sağlar. Arteryovenöz şant artefaktı CEUS'ta oluşmaz. ICC'nin erken washout paterni bu özellik sayesinde daha belirgin görülür.",
        "level": 6
    },

    # ── YENİ TANILAR İÇİN SORULAR ─────────────────────────────────────────────

    {
        "id": "bulk_klatskin_1",
        "concept_id": "dd_jaundice_algorithm",
        "type": "multiple_choice",
        "question": "Klatskin tümörü (hilar kolanjiyokarsinom) Bismuth-Corlette Type IV ne anlama gelir?",
        "options": [
            "Bifürkasyon altında, rezektabl",
            "Sağ hepatik duktus tutulumu",
            "Her iki hepatik duktusu sekonder bifürkasyona kadar tutan — genellikle rezektabl değil",
            "Sadece common hepatik duktus"
        ],
        "correct": 2,
        "explanation": "Bismuth-Corlette: Tip I=bifürkasyon altı, Tip II=bifürkasyon, Tip IIIa=sağ+bifürkasyon, Tip IIIb=sol+bifürkasyon, Tip IV=bilateral sekonder bifürkasyona kadar. Tip IV genellikle irrezektabl. MRCP bu sınıflandırma için kritik — biliyer tutulumun haritası çıkarılır.",
        "level": 4
    },
    {
        "id": "bulk_ehe_1",
        "concept_id": "dd_multiple_lesions",
        "type": "multiple_choice",
        "question": "Epiteloid hemanjiyoendotelyoma (EHE) için karakteristik görüntüleme bulgusu hangisidir?",
        "options": [
            "Tek büyük hipervasküler kitle",
            "Periferik yerleşimli multipl nodüller + kapsüler retraksiyon",
            "Diffüz infiltratif patern",
            "Santral kalsifikasyon"
        ],
        "correct": 1,
        "explanation": "EHE: karaciğer kapsülüne yakın (periferik) multipl nodüller + kapsüler retraksiyon. Kapsüler retraksiyon fibröz reaksiyon nedeniyle oluşur — bu ICC ile de görülür. Ayırım için biyopsi gerekli. İmmünohistokimya: CD31, CD34, ERG pozitif.",
        "level": 4
    },
]


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

print("\n── Toplu soru havuzu yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_questions)
    print(f"✓ {n} Question")

driver.close()
print(f"\n✓ Toplu soru havuzu tamamlandı — {len(QUESTIONS)} soru eklendi")

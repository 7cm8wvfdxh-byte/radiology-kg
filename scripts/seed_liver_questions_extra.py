from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

QUESTIONS = [

    # ── SEVİYE 1: TEMEL BİLİM ────────────────────────────────────────────────

    {
        "id": "extra_seg_4",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Karaciğer rezeksiyonunda 'sağ hepatektomi' hangi segmentleri içerir?",
        "options": ["I, II, III, IV", "V, VI, VII, VIII", "V, VI, VII, VIII (± I)", "II, III, IV, V"],
        "correct": 2,
        "explanation": "Sağ hepatektomi: Segment V, VI, VII, VIII. Kaudat lob (Segment I) genellikle sağ hepatektomiye dahil edilir. Sol hepatektomi: II, III, IV. Segment IV'ü içermeyen rezeksiyona 'sol lateral sektörektomi' (Segment II+III) denir.",
        "level": 1
    },
    {
        "id": "extra_seg_5",
        "concept_id": "liver_anatomy_segments",
        "type": "multiple_choice",
        "question": "Portal ven Segment VI ve VII'ye hangi dal aracılığıyla girer?",
        "options": ["Sol portal ven", "Posterior sağ portal ven dalı", "Anterior sağ portal ven dalı", "Umbilikal ven dalı"],
        "correct": 1,
        "explanation": "Sağ portal ven iki ana dala ayrılır: anterior dal (Segment V, VIII) ve posterior dal (Segment VI, VII). Bu anatomik bilgi sağ lobu besleyen embolizasyon veya biyopsi planlamasında kritik.",
        "level": 1
    },
    {
        "id": "extra_vasc_3",
        "concept_id": "liver_anatomy_vasculature",
        "type": "multiple_choice",
        "question": "Hepatik arterin karaciğer kanlanmasına katkısı düşük (%25-30) olmasına rağmen önemi neden büyüktür?",
        "options": [
            "Karaciğerin tek oksijen kaynağı",
            "Safra kanalları sadece hepatik arterden beslenir — iskemide biliyer hasar olur",
            "Portal kandan daha fazla besin taşır",
            "Karaciğer tümörleri sadece portal venden beslenir"
        ],
        "correct": 1,
        "explanation": "Safra kanalları (peribildüktüler pleksus) oksijeni yalnızca hepatik arterden alır — portal ven bunları beslemez. Bu yüzden hepatik arter trombozu veya iskemisinde safra yolları hasar görür ve biliyer striktür gelişir. Transplantasyon sonrası hepatik arter trombozu bu yüzden biliyer komplikasyona yol açar.",
        "level": 1
    },
    {
        "id": "extra_histo_3",
        "concept_id": "liver_histology_lobule",
        "type": "multiple_choice",
        "question": "Hepatik asinus modeli (Rappaport zonları) ne anlama gelir?",
        "options": [
            "Karaciğeri 6 segmente böler",
            "Kan akımına göre zonal metabolik farklılık: Zon 1 portal triad yakını (en iyi oksijenli), Zon 3 santral ven yakını (en az)",
            "Safra akışı yönünü tanımlar",
            "Karaciğer fibrozisini evrelendirir"
        ],
        "correct": 1,
        "explanation": "Rappaport hepatik asinusu: Zon 1 (periportal) en iyi oksijenlenmiş → glikojen sentezi. Zon 3 (perisentral/perivenöz) en az oksijen → detoksifikasyon, ilaç metabolizması. Bu nedenle iskemik hepatit santral vene yakın (Zon 3) hasara yol açar. Viral hepatit ise periportal (Zon 1) bölgeyi önce etkiler.",
        "level": 1
    },
    {
        "id": "extra_histo_4",
        "concept_id": "liver_histology_hepatocyte",
        "type": "multiple_choice",
        "question": "Karaciğer fibrozisinde hangi hücre tip aktive olarak kollajen üretir?",
        "options": ["Kupffer hücreleri", "Hepatositler", "Hepatik stellat hücreler (İto hücreleri)", "Kolanjiositler"],
        "correct": 2,
        "explanation": "Hepatik stellat hücreler (İto hücreleri) Disse aralığında bulunur ve normalde A vitamini depolar. Kronik karaciğer hasarında aktive olurlar → miyofibroblast benzeri fenotip → kollajen tip I ve III üretimi → fibrozis. Antifibrotik tedavilerin hedefi bu hücrelerdir.",
        "level": 1
    },
    {
        "id": "extra_contrast_iod_2",
        "concept_id": "liver_contrast_iodinated",
        "type": "multiple_choice",
        "question": "İyotlu kontrast madde reaksiyonlarının sınıflaması nedir?",
        "options": [
            "Tip 1 ve Tip 2",
            "Hafif (kurdeşen, bulantı), orta (bronkospazm, hipotansiyon), ağır (anafilaksi, kardiyak arrest)",
            "Anafilaktoid ve nefrotoksik",
            "Erken ve geç"
        ],
        "correct": 1,
        "explanation": "ACR sınıflaması: Hafif (kurdeşen, kaşıntı, bulantı — takip yeterli), Orta (bronkospazm, ağır ürtiker, geçici hipotansiyon — tedavi gerekli), Ağır (anafilaksi, pulmoner ödem, kardiyak arrest — acil müdahale). Önceki reaksiyon öyküsü en önemli risk faktörü. Premedikasyon: steroid + antihistamin.",
        "level": 1
    },
    {
        "id": "extra_mr_t1t2_3",
        "concept_id": "mr_physics_t1_t2",
        "type": "multiple_choice",
        "question": "MR'da fibröz doku (siroz fibrozis bandları) T2'de nasıl görünür?",
        "options": [
            "Parlak — serbest su gibi",
            "Koyu (hipointens) — yoğun kollajen T2'yi kısaltır",
            "İzointens",
            "Heterojen"
        ],
        "correct": 1,
        "explanation": "Fibröz doku (kollajen) T2'de hipointenstir — yoğun makromoleküler yapı proton mobilitesini kısıtlar ve T2 relaksasyonunu hızlandırır. Bu nedenle siroz fibrozis bandları T2'de ince koyu çizgiler olarak görünür. Akut inflamasyon veya ödem ise T2'de parlak görünür.",
        "level": 1
    },
    {
        "id": "extra_us_2",
        "concept_id": "us_physics_liver",
        "type": "multiple_choice",
        "question": "Karaciğerde yağlı infiltrasyon US'de nasıl görünür?",
        "options": [
            "Hipoekoik difüz görünüm",
            "Difüz hipereko — yağ-su ara yüzeylerinden çok yansıma + derin yapıların zayıf görülmesi",
            "Heterojen nodüler",
            "Normal"
        ],
        "correct": 1,
        "explanation": "Steatozda karaciğer US'de difüz hipereko (parlak) görünür. Neden: yağ damlacıkları çok sayıda akustik ara yüzey oluşturur → artan yansıma → hipereko. Aynı zamanda ses dalgaları daha fazla absorbe olur → derin yapılar zayıf görülür (arka zayıflama). Karaciğer-böbrek ekojenitesi karşılaştırması: normal KC böbrekle eşit veya hafif yüksek.",
        "level": 1
    },
    {
        "id": "extra_lab_3",
        "concept_id": "liver_lab_tests",
        "type": "multiple_choice",
        "question": "PT/INR karaciğer fonksiyon testlerinde neyi gösterir?",
        "options": [
            "Hepatosit nekrozunu",
            "Sentetik fonksiyonu — karaciğer koagülasyon faktörü üretemez → PT uzar",
            "Biliyer obstrüksiyonu",
            "Portal hipertansiyonu"
        ],
        "correct": 1,
        "explanation": "Faktör II, V, VII, IX, X karaciğerde sentezlenir. Ağır karaciğer yetmezliğinde bu faktörlerin üretimi azalır → PT uzar / INR yükselir. Child-Pugh skorunun komponentidir. Albumin ile birlikte sentetik fonksiyonun en güvenilir göstergeleridir.",
        "level": 1
    },
    {
        "id": "extra_hu_3",
        "concept_id": "ct_physics_hu",
        "type": "multiple_choice",
        "question": "Karaciğer BT'sinde 'double duct sign' (çift kanal işareti) ne anlama gelir?",
        "options": [
            "İki ayrı karaciğer lezyonu",
            "Hem common bile duct hem de pankreatik kanalın dilatasyonu — pankreas başı patolojisi",
            "Hepatik ven ve portal venin aynı anda görülmesi",
            "İki ayrı vasküler yapı"
        ],
        "correct": 1,
        "explanation": "Çift kanal işareti: BT veya MRCP'de hem CBD hem de wirsung kanalının aynı anda dilate görülmesi. Pankreatik başta kitle (adenokarsinom, ampüller karsinom) her iki kanalı tıkıyor demektir. Bu bulgu pankreas başı patolojisinin önemli görüntüleme işaretidir.",
        "level": 1
    },

    # ── SEVİYE 2: ORTA DÜZEY ─────────────────────────────────────────────────

    {
        "id": "extra_portal_3",
        "concept_id": "portal_hypertension",
        "type": "multiple_choice",
        "question": "Rekanalize umbilikal ven (caput medusae) portal hipertansiyonda neden gelişir?",
        "options": [
            "Yeni damar oluşumu",
            "Fetal hayatta açık olan umbilikal ven portal basınç artışında tekrar açılarak paraumbilikal kollateral yol sağlar",
            "Umbilikal herni komplikasyonu",
            "Karaciğer tümörü invazyonu"
        ],
        "correct": 1,
        "explanation": "Umbilikal ven fetal hayatta açık, doğum sonrası kapanır (ligamentum teres). Portal hipertansiyonda basınç artışı bu reziküel yapıyı tekrar açabilir. Falciform ligament içinde umbilikal vende kan akımı başlar → göbek çevresinde yılan şekilli venler → caput medusae. US Doppler'da falciform ligament içinde artmış akım görülür.",
        "level": 2
    },
    {
        "id": "extra_cirrhosis_3",
        "concept_id": "liver_cirrhosis_imaging",
        "type": "multiple_choice",
        "question": "MR elastografi karaciğer değerlendirmesinde ne işe yarar?",
        "options": [
            "Lezyon karakterizasyonu",
            "Karaciğer sertliğini ölçer → fibrozis evrelendirmesi (F0-F4)",
            "Kontrast kinetik analizi",
            "Safra yolu görüntüleme"
        ],
        "correct": 1,
        "explanation": "MR elastografi (MRE): mekanik dalga yayılım hızını ölçerek karaciğer sertliğini kPa cinsinden hesaplar. Sertlik = fibrozis. F0 (<2.5 kPa) → F4/siroz (>5 kPa). Biyopsiye alternatif non-invazif fibrozis değerlendirmesi. NASH, viral hepatit, otoimmün hepatit takibinde kullanılır. Asit varlığında güvenilirliği azalır.",
        "level": 2
    },
    {
        "id": "extra_fatty_2",
        "concept_id": "liver_fatty_infiltration",
        "type": "multiple_choice",
        "question": "MR PDFF (proton density fat fraction) nedir ve önemi nedir?",
        "options": [
            "Difüzyon ölçüm yöntemi",
            "Karaciğerdeki yağ oranını %5-95 hassasiyetle ölçen kantitatif MR tekniği",
            "Kontrast tutulum hesabı",
            "T2* relaxometry"
        ],
        "correct": 1,
        "explanation": "PDFF (Proton Density Fat Fraction): multi-echo GRE sekansıyla yağ ve su protonlarının sinyalinden yağ fraksiyonu hesaplanır. Karaciğer yağ içeriğini kantitatif olarak %1-5 hassasiyetle ölçer. Steatoz evresi: <5% normal, 5-10% hafif, 10-20% orta, >20% ağır. NAFLD/NASH tedavi yanıtı takibinde biyopsiden üstün.",
        "level": 2
    },
    {
        "id": "extra_biliary_2",
        "concept_id": "liver_biliary_anatomy",
        "type": "multiple_choice",
        "question": "Mirizzi sendromu nedir?",
        "options": [
            "İntrahepatik safra yolu kisti",
            "Safra kesesi boynu veya sistik kanaldaki taşın common hepatik kanalı dışarıdan baskılaması → obstrüktif sarılık",
            "Klatskin tümörü başka adı",
            "Pankreatik kanal darlığı"
        ],
        "correct": 1,
        "explanation": "Mirizzi sendromu: safra kesesi boynu veya sistik kanaldaki taşın komşu CHD'yi dışarıdan baskılamasıyla obstrüktif sarılık. MRCP'de sistik kanalda taş + CHD'de dıştan bası görülür. Cerrahi planlama açısından önemli — kolanjiyokarsinom ile karışabilir.",
        "level": 2
    },
    {
        "id": "extra_vascular_2",
        "concept_id": "liver_vascular_pathology",
        "type": "multiple_choice",
        "question": "Konjesif hepatopati hangi kardiyolojik durumla ilişkilidir?",
        "options": [
            "Sol kalp yetmezliği",
            "Sağ kalp yetmezliği veya triküspit regürjitasyonu — hepatik ven basıncı artar",
            "Aort stenozu",
            "Mitral stenoz"
        ],
        "correct": 1,
        "explanation": "Sağ kalp yetmezliğinde sistemik venöz basınç artar → hepatik venler ve IVC dilate → karaciğer konjesyonu. BT/MR'da mozaik enhancement (periferik sinüzoidal dilatasyon), hepatomegali, periferden merkeze enhancement paterni, IVC dilatasyonu. Kardiyoloji konsültasyonu gerekir.",
        "level": 2
    },
    {
        "id": "extra_systematic_2",
        "concept_id": "liver_systematic_reading",
        "type": "multiple_choice",
        "question": "Karaciğer BT'sinde lezyon boyutu nasıl ölçülür?",
        "options": [
            "Her zaman axial kesitte en geniş çap",
            "En büyük çap — tek ölçüm veya iki boyutlu (uzun × kısa aks) — tutarlı kesitte",
            "Hacim hesabı zorunlu",
            "Sadece kontrastlı kesitte"
        ],
        "correct": 1,
        "explanation": "LI-RADS ve RECIST standartları: en büyük çap, tutarlı kesitte (axial tercih edilir). Takip görüntülemesinde aynı kesit seviyesinden ölçüm karşılaştırma güvenilirliğini artırır. Hemanjiom gibi değişken boyutlular için iki yönde ölçüm (çap × çap) kullanılabilir.",
        "level": 2
    },
    {
        "id": "extra_hemochrom_2",
        "concept_id": "liver_hemochromatosis",
        "type": "multiple_choice",
        "question": "Hemokromatozda HKH gelişim riski ne kadar artar?",
        "options": [
            "Risk artmaz",
            "2-3 kat",
            "20-200 kat — özellikle siroz gelişmişse",
            "Sadece transplant sonrası risk artar"
        ],
        "correct": 2,
        "explanation": "Hemokromatozda HKH riski 20-200 kat artmış. Özellikle siroz gelişmişse risk çarpıcı biçimde yüksek. Erken tanı ve demir boşaltma (flebotomi veya kelasyon) siroz ve HKH gelişimini önleyebilir. Bu yüzden hemokromatoz tanısı konunca HKH surveyansı başlanmalıdır.",
        "level": 2
    },
    {
        "id": "extra_wilson_2",
        "concept_id": "liver_wilson_disease",
        "type": "multiple_choice",
        "question": "Wilson hastalığı genç sirotik hastada nasıl tanınır?",
        "options": [
            "AFP yüksekliği",
            "Serum serüloplazmin düşük + 24 saatlik idrar bakırı yüksek + Kayser-Fleischer halkası",
            "HBsAg pozitifliği",
            "Biliyer obstrüksiyon"
        ],
        "correct": 1,
        "explanation": "Wilson tanı kriterleri: serum serüloplazmin <20 mg/dL + 24 saat idrar bakırı >100 μg/gün + Kayser-Fleischer halkası (yarık lamba). Leipzig skoru kullanılır. Genç hastada (<40 yaş) açıklanamayan siroz, hemolitik anemi veya nöropsikiyatrik bulgular Wilson'ı düşündürmelidir.",
        "level": 2
    },
    {
        "id": "extra_budd_2",
        "concept_id": "liver_budd_chiari",
        "type": "multiple_choice",
        "question": "Budd-Chiari sendromunda hangi hiperkoagülabilite durumları araştırılmalıdır?",
        "options": [
            "Sadece faktör V Leiden",
            "Polisitemi vera, JAK2 mutasyonu, faktör V Leiden, protein C/S eksikliği, antifosfolipid sendromu, OKS",
            "Sadece OKS kullanımı",
            "Sadece gebelik"
        ],
        "correct": 1,
        "explanation": "Budd-Chiari'nin %75'inde hiperkoagülabilite saptanır. En sık: JAK2 V617F mutasyonu (polisitemi vera, esansiyel trombositemi). Diğerleri: faktör V Leiden, protein C/S eksikliği, antitrombin III eksikliği, antifosfolipid sendromu, OKS kullanımı, gebelik. Hematoloji konsültasyonu zorunludur.",
        "level": 2
    },
    {
        "id": "extra_ct_protocol_3",
        "concept_id": "liver_ct_protocol",
        "type": "multiple_choice",
        "question": "Karaciğer BT'sinde geç faz (3-5 dk) neden alınır?",
        "options": [
            "Arteryel yapılar için",
            "Washout değerlendirmesi + enhancing kapsül + ICC persistan enhancement + hemanjiom fill-in",
            "Portal ven için",
            "Safra yolu görüntüleme"
        ],
        "correct": 1,
        "explanation": "Geç faz (equilibrium phase): (1) HKH washout teyidi, (2) enhancing kapsül en belirgin, (3) ICC fibröz stroması geç fazda persistan enhancement, (4) hemanjiom fill-in tamamlanır. Bu faz HKH-ICC ayırımında ve hemanjiom konfirmasyonunda kritik.",
        "level": 2
    },
    {
        "id": "extra_mr_protocol_3",
        "concept_id": "liver_mr_protocol",
        "type": "multiple_choice",
        "question": "Dixon sekansı karaciğer MR'ında ne işe yarar?",
        "options": [
            "Difüzyon ölçümü",
            "Yağ ve su görüntülerini ayrı ayrı üretir + yağ fraksiyonu hesabı — in/out phase'e alternatif",
            "Kontrast kinetik analizi",
            "Kalsifikasyon tespiti"
        ],
        "correct": 1,
        "explanation": "Dixon tekniği multi-echo GRE sekansıdır. In-phase ve out-phase görüntülerinden matematiksel olarak 'sadece su' ve 'sadece yağ' görüntüleri üretilir. PDFF hesabında kullanılır. Geleneksel in/out phase'e göre daha hassas ve kantitatif yağ ölçümü sağlar.",
        "level": 2
    },
    {
        "id": "extra_trauma_3",
        "concept_id": "liver_trauma_aast",
        "type": "multiple_choice",
        "question": "Karaciğer yaralanmalarında nonoperatif yönetim (NOM) için temel kriter nedir?",
        "options": [
            "AAST Grade I-II olmak",
            "Hemodinamik stabilite — stabil hastada Grade III-IV bile NOM mümkün",
            "Laserasyon yokluğu",
            "Kanama odağı olmamak"
        ],
        "correct": 1,
        "explanation": "NOM için temel kriter hemodinamik stabilite. Stabil hastalarda Grade III-IV yaralanmalar bile başarıyla NOM ile yönetilebilir. Hemodinamik instabilite → acil cerrahi veya anjiyoembolizasyon. WSES kılavuzu: Grade bakılmaksızın stabil hasta → NOM dene, instabil → cerrahi.",
        "level": 2
    },
    {
        "id": "extra_transplant_2",
        "concept_id": "liver_transplant_imaging",
        "type": "multiple_choice",
        "question": "Post-transplant lenfoproliferatif hastalık (PTLD) neden gelişir ve görüntülemede nasıl görünür?",
        "options": [
            "Transplant reddi",
            "İmmunosüpresyon altında EBV reaktivasyonu → B hücre proliferasyonu — karaciğer, LN, dalak, böbrek kitleler",
            "Cerrahi komplikasyon",
            "Steatoz"
        ],
        "correct": 1,
        "explanation": "PTLD: immünosüpresyon altında EBV (Epstein-Barr virüs) reaktivasyonu → kontrol dışı B lenfosit proliferasyonu. Görüntülemede: karaciğer, dalak, lenf nodları, böbrek, GIS'te kitleler. BT'de solid veya ring-enhancing kitleler. Tedavi: immünosüpresyon azaltma, rituksimab. Erken tanı kritik.",
        "level": 2
    },
    {
        "id": "extra_caroli_2",
        "concept_id": "liver_caroli_disease",
        "type": "multiple_choice",
        "question": "Caroli hastalığında kolanjiyokarsinom gelişim riski ne kadar?",
        "options": [
            "Risk yok",
            "%7 kümülatif risk — uzun süreli PSK benzeri safra oluşumu ve taş",
            "%50 dönüşüm",
            "Sadece Caroli sendromunda"
        ],
        "correct": 1,
        "explanation": "Caroli hastalığında yaşam boyu kolanjiyokarsinom gelişim riski yaklaşık %7. Kronik safra stazı, intrahepatik taş formasyonu ve tekrarlayan kolanjit epizodları kolanjiokarsinom riskini artırır. Bu nedenle periodik görüntüleme ve CA 19-9 takibi önerilir.",
        "level": 2
    },

    # ── SEVİYE 3: İLERİ DÜZEY ────────────────────────────────────────────────

    {
        "id": "extra_lirads_ancillary_2",
        "concept_id": "lirads_ancillary_features",
        "type": "multiple_choice",
        "question": "Corona enhancement yardımcı özelliği ne anlama gelir?",
        "options": [
            "Lezyon çevresinde arteryel fazda geçici perilesional enhancement — tümör drene eden sinüzoidlerin arteryel kanlanması",
            "Enhancing kapsül",
            "Satellit lezyon",
            "Rim enhancement"
        ],
        "correct": 0,
        "explanation": "Corona enhancement: arteryel fazda lezyon çevresinde perilesional enhancement halkası. Mekanizma: HKH peritümöral sinüzoidlerin arteryel kanlanmaya geçmesi. Geç fazda kaybolur. HKH'ya özgü yardımcı özellik — malignite lehine kullanılır ama LR-5'e yükseltemez.",
        "level": 3
    },
    {
        "id": "extra_lirads_ancillary_3",
        "concept_id": "lirads_ancillary_features",
        "type": "multiple_choice",
        "question": "LI-RADS'ta 'mozaik mimari' hangi lezyona özgü yardımcı özelliktir?",
        "options": [
            "ICC — fibröz stroma",
            "HKH — farklı kleranlı nodüller veya septalı görünüm",
            "Metastaz",
            "Hemanjiom"
        ],
        "correct": 1,
        "explanation": "Mozaik mimari: HKH'ya özgü yardımcı özellik. HKH içinde farklı vaskülarizasyon veya diferansiasyon gösteren alanlar oluşturur → lezyon içi heterojen, 'mozaik' görünüm. Fibröz kapsül veya septalara benzer ama daha düzensiz. İleri evre HKH'da daha belirgin.",
        "level": 3
    },
    {
        "id": "extra_bclc_3",
        "concept_id": "hcc_bclc_staging",
        "type": "multiple_choice",
        "question": "Down-staging nedir ve radyoloji ne zaman kullanılır?",
        "options": [
            "HKH'nın tümüyle yok edilmesi",
            "Milan kriterleri dışındaki HKH'yı TACE/ablasyon ile Milan içine çekme → transplant fırsatı",
            "Evre yükseltme",
            "Biyopsi sonrası evreleme"
        ],
        "correct": 1,
        "explanation": "Down-staging: Milan kriterleri dışındaki HKH'yı (örn: 7 cm tek veya 3 nodül >3 cm) lokal-bölgesel tedavi (TACE, ablasyon) ile Milan kriterlerine çekme stratejisi. Radyoloji: tedavi yanıtını değerlendirerek hastanın transplant listesine alınıp alınamayacağını belirler. mRECIST ile canlı tümör ölçülür.",
        "level": 3
    },
    {
        "id": "extra_dysplastic_2",
        "concept_id": "dysplastic_nodule_hcc",
        "type": "multiple_choice",
        "question": "Gadoxetat MR'da displastik nodül ile erken HKH arasındaki en önemli fark nedir?",
        "options": [
            "Boyut farkı",
            "HBP: displastik nodül izointens kalabilir veya hiperdens olabilir; erken HKH hipointens olmaya başlar",
            "T1 sinyali",
            "APHE her ikisinde de var"
        ],
        "correct": 1,
        "explanation": "Gadoxetat MR HBP: displastik nodülde OATP ekspresyonu korunmuş olabilir → izointens veya hiperintens. Erken HKH'da OATP ekspresyonu kaybı başlar → HBP hipointens. Bu geçiş dinamik bir süreçtir. HBP hipointensite displastik nodüle kıyasla HKH'yı yüksek sensitivite ile işaret eder.",
        "level": 3
    },
    {
        "id": "extra_hemangioma_2",
        "concept_id": "hemangioma_variants",
        "type": "multiple_choice",
        "question": "Hemanjiomda CEUS kullanımının avantajı nedir?",
        "options": [
            "Daha büyük görüntüleme alanı",
            "Gerçek zamanlı periferik nodüler → fill-in patern gösterimi — BT/MR'dan daha yüksek spesifisite",
            "Gadolinyum içermez",
            "Hızlı"
        ],
        "correct": 1,
        "explanation": "CEUS hemanjiom tanısında %98+ spesifite gösterir. Mikrobalonların tamamen intravasküler karakteri hemanjiomun yavaş kan havuzu dolumunu gerçek zamanlı gösterir. Flash fill hemanjiomda bile CEUS periferik nodüler dolum sonra fill-in paternini net ortaya koyar. Gadolinyum ve radyasyon gerektirmez.",
        "level": 3
    },
    {
        "id": "extra_adenoma_3",
        "concept_id": "adenoma_subtypes_full",
        "type": "multiple_choice",
        "question": "Hepatik adenom ≥5 cm boyutunda neden özellikle izlenir veya rezeke edilir?",
        "options": [
            "Malignite riski artar",
            "Spontan kanama riski artar + β-katenin dönüşüm riski. OKS kesimi + 6 ay sonra küçülme görülmezse cerrahi",
            "US'de görülmez hale gelir",
            "Transplant şartı"
        ],
        "correct": 1,
        "explanation": "≥5 cm adenom: (1) Spontan kanama/rüptür riski belirgin artar — hemoperitoneum hayati tehlike, (2) Malign transformasyon riski artar (özellikle β-katenin). Bu nedenle OKS kesilmesi + 6 ayda MR kontrolü önerilir. 6 ayda küçülme görülmezse veya β-katenin şüphesi varsa cerrahi değerlendirme.",
        "level": 3
    },
    {
        "id": "extra_metastasis_3",
        "concept_id": "metastasis_patterns_full",
        "type": "multiple_choice",
        "question": "Karaciğer metastazı değerlendirmesinde PET-BT ne zaman kullanılır?",
        "options": [
            "Her metastaz şüphesinde",
            "BT/MR ile tespit edilemeyen küçük lezyonlarda ve tedavi yanıt değerlendirmesinde — metabolik aktiviteyi gösterir",
            "Tanı koymak için tek yöntem",
            "Biyopsi yerine"
        ],
        "correct": 1,
        "explanation": "PET-BT (FDG): metabolik aktif tümör hücrelerini gösterir. Karaciğer metastazı değerlendirmesinde: (1) BT/MR'da şüpheli ama küçük lezyonlar, (2) Sistemik tedavi yanıt değerlendirmesi, (3) Ekstrahepatik yayılım araştırması. Kısıtlama: FDG-avid olmayan tümörler (NET, müsinöz) false-negative. MR difüzyon genellikle daha sensitif.",
        "level": 3
    },
    {
        "id": "extra_abscess_3",
        "concept_id": "liver_abscess_types",
        "type": "multiple_choice",
        "question": "Amipli karaciğer apsesinin piyojeninden klinik ayırımı nasıl yapılır?",
        "options": [
            "Görüntüleme ile tam ayrım mümkün",
            "Seyahat öyküsü + tek büyük lezyon + Entamoeba histolytica serolojisi pozitif + antibiyotik yerine metronidazol yanıtı",
            "Piyojenik daima multipl",
            "Amipli daima kalsifiye"
        ],
        "correct": 1,
        "explanation": "Amipli apse ayırım kriterleri: endemik bölgeye seyahat öyküsü, tek büyük lezyon (genellikle sağ lob), US'de homojen hipoekoik (mayonez/çikolata şurubu), E. histolytica serolojisi pozitif. Tedavi: metronidazol (piyojenik'te antibiyotik). Görüntülemede ikisi tam ayrılamaz — klinik ve seroloji zorunlu.",
        "level": 3
    },

    # ── SEVİYE 4: AYIRıCI TANI ───────────────────────────────────────────────

    {
        "id": "extra_dd_hyper_3",
        "concept_id": "dd_hypervascular_lesion",
        "type": "multiple_choice",
        "question": "Karaciğerde APHE gösteren lezyon için 'non-rim' özelliği neden önemlidir?",
        "options": [
            "Boyutu gösterir",
            "Non-rim APHE (sentral veya diffüz) HKH'ya özgü. Rim APHE (periferik) LR-M — ICC veya metastaz",
            "Kontrast dozu belirler",
            "Tedavi seçimini etkiler"
        ],
        "correct": 1,
        "explanation": "Non-rim APHE: lezyon içinde uniform veya heterojen arteryel enhancement — HKH'ya özgü majör özellik. Rim APHE: lezyon kenarında arteryel enhancement, merkez almaz — LR-M kriteridir ve ICC veya hipovasküler metastazı düşündürür. Bu ayrım LI-RADS kategorisini ve hasta yönetimini doğrudan değiştirir.",
        "level": 4
    },
    {
        "id": "extra_dd_hypo_2",
        "concept_id": "dd_hypodense_lesion_ct",
        "type": "multiple_choice",
        "question": "BT'de periferik enhancement + santral düşük dansite — target (hedef) görünümü neyi düşündürür?",
        "options": [
            "Basit kist",
            "Hipovasküler metastaz — periferik canlı tümör, santral nekroz",
            "Hemanjiom",
            "Apse"
        ],
        "correct": 1,
        "explanation": "Target/bull's eye işareti: periferik rim enhancement + santral düşük dansite (nekroz/fibrozis). Hipovasküler metastazın (kolorektal, meme, akciğer) tipik bulgusu. Portal fazda en belirgin. Apse ile ayırım: apseye eşlik eden klinik bulgular (ateş), DWI kısıtlama ve CEUS honeycomb paterni.",
        "level": 4
    },
    {
        "id": "extra_dd_cyst_2",
        "concept_id": "dd_cystic_lesion_liver",
        "type": "multiple_choice",
        "question": "BT'de 4 cm kistik lezyon, septa var, mural nodül yok, içerik homojen düşük dansite. Sonraki adım?",
        "options": [
            "Biyopsi",
            "Takip gerekmez",
            "MR T2 + kontrast + DWI — mural nodül ve solid komponent değerlendirmesi",
            "Cerrahi direkt"
        ],
        "correct": 2,
        "explanation": "Septasyonlu kistik lezyon BT'de karakterize edilemez. MR: T2 (sıvı karakteri), kontrast (mural nodül enhancement = solid komponent = neoplazm şüphesi), DWI (hücresellik). MCN veya biliyer kistadenoma ekartasyonu için MR zorunlu. Homojen görünüm maligniteyi ekarte etmez — MR ile doğrulama.",
        "level": 4
    },
    {
        "id": "extra_dd_t2_2",
        "concept_id": "dd_t2_bright_lesion",
        "type": "multiple_choice",
        "question": "FNH'nin santral skarı T2'de neden parlaktır?",
        "options": [
            "Fibröz doku T2'de her zaman parlak",
            "Santral skarda fibröz doku içinde miyksoid degenerasyon ve vasküler yapılar → uzun T2",
            "Kontrast birikir",
            "Nekroz alanı"
        ],
        "correct": 1,
        "explanation": "FNH santral skarı: fibröz doku + sıkışmış dilate safra kanalları + anormal damarlar içerir. Bu yapılar uzun T2 gösterir → T2'de parlak. Geç fazda kontrast da alır. T2'de parlak santral skar + arteryel enhancement + geç faz skar tutulumu FNH'nın karakteristik triyadıdır. İCC'nin santral fibrozisi T2'de koyu.",
        "level": 4
    },
    {
        "id": "extra_dd_portal_2",
        "concept_id": "dd_portal_hypertension_differential",
        "type": "multiple_choice",
        "question": "Şistosomiasis karaciğer görüntülemesinde nasıl görünür?",
        "options": [
            "Fokal lezyon",
            "Periportal fibroz — kaplumbağa sırtı paterni (pipestem fibrosis) + portal hipertansiyon",
            "Difüz steatoz",
            "Kistik lezyonlar"
        ],
        "correct": 1,
        "explanation": "Şistosomiasis (Schistosoma mansoni): portal alana yumurta emboli → periportal fibrozis. BT/US'de periportal hipereko/hiperdens bandlar 'pipestem fibrosis' — kaplumbağa sırtı paterni. İntrahepatik sinüzoidal fibrozis → presinüzoidal portal HT. Karaciğer parankimi korunur. Endemik bölgeden seyahat öyküsü.",
        "level": 4
    },
    {
        "id": "extra_dd_incidental_2",
        "concept_id": "dd_incidental_liver_lesion",
        "type": "multiple_choice",
        "question": "Onkoloji hastasında BT'de yeni 5 mm hipodens karaciğer lezyonu. Yönetim?",
        "options": [
            "Takip gerekmez — çok küçük",
            "Her boyuttaki lezyon değerlendirilmeli — MR ile karakterizasyon veya kısa interval takip",
            "Biyopsi",
            "6 ayda US"
        ],
        "correct": 1,
        "explanation": "Bilinen malignite olan hastada yeni karaciğer lezyonu — boyuttan bağımsız — dikkat gerektirir. <1 cm olsa bile metastaz olabilir. ACR: onkoloji hastasında <1 cm lezyon için 3-6 ay MR ile takip. Şüpheli ise MR ile karakterizasyon. Normal karaciğer zeminindeki insidental <1 cm lezyon için takip gerekmezdi — bu vakanın farkı klinik bağlam.",
        "level": 4
    },
    {
        "id": "extra_dd_young_2",
        "concept_id": "dd_liver_mass_young_woman",
        "type": "multiple_choice",
        "question": "Genç kadında FNH'nin tedavisi nedir?",
        "options": [
            "Cerrahi rezeksiyon zorunlu",
            "OKS kesilmesi + görüntüleme izlemi — çoğu FNH küçülür",
            "TACE uygulanır",
            "Biyopsi şarttır"
        ],
        "correct": 1,
        "explanation": "FNH malign transformasyon riski taşımaz ve kanama riski minimal. Tedavi: OKS kesilmesi (varsa) + 6-12 ay görüntüleme takibi. Çoğu FNH küçülür veya stabil kalır. Cerrahi sadece: büyüyen semptomatik lezyon, tanısal belirsizlik (adenom ile ayrım yapılamıyor) veya hasta tercihi. Biyopsi gadoxetat MR diagnostik ise gerekmez.",
        "level": 4
    },
    {
        "id": "extra_dd_afp_2",
        "concept_id": "dd_elevated_afp_imaging",
        "type": "multiple_choice",
        "question": "HBV pozitif, siroz yok, AFP 150 ng/mL, 18 mm lezyon LR-4. Yönetim?",
        "options": [
            "Kesin benign — takip",
            "Biyopsi gerekebilir — LR-4 + AFP yüksek + HBV risk faktörü MDT tartışması",
            "Biyopsisiz TACE başla",
            "6 ayda US kontrolü"
        ],
        "correct": 1,
        "explanation": "HBV pozitif + AFP 150 + LR-4: birden fazla risk faktörü. LR-4 tek başına biyopsi gerektirmez ama AFP yüksekliği ve HBV birlikteliği klinik şüpheyi artırır. MDT tartışması önerilir. LI-RADS 2024 AFP >200 ng/mL yardımcı özellik olarak resmileştirdi. Bu vakada 3 ayda MR kontrolü veya biyopsi MDT kararına bırakılır.",
        "level": 4
    },

    # ── SEVİYE 5: TUZAKLAR ───────────────────────────────────────────────────

    {
        "id": "extra_pseudo_2",
        "concept_id": "pitfall_pseudolesion",
        "type": "multiple_choice",
        "question": "Fokal yağ sparing ile fokal nodüler lezyon US'de nasıl ayrılır?",
        "options": [
            "Boyut farkı",
            "Fokal yağ sparing: düzgün sınırsız, damarlar normal anatomide geçer içinden. Gerçek lezyon: damarları iter, küresel şekil",
            "Enhancement farkı",
            "Ayrım yapılamaz — MR şart"
        ],
        "correct": 1,
        "explanation": "Fokal yağ sparing: diffüz yağlı karaciğerde yağ içermeyen alan hipoekoik görünür ama gerçek lezyon değil. Ayırım: (1) Damarlar (portal ven dalları) normal anatomik seyirleriyle bölgenin içinden geçer — lezyon değil. (2) Düzgün coğrafi sınır. (3) Tipik lokalizasyon: safra kesesi fossası, falciform ligament, porta hepatis. MR kimyasal kayma konfirme eder.",
        "level": 5
    },
    {
        "id": "extra_burnout_2",
        "concept_id": "pitfall_burnout_metastasis",
        "type": "multiple_choice",
        "question": "Burn-out HKH siroz zemininde nasıl görünür ve klinik önemi nedir?",
        "options": [
            "Arteryel enhancement gösterir",
            "T2 hipointens fibrotik skar, enhancement yok — aktif HKH değil ama önceki aktif lezyon yerini gösterir",
            "Portal fazda belirgin",
            "Biyopsi gerektirir"
        ],
        "correct": 1,
        "explanation": "Burn-out HKH: spontan fibrozis veya tedavi sonrası. T2'de hipointens skar, arteryel enhancement yok veya minimal. LI-RADS LR-TR Nonviable veya LR-1/2. Önem: (1) Satellit lezyon için çevre takip, (2) Önceki görüntülemelerle karşılaştırma, (3) Başka aktif lezyon araştırması. 'Skar = benign' refleksi tehlikeli — yeni nodül gelişebilir.",
        "level": 5
    },
    {
        "id": "extra_small_hcc_2",
        "concept_id": "pitfall_small_hcc_detection",
        "type": "multiple_choice",
        "question": "LR-4 lezyonun takip aralığı nedir?",
        "options": [
            "6 ayda US",
            "3 ayda CT veya MR",
            "Yıllık MR",
            "Hemen biyopsi"
        ],
        "correct": 1,
        "explanation": "LR-4 (HKH olasılığı yüksek ~%74): 3 ayda CT veya MR. Bu aralık kritik — 3 ayda eşik büyüme (%50) olursa LR-5'e yükselir ve tedavi başlanabilir. 6 ay beklemek HKH'nın ilerlemesine fırsat tanır. AASLD 2023 önerir: LR-4 → 3 ayda multifazik CT veya MR.",
        "level": 5
    },
    {
        "id": "extra_artifact_2",
        "concept_id": "pitfall_mri_artifacts",
        "type": "multiple_choice",
        "question": "Susceptibility ağırlıklı görüntülemede (SWI/GRE) karaciğerde diffüz sinyal kaybı görülüyor. Neden?",
        "options": [
            "Steatoz",
            "Demir birikimi — hemokromatoz veya siderotik nodüller",
            "Fibrozis",
            "Ödem"
        ],
        "correct": 1,
        "explanation": "SWI veya GRE (T2*) sekanslar manyetik susceptibility farklılıklarına duyarlıdır. Demir güçlü paramanyetik materyal olduğundan sinyal kaybına yol açar. Diffüz karaciğer sinyal kaybı = demir birikimi (hemokromatoz). Fokal sinyal kaybı = siderotik nodül. Bu sekanslar demir miktarını kantitatif R2* ile ölçmede kullanılır.",
        "level": 5
    },
    {
        "id": "extra_hcc_mimic_2",
        "concept_id": "pitfall_hcc_mimics",
        "type": "multiple_choice",
        "question": "Arteryovenöz malformasyon (AVM) HKH'dan nasıl ayrılır?",
        "options": [
            "Boyutu küçüktür",
            "AVM: büyük besleyici damar + erken drene ven + kama veya üçgen şekil + portal fazda kaybolmaz tam olarak",
            "AVM T2'de koyu",
            "AVM enhancement göstermez"
        ],
        "correct": 1,
        "explanation": "AVM: anormal arteriyovenöz bağlantı. BT/MR'da: (1) Büyük besleyici hepatik arter dalı, (2) Arteryel fazda erken dolum eden hepatik ven (erken venöz dönüş), (3) Küresel değil geometrik şekil. Nodüler HKH paterni yok. Anjiyografi tanı koydurucu. Büyük semptomatik AVM'ler embolizasyon gerektirebilir.",
        "level": 5
    },
    {
        "id": "extra_postop_2",
        "concept_id": "pitfall_post_op_liver",
        "type": "multiple_choice",
        "question": "Rezeksiyon sonrası karaciğer hipertrofisi ne zaman ve neden oluşur?",
        "options": [
            "Hemen — cerrahi sırasında",
            "Haftalar-aylar içinde — remnant karaciğer kalan porsiyon için kompansatuvar büyüme",
            "Yıllarca sürer",
            "Hipertrofi olmaz"
        ],
        "correct": 1,
        "explanation": "Karaciğer rezeksiyonu sonrası remnant hepatosit proliferasyonu başlar. İlk haftalarda hızlı, sonra yavaşlar. 6-8 haftada işlevsel hacmin %80-90'ı restore edilebilir. Portal ven embolizasyonu (PVE) bu büyümeyi preoperatif stimüle etmek için kullanılır — küçük remnant lob için. Görüntülemede kontralateral lob büyümesi beklenen bulgu.",
        "level": 5
    },

    # ── SEVİYE 6: MULTİMODAL ─────────────────────────────────────────────────

    {
        "id": "extra_mdt_2",
        "concept_id": "multimodal_mdt_radiology",
        "type": "multiple_choice",
        "question": "TACE planlaması için radyolojun MDT'ye sunması gereken en kritik bilgi nedir?",
        "options": [
            "Lezyon boyutu",
            "Hepatik arter anatomisi (Michel sınıflaması varyantları) + portal ven açıklığı + tümör besleme damarı",
            "Child-Pugh skoru",
            "AFP değeri"
        ],
        "correct": 1,
        "explanation": "TACE için radyoloj anatomi raporu: (1) Hepatik arter varyantı — varyant arterden TACE yapılabilir mi, (2) Portal ven açıklığı — portal trombozu TACE kontrendikasyonu, (3) Tümörü besleyen spesifik damar — superselectif kateterizasyon için. Girişimsel radyolog bu bilgi olmadan güvenli TACE yapamaz.",
        "level": 6
    },
    {
        "id": "extra_surveillance_2",
        "concept_id": "multimodal_surveillance_strategy",
        "type": "multiple_choice",
        "question": "HBV pozitif ancak siroz olmayan hastada HKH surveyansı gerekli midir?",
        "options": [
            "Hayır — siroz olmadan risk yok",
            "Evet, belirli kriterlerde — 40 yaş üstü erkek, HBV DNA yüksek veya aile öyküsü",
            "Sadece kemoterapi alanlarda",
            "Sadece HBeAg pozitif olanlarda"
        ],
        "correct": 1,
        "explanation": "HBV integrasyon mekanizmasıyla siroz olmadan da HKH oluşabilir. AASLD 2023: siroz olmayan HBV hastasında surveyans endikasyonları: (1) Asiralı veya Afrika kökenli erkek >40 yaş, (2) Asialı kadın >50 yaş, (3) Ailede HKH öyküsü, (4) Yüksek viral yük. Bu grupta 6 ayda US + AFP önerilir.",
        "level": 6
    },
    {
        "id": "extra_ct_mr_2",
        "concept_id": "multimodal_ct_to_mr",
        "type": "multiple_choice",
        "question": "BT ile MR'ın karaciğer HKH tespitindeki duyarlılık farkı nedir?",
        "options": [
            "BT daha sensitif",
            "MR daha sensitif özellikle küçük lezyonlarda — MR %61-82 vs BT %48-66 (meta-analiz)",
            "İkisi eşit",
            "BT'nin spesifisitesi daha düşük"
        ],
        "correct": 1,
        "explanation": "HKH tespitinde MR > BT (özellikle <2 cm). Meta-analiz verileri: MR duyarlılığı %61-82, BT %48-66. Gadoxetat MR HBP ile ek bilgi sağlar. Ancak BT daha hızlı, geniş alan kaplama ve vasküler invazyon değerlendirmesinde üstün. Pratik yaklaşım: BT evreleme, MR karakterizasyon ve transplant değerlendirmesi için.",
        "level": 6
    },
    {
        "id": "extra_reporting_2",
        "concept_id": "multimodal_reporting_structured",
        "type": "multiple_choice",
        "question": "LI-RADS raporlamasında 'LR-NC' kategorisi ne zaman kullanılır?",
        "options": [
            "Normal karaciğer",
            "Görüntü kalitesi yetersiz veya faz atlanmış — kategorize edilemeyen lezyon",
            "Kesin HKH",
            "Benign lezyon"
        ],
        "correct": 1,
        "explanation": "LR-NC (Not Categorizable): teknik yetersizlik nedeniyle kategori verilemeyen durum. Örnekler: arteryel faz kalitesi bozuk (gadoxetat artefaktı), hasta hareketi, faz atlanması. Raporda nedenin açıklanması ve tekrar görüntüleme önerilmesi gerekir. Klinisyene 'belirsiz' mesajı verilmemelidir.",
        "level": 6
    },
    {
        "id": "extra_treatment_2",
        "concept_id": "multimodal_treatment_response",
        "type": "multiple_choice",
        "question": "LR-TR Viable kategorisinin klinik önemi nedir?",
        "options": [
            "Tedavi başarılı — izlem yeterli",
            "Canlı tümör var — retreatment veya tedavi değişikliği gerekli",
            "Beklenen değişiklik",
            "Belirsiz — 3 ayda tekrar"
        ],
        "correct": 1,
        "explanation": "LR-TR Viable: nodüler APHE veya washout — canlı tümör dokusu. Tedavi başarısız veya yetersiz. Aksiyon: MDT tartışması, tekrar ablasyon, TACE veya tedavi değişikliği (TARE, sistemik). LR-TR Equivocal ise 3 ayda tekrar değerlendirme. LR-TR Nonviable ise başarılı tedavi — surveyans devam.",
        "level": 6
    },
    {
        "id": "extra_ceus_2",
        "concept_id": "multimodal_ceus_role",
        "type": "multiple_choice",
        "question": "CEUS'ta bowel gas artefaktı sorunu neden BT/MR'a kıyasla daha az sorun yaratır?",
        "options": [
            "CEUS daha yüksek frekanslı ses kullanır",
            "Mikrobalonlar bowel gas'ı geçer — ancak bowel gas CEUS'ta da sorun yaratır, avantaj gerçek zamanlı ve dinamik izlem",
            "CEUS 3 boyutlu",
            "CEUS geniş görüntüleme alanı sağlar"
        ],
        "correct": 1,
        "explanation": "CEUS'ta bowel gas sorun yaratmaya devam eder (US fiziği aynı). Ancak CEUS'un temel avantajı gerçek zamanlı ve dinamik kontrastlı görüntüleme: arteryel fazın tam zamanlaması ve periferik nodüler fill-in'in gerçek zamanlı izlemi. BT'de çok kısa arteryel faz penceresi sabit zamanlı alınır; CEUS'ta kaçırma riski azalır.",
        "level": 6
    },
    {
        "id": "extra_sequences_2",
        "concept_id": "multimodal_liver_mr_sequences_guide",
        "type": "multiple_choice",
        "question": "Karaciğer MR'ında VIBE (volumetric interpolated breath-hold examination) sekansı ne için kullanılır?",
        "options": [
            "T2 görüntüleme",
            "3D T1 gradient echo — nefes tutmayla kontrast öncesi ve sonrası multifazik görüntüleme",
            "Difüzyon",
            "MRCP"
        ],
        "correct": 1,
        "explanation": "VIBE: 3 boyutlu, hızlı, nefes tutmayla T1 GRE sekansı. Karaciğer multifazik görüntülemede standarttır. Ince kesit (1-3 mm), isotropik voxel, multiplanar reformat imkanı. Kontrast öncesi + arteryel + portal venöz + geç fazlar VIBE ile alınır. Siemens terminolojisi; Philips'te THRIVE, GE'de LAVA adlarını alır.",
        "level": 6
    },

    # ── YENİ TANILARA SORULAR ─────────────────────────────────────────────────

    {
        "id": "extra_klatskin_2",
        "concept_id": "dd_biliary_dilation_algorithm",
        "type": "multiple_choice",
        "question": "Klatskin tümöründe en önemli rezektabilite kriteri nedir?",
        "options": [
            "Tümör boyutu <3 cm",
            "Bilateral sekonder safra yollarının tutulmaması + portal ven ve hepatik arterin bilateral invazyonu olmaması",
            "AFP değeri",
            "Lenf nodu durumu"
        ],
        "correct": 1,
        "explanation": "Klatskin rezektabilite: (1) Biliyer tutulum: Bismuth I-IIIb rezektabl, IV genellikle değil, (2) Vasküler invazyon: bilateral portal ven veya hepatik arter invazyonu irrezektabilite, (3) Yeterli remnant karaciğer hacmi. MDCT+MRCP kombinasyonu ile preoperatif değerlendirme şart. Biliyer drenaj görüntülemeden sonra yapılmalı.",
        "level": 4
    },
    {
        "id": "extra_pbc_1",
        "concept_id": "liver_systematic_reading",
        "type": "multiple_choice",
        "question": "Primer biliyer kolanjit (PBK) hangi antikor ile tanınır?",
        "options": [
            "ANCA",
            "Anti-mitokondriyal antikor (AMA-M2) — %95 sensitivite",
            "Anti-smooth muscle antikor",
            "ANA"
        ],
        "correct": 1,
        "explanation": "PBK'da AMA-M2 (anti-mitokondriyal antikor) %95 sensitivite ve %98 spesifisite gösterir. Görüntülemede intahepatik safra yolları tutulumu (PSK'dan farklı — ekstrahepatik tutulum nadir). Siroza ilerleyince HKH surveyansı gerekir. Ursodeoksikolik asit (UDCA) tedavisi hastalık progresyonunu yavaşlatır.",
        "level": 2
    },
    {
        "id": "extra_nash_2",
        "concept_id": "liver_fatty_infiltration",
        "type": "multiple_choice",
        "question": "NASH'ın siroza ilerleme hızı diğer etiyolojilere kıyasla nasıldır?",
        "options": [
            "Çok hızlı — 1-2 yılda siroz",
            "Yavaş — yıllar-onlarca yıl, ama küresel obezite epidemisi nedeniyle HKH'nın artan nedeni",
            "Hiç sirotik olmaz",
            "Sadece alkoliklerde olur"
        ],
        "correct": 1,
        "explanation": "NASH yavaş ilerler: basit steatozdan F4 siroza ortalama 10-20+ yıl. Ancak obezite ve diyabet prevalansı nedeniyle NASH kökenli HKH giderek artmakta ve bazı bölgelerde HBV/HCV'yi geçmektedir. Radyolojik olarak: siroz + steatoz + bilinen risk faktörleri (obezite, DM2) = NASH etiyolojisi düşündürür.",
        "level": 2
    },
    {
        "id": "extra_peliosis_1",
        "concept_id": "dd_multiple_lesions",
        "type": "multiple_choice",
        "question": "Peliozis hepatis hangi ilaçlar veya durumlarla ilişkilidir?",
        "options": [
            "Metformin ve statinler",
            "Anabolik steroidler, OKS, azatioprin, HIV (Bartonella)",
            "NSAIDlar",
            "Antihipertansifler"
        ],
        "correct": 1,
        "explanation": "Peliozis hepatis: sinüzoidal dilatasyon ve kan göllenmesi. Nedenler: anabolik steroidler, oral kontraseptifler, azatioprin, tamoksifen. HIV hastasında Bartonella henselae enfeksiyonu da peliozise yol açabilir. İlaç kesilince çoğu vaka geriler. Görüntüleme: değişken enhancement, US'de heterojen.",
        "level": 4
    },
    {
        "id": "extra_combined_hcc_icc_1",
        "concept_id": "pitfall_hcc_mimics",
        "type": "multiple_choice",
        "question": "Kombine HKH-ICC lezyonu görüntülemede nasıl şüphelenilir?",
        "options": [
            "Tipik HKH paterni — LR-5",
            "Karma özellikler: APHE + washout (HKH like) VEYA periferik enhancement + geç persistan (ICC like) — LR-M kategorisi",
            "Her zaman küçük lezyon",
            "Satellit lezyon karakteristik"
        ],
        "correct": 1,
        "explanation": "Kombine HKH-ICC: her iki tümörün özelliklerini taşır. Görüntülemede atipik patern — hem HKH hem ICC kriterlerini tam karşılamayan. LR-M kategorisi şüpheyi ifade eder. Biyopsi ile tanı konur: immünohistokimyada hem hepatoselüler (AFP, Arginaz-1) hem biliyer (CK7, CK19) markerleri pozitif.",
        "level": 5
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

print(f"\n── {len(QUESTIONS)} ek soru yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_questions)
    print(f"✓ {n} Question eklendi")

driver.close()
print(f"\n✓ Soru havuzu tamamlandı. Toplam eklenen: {len(QUESTIONS)}")

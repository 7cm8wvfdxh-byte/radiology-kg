from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

CONCEPTS = [

    # ── BT / MR PROTOKOLLERİ ─────────────────────────────────────────────────

    {
        "id": "liver_ct_protocol",
        "name": "Karaciğer BT Protokolleri — Endikasyona Göre Seçim",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Karaciğer BT protokolü endikasyona göre değişir. HKH şüphesi multifazik gerektirir. Travma tek fazla portal venöz yeterli olabilir. Doğru protokol seçimi teşhis kalitesini doğrudan etkiler.",
        "why_matters": "Yanlış protokol → yanlış zamanlama → APHE kaçırılır → HKH atlanır. Hangi endikasyonda hangi faz alınacağını bilmek hem teknik hem klinik sorumluluk.",
        "key_points": [
            "HKH tarama/tanı: Natif + Arteryel + Portal venöz + Geç faz (4 faz)",
            "Metastaz tarama: Portal venöz faz yeterli (hipovasküler metastaz burada belirgin)",
            "Hipervasküler metastaz şüphesi (NET, RCC): Arteryel + Portal venöz",
            "Travma: Portal venöz faz altın standart; şüpheli vasküler yaralanmada arteryel ekle",
            "Kolanjiyokarsinom: Portal + Geç faz (fibröz stroma geç fazda enhance eder)",
            "Kolesistit/safra yolu: Portal venöz + Geç faz yeterli",
            "Kontrastsız BT: spontan hiperdensite, kalsifikasyon, yağ değerlendirmesi"
        ],
        "source": "ACR Appropriateness Criteria, ESGAR 2024, Radiology RSNA Bae 2010"
    },
    {
        "id": "liver_mr_protocol",
        "name": "Karaciğer MR Protokolleri — Sekans Seçimi",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Karaciğer MR'ı çoklu sekans gerektirir. Temel sekanslar: T1 in/out phase, T2 FS, DWI, multifazik kontrast. Gadoxetat kullanılıyorsa 15-20. dakikada HBP eklenir.",
        "why_matters": "Her sekansın ne için kullanıldığını bilmeden MR raporu yorumlanamaz. T2'yi atlayan, DWI'ı değerlendirmeyen, HBP fazını kaçıran radyolog kritik tanıları atlar.",
        "key_points": [
            "T1 in/out phase: yağ içeriği (kimyasal kayma), kanama, proteinöz içerik",
            "T2 FS: kist (parlak), hemanjiom (parlak), malignite (hafif parlak)",
            "DWI b50/b400/b800 + ADC: hücresellik — malignite kısıtlar",
            "Multifazik kontrast: natif + arteryel + portal + geç (ekstraselüler ajan)",
            "HBP (gadoxetat): 15-20 dk — hepatosit fonksiyonu, FNH-adenom ayırımı",
            "MRCP: safra yolu anatomisi — non-invazif, iyonize radyasyon yok",
            "Gadoxetat arteryel faz: 1 mL/sn yavaş enjeksiyon önerilir (nefes artefaktı azalır)"
        ],
        "source": "ESGAR Consensus Statement, AJR Gadoxetate Part 1-2, RadioGraphics 2022"
    },

    # ── DİFFÜZ KARACİĞER HASTALIKLARI ────────────────────────────────────────

    {
        "id": "liver_hemochromatosis",
        "name": "Hemokromatoz — Demir Birikimi Görüntüleme",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Herediter hemokromatoz HFE gen mutasyonu ile demir birikimi. Karaciğerde T2* ve GRE sekanslarında belirgin sinyal düşümü karakteristik. Erken tanı siroz ve HKH gelişimini önler.",
        "why_matters": "T2'de karaciğer çok koyu görünüyorsa hemokromatoz düşün. Siderotik nodüller HKH ile karışabilir. MR demir miktarını non-invazif ölçer.",
        "key_points": [
            "MR T2* ve GRE: karaciğer sinyali çok düşük — demir manyetik susceptibility artefaktı",
            "Hepatik demir konsantrasyonu MR ile ölçülebilir (R2* relaxometry)",
            "Herediter: karaciğer + pankreas + kalp tutulumu",
            "Sekonder (transfüzyon): karaciğer + dalak + kemik iliği",
            "Siderotik nodüller: rejenerasyon nodülleri demir biriktirir → T2'de koyu",
            "Siderotik nodül → HKH: T2 sinyali artarsa upgrade → MR ile takip",
            "BT: diffüz karaciğer hiperdensite (demir yoğunluğu artmış)"
        ],
        "source": "EASL 2022, Radiology Key Iron Overload, ESGAR 2024"
    },
    {
        "id": "liver_wilson_disease",
        "name": "Wilson Hastalığı — Bakır Birikimi",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Otozomal resesif bakır metabolizması bozukluğu. Karaciğer, beyin (bazal ganglion), kornea (Kayser-Fleischer halkası) tutulur. MR görüntüleme özgün değil; siroz komplikasyonları önce gelir.",
        "why_matters": "Genç sirotik hastada Wilson akla gelmeli. BT'de bakır birikimi bazen hiperdensite yaratır. Nörolojik bulgular eşlik edebilir — multisistem düşün.",
        "key_points": [
            "Genç hastada (<40 yaş) açıklanamayan siroz → Wilson",
            "BT: karaciğer heterojenik, bazen diffüz hiperdensite (bakır birikimi)",
            "MR: özgün bulgu yok, siroz paterni + steatoz + heterojenik parankim",
            "Beyin MR: bazal ganglion T2 hiperintensitesi (nörolojik Wilson)",
            "Kayser-Fleischer halkası: yarık lamba muayenesi ile korneal bakır birikimi",
            "Tanı: serum serüloplazmin düşük + 24 saatlik idrarda bakır yüksek"
        ],
        "source": "EASL Wilson Disease Guidelines 2012, Radiology Key"
    },
    {
        "id": "liver_amyloidosis",
        "name": "Amiloidoz ve İnfiltratif Karaciğer Hastalıkları",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Amiloid, sarkoidoz, lenfoma ve lösemi karaciğere infiltre olabilir. Görüntüleme genellikle non-spesifik — hepatomegali + diffüz heterojenite. Biyopsi çoğu zaman gerekli.",
        "why_matters": "Hepatomegalinin tüm nedenleri görüntülemede aynı görünmez. İnfiltratif hastalıklarda lezyon olmayabilir — diffüz değişiklik ön planda.",
        "key_points": [
            "Amiloidoz: hepatomegali + diffüz düşük echogenite US'de + BT'de heterojenik",
            "Sarkoidoz: multiple hipodens nodüller — lenfoma gibi görünür",
            "Karaciğer lenfoma: hipodens kitleler, lenfadenopati, dalak tutulumu",
            "Lösemi/lenfoma infiltrasyonu: diffüz hepatomegali, fokal lezyon nadir",
            "Peliozis hepatis: sinüzoid dilatasyonu — ilaç/hormona bağlı, US'de heterojen",
            "Biyopsi: infiltratif hastalıkta görüntüleme yönlendirir ama tanı koymaz"
        ],
        "source": "ACG 2024, Radiology Key, EASL"
    },
    {
        "id": "liver_budd_chiari",
        "name": "Budd-Chiari Sendromu — Hepatik Ven Oklüzyonu",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Hepatik ven oklüzyonu sonucu karaciğer konjesyonu. Akut, subakut veya kronik olabilir. BT/MR'da karakteristik santral konjesyon + periferik atrofi + kaudat lob hipertrofisi.",
        "why_matters": "Kaudat lobun izole büyümesi Budd-Chiari'nin klasik işareti. Erken tanınmazsa kronik siroz ve portal HT gelişir. Antikoagülasyon ve TIPS kritik.",
        "key_points": [
            "Akut: karaciğer ödemi, asit, santral hipodens — bant şeklinde enhancement",
            "Kronik: kaudat lob hipertrofisi (kendi ayrı venöz drenajı IVC'ye),  periferik atrofi",
            "BT kontrast: santral karaciğer erken enhance, periferi geç — 'flip-flop' paterni",
            "MR: hepatik ven görülmez veya trombüs içerir",
            "Neden: hiperkoagülabilite (polisitemi vera, faktör V Leiden, OKS)",
            "Tedavi: antikoagülasyon + TIPS + karaciğer transplantasyonu"
        ],
        "source": "EASL 2018, Radiology Key, ACG 2024"
    },

    # ── KARACİĞER TRAVMASI ────────────────────────────────────────────────────

    {
        "id": "liver_trauma_aast",
        "name": "Karaciğer Travması — AAST Sınıflaması (2018)",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "AAST 2018 karaciğer yaralanma skalası BT bulgularına göre 5 grade tanımlar. Grade 1-3 genellikle nonoperatif yönetim. Grade 4-5 vasküler yaralanma içerir, cerrahi/anjiyoembolizasyon gerekebilir.",
        "why_matters": "Travma BT'si okurken AAST gradeini söylemek standardtır. Cerrahla iletişim bu dil üzerinden kurulur. Grade atlamak veya yanlış grade vermek yönetimi doğrudan etkiler.",
        "key_points": [
            "Grade I: subkapsüler hematom <%10, yüzeyel laserasyon <1 cm derinlik",
            "Grade II: subkapsüler %10-50, intraparankimal <10 cm, laserasyon 1-3 cm",
            "Grade III: subkapsüler >%50 veya rüptür, intraparankimal >10 cm, laserasyon >3 cm",
            "Grade IV: parankimal yıkım %25-75 hepatik lob veya 1-3 Couinaud segmenti",
            "Grade V: parankimal yıkım >%75 veya juxtahepatik venöz yaralanma",
            "2018 revizyonu: vasküler yaralanma (psödoanevrizma, AV fistül) grade artırır",
            "BT altın standart: arteryel + portal venöz faz — aktif kanama ve damar yaralanması"
        ],
        "source": "RadioGraphics AAST 2018 Revision, WSES 2020 Guidelines, ACR Appropriateness Criteria"
    },
    {
        "id": "liver_trauma_findings",
        "name": "Karaciğer Travması — BT Bulguları ve Tuzaklar",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Karaciğer travmasında BT'de laserasyon, hematom (subkapsüler/intraparankimal), aktif kanama, periportal ödem ve vasküler yaralanma aranır. Her bulgunun tanımlanması ve raporlanması kritik.",
        "why_matters": "Aktif kanamanın (kontrast extravazasyonu) atlanması hayati tehlike. Periportal düşük dansiteyi 'laserasyon' zannetmek hata — bu ödem veya safeveböyle lenfatik yaralanma olabilir.",
        "key_points": [
            "Laserasyon: parankimde lineer/yıldız şeklinde hipodens hat",
            "Subkapsüler hematom: karaciğer yüzeyinde kreşent şeklinde koleksiyon",
            "İntraparankimal hematom: karaciğer içi yuvarlak/oval hematom",
            "Aktif kanama: arteryel fazda kontrast extravazasyonu — kırmızı nokta işareti",
            "Periportal ödem: portal triady çevresinde düşük dansiteli halo — ödem/lenfatik",
            "Flat IVC: ağır hipovolemi işareti — acil",
            "Safra yolu yaralanması: geç komplikasyon — bilioma, MRCP ile değerlendir"
        ],
        "source": "RadioGraphics CT Blunt Liver Trauma, AAST 2018, ACR Trauma"
    },

    # ── TRANSPLANTASYON SONRASI ────────────────────────────────────────────────

    {
        "id": "liver_transplant_imaging",
        "name": "Karaciğer Transplantasyonu Sonrası Görüntüleme",
        "organ": "liver",
        "level": 2,
        "category": "technique",
        "summary": "Transplantasyon sonrası vasküler, biliyer ve parankimal komplikasyonlar izlenmelidir. US ilk basamak, Doppler kritik. Hepatik arter trombozu acil cerrahi gerektiren en ciddi komplikasyon.",
        "why_matters": "Transplant hastasında hepatik arter trombozu erken tespit edilmezse greft kaybı olur. US Doppler haftalık protokolü bu yüzden standarttır.",
        "key_points": [
            "Hepatik arter trombozu: Doppler'da akım yok — acil retransplantasyon",
            "Hepatik arter stenozu: tardus-parvus Doppler dalga formu, anastomoz hızı >200 cm/s",
            "Portal ven trombozu: Doppler'da dolma defekti, hepatofugal akım",
            "Safra yolu komplikasyonları: anastomoz striktürü, safra sızıntısı, biloma",
            "Rejeksiyon: görüntülemede non-spesifik — biyopsi gerekli",
            "Transplant sonrası HKH nüksü: US + AFP takibi",
            "Post-transplant lenfoproliferatif hastalık (PTLD): US/BT'de kitleler"
        ],
        "source": "EASL Transplant Guidelines, Radiology Key, ACR"
    },

    # ── KONJENİTAL ANOMALİLER ─────────────────────────────────────────────────

    {
        "id": "liver_caroli_disease",
        "name": "Caroli Hastalığı ve Konjenital Biliyer Anomaliler",
        "organ": "liver",
        "level": 2,
        "category": "pathology",
        "summary": "Caroli hastalığı: intrahepatik safra kanallarının konjenital sakkül dilatasyonu. İki tip: saf Caroli (kanal dilatasyonu) ve Caroli sendromu (konjenital hepatik fibrozis ile birlikte).",
        "why_matters": "Caroli'yi basit kist veya kistik tümörle karıştırmak ciddi hatadır. 'Merkezi nokta işareti' tanısal: dilate kanallar içinde portal ven dalları.",
        "key_points": [
            "Merkezi nokta işareti: dilate biliyer kanallar içinde portal ven dalları (BT/MR)",
            "MRCP'de safra kanallarıyla bağlantı gösterilebilir — kist değil kanal",
            "Komplikasyon: intrahepatik taş, kolanjit, kolanjiyokarsinom riski (%7)",
            "Caroli sendromu: konjenital hepatik fibrozis + portal HT eşlik eder",
            "Tedavi: hastalık yaygın ise transplantasyon, fokal ise rezeksiyon",
            "Polikistik karaciğer (PLD): çok sayıda basit kist, otozomal dominant"
        ],
        "source": "EASL 2022, Radiology Key Caroli, ACG 2024"
    },
    {
        "id": "liver_congenital_vascular",
        "name": "Konjenital Karaciğer Vasküler Anomalileri",
        "organ": "liver",
        "level": 2,
        "category": "anatomy",
        "summary": "Hepatik arter varyasyonları, portal ven anomalileri ve portosistemik şantlar görüntülemede önemli. Özellikle pre-op planlama ve transplantasyon değerlendirmesinde bilinmeli.",
        "why_matters": "Aberrant sağ hepatik arteri bilmeden yapılan pankreatikoduodenektomi kanama ile sonuçlanabilir. Konjenital portosistemik şant HKH taklidini yapabilir.",
        "key_points": [
            "Hepatik arter varyasyonları: Michel sınıflaması (9 tip)",
            "En sık varyant: sol hepatik arter gastrohepatic ligamandan (sol gastrik), sağ hepatik SMA'dan",
            "Konjenital portosistemik şant (Abernethy): portal kan IVC'ye direkt şant",
            "Tip 1 Abernethy: portal ven tamamen yoktur — transplantasyon gerekir",
            "Tip 2 Abernethy: parsiyel şant — HKH benzeri hipervasküler lezyon yapabilir",
            "Abernethy'de fokal nodüler hiperplazi ve HCA insidansı artmış"
        ],
        "source": "Radiology Key, EASL, RadioGraphics Abernethy"
    },
]

# ── ÖNKOŞUL İLİŞKİLERİ ───────────────────────────────────────────────────────
PREREQUISITES = [
    # BT/MR Protokolleri
    {"from": "liver_contrast_iodinated",   "to": "liver_ct_protocol"},
    {"from": "ct_principles",              "to": "liver_ct_protocol"},
    {"from": "liver_contrast_gadolinium",  "to": "liver_mr_protocol"},
    {"from": "mr_physics_t1_t2",           "to": "liver_mr_protocol"},
    {"from": "concept_dwi",               "to": "liver_mr_protocol"},

    # Diffüz hastalıklar
    {"from": "liver_physiology_function",  "to": "liver_hemochromatosis"},
    {"from": "mr_physics_t1_t2",           "to": "liver_hemochromatosis"},
    {"from": "liver_physiology_function",  "to": "liver_wilson_disease"},
    {"from": "liver_physiology_function",  "to": "liver_amyloidosis"},
    {"from": "portal_hypertension",        "to": "liver_budd_chiari"},
    {"from": "liver_anatomy_vasculature",  "to": "liver_budd_chiari"},

    # Travma
    {"from": "liver_ct_protocol",          "to": "liver_trauma_aast"},
    {"from": "liver_anatomy_segments",     "to": "liver_trauma_aast"},
    {"from": "liver_trauma_aast",          "to": "liver_trauma_findings"},
    {"from": "liver_contrast_iodinated",   "to": "liver_trauma_findings"},

    # Transplantasyon
    {"from": "liver_anatomy_vasculature",  "to": "liver_transplant_imaging"},
    {"from": "liver_biliary_anatomy",      "to": "liver_transplant_imaging"},
    {"from": "us_physics_liver",           "to": "liver_transplant_imaging"},

    # Konjenital
    {"from": "liver_biliary_anatomy",      "to": "liver_caroli_disease"},
    {"from": "liver_anatomy_vasculature",  "to": "liver_congenital_vascular"},
    {"from": "liver_anatomy_segments",     "to": "liver_congenital_vascular"},
]

# ── CONCEPT → DIAGNOSIS ───────────────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "liver_hemochromatosis",   "diagnosis": "hcc",        "relation": "RISK_FACTOR_FOR"},
    {"concept": "liver_budd_chiari",       "diagnosis": "hcc",        "relation": "RISK_FACTOR_FOR"},
    {"concept": "liver_caroli_disease",    "diagnosis": "icc",        "relation": "RISK_FACTOR_FOR"},
    {"concept": "liver_ct_protocol",       "diagnosis": "hcc",        "relation": "TECHNIQUE_FOR"},
    {"concept": "liver_mr_protocol",       "diagnosis": "hcc",        "relation": "TECHNIQUE_FOR"},
    {"concept": "liver_mr_protocol",       "diagnosis": "fnh",        "relation": "TECHNIQUE_FOR"},
    {"concept": "liver_mr_protocol",       "diagnosis": "hca",        "relation": "TECHNIQUE_FOR"},
    {"concept": "liver_congenital_vascular","diagnosis": "fnh",       "relation": "ASSOCIATED_WITH"},
    {"concept": "liver_congenital_vascular","diagnosis": "hca",       "relation": "ASSOCIATED_WITH"},
]

# ── SORULAR ───────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_ct_protocol_hcc",
        "concept_id": "liver_ct_protocol",
        "type": "multiple_choice",
        "question": "HKH şüpheli bir hastada multifazik karaciğer BT'de kaç faz alınır?",
        "options": [
            "Sadece portal venöz faz yeterli",
            "Natif + Arteryel + Portal venöz — 3 faz",
            "Natif + Arteryel + Portal venöz + Geç faz — 4 faz",
            "Sadece arteryel faz yeterli"
        ],
        "correct": 2,
        "explanation": "HKH tanısı için 4 faz gerekir: Natif (spontan hiperdensite ekarte), Arteryel (APHE değerlendirme), Portal venöz (washout değerlendirme), Geç faz (enhancing kapsül). Portal venöz faz tek başına yetersiz — APHE kaçırılır. ACR ve ESGAR protokolleri 4 faz önermektedir.",
        "level": 2
    },
    {
        "id": "q_mr_protocol_gadoxetate",
        "concept_id": "liver_mr_protocol",
        "type": "multiple_choice",
        "question": "Gadoxetat (Primovist) kullanılan MR'da hepatobiliyer faz ne zaman elde edilir?",
        "options": [
            "Kontrast enjeksiyonundan hemen sonra (1-2 dk)",
            "Portal venöz fazla eş zamanlı (60-70 sn)",
            "Enjeksiyondan 15-20 dakika sonra",
            "Enjeksiyondan 1 saat sonra"
        ],
        "correct": 2,
        "explanation": "Gadoxetat OATP1B1/B3 taşıyıcıları ile hepatositlere alınır. Yeterli hepatosit tutulumu için 15-20 dakika gerekmektedir. ESGAR: yeterli HBP = intrahepatic damar sinyali karaciğer parankiminden daha düşük olduğunda. Bu fazda FNH hiperintens, adenom/HKH hipointens görünür.",
        "level": 2
    },
    {
        "id": "q_hemochromatosis_mr",
        "concept_id": "liver_hemochromatosis",
        "type": "multiple_choice",
        "question": "Herediter hemokromatozda MR T2* görüntülemede ne beklenir?",
        "options": [
            "Karaciğer sinyalinde artış — demir T2'yi uzatır",
            "Karaciğer sinyalinde belirgin düşüş — demir manyetik susceptibility artefaktı",
            "Fokal hiperdens lezyon",
            "Diffüz T2 hiperintensite"
        ],
        "correct": 1,
        "explanation": "Demir güçlü paramagnetik özelliği nedeniyle T2* sekanslarında susceptibility artefaktı oluşturur — karaciğer sinyali belirgin düşer, neredeyse siyaha döner. Herediter hemokromatozda karaciğer + pankreas + kalp etkilenir. Sekonder (transfüzyon): karaciğer + dalak + kemik iliği. MR ile hepatik demir konsantrasyonu R2* relaxometry ile sayısal olarak ölçülebilir.",
        "level": 2
    },
    {
        "id": "q_aast_grade",
        "concept_id": "liver_trauma_aast",
        "type": "multiple_choice",
        "question": "BT'de karaciğerde subkapsüler hematom (%60 yüzey alanı) + aktif kontrast extravazasyonu saptanıyor. AAST grade kaçtır?",
        "options": [
            "Grade II",
            "Grade III",
            "Grade IV",
            "Grade V"
        ],
        "correct": 2,
        "explanation": "Subkapsüler hematom >%50 = Grade III. Ancak 2018 revizyonuna göre vasküler yaralanma (aktif kanama = kontrast extravazasyonu) bulunması durumunda grade IV'e yükseltilir. Final grade her zaman en yüksek kriterden alınır. Bu hasta anjiyoembolizasyon veya cerrahi değerlendirme gerektirir.",
        "level": 2
    },
    {
        "id": "q_budd_chiari",
        "concept_id": "liver_budd_chiari",
        "type": "multiple_choice",
        "question": "Budd-Chiari sendromunda kronik fazda karaciğerin hangi bölümü büyür ve neden?",
        "options": [
            "Sağ lob — en iyi perfüze olan bölüm",
            "Sol lob — portal ven sol loba daha yakın",
            "Kaudat lob — kendi venöz drenajı IVC'ye bağımsız",
            "Her bölüm eşit büyür"
        ],
        "correct": 2,
        "explanation": "Kaudat lobun hepatik venöz drenajı, sağ/sol hepatik venlerden bağımsız olarak doğrudan IVC'ye açılır. Bu nedenle hepatik ven oklüzyonunda kaudat lob konjesyondan korunur ve kompansatuvar olarak büyür. Bu Budd-Chiari'nin klasik ve patognomonik görüntüleme bulgusudur.",
        "level": 2
    },
    {
        "id": "q_caroli_sign",
        "concept_id": "liver_caroli_disease",
        "type": "multiple_choice",
        "question": "Caroli hastalığının BT/MR'daki patognomik bulgusu nedir?",
        "options": [
            "Karaciğerde çok sayıda basit kist",
            "Santral nokta işareti — dilate biliyer kanallar içinde portal ven dalları",
            "Diffüz safra yolu dilatasyonu",
            "Karaciğer içi kalsifikasyonlar"
        ],
        "correct": 1,
        "explanation": "Merkezi nokta (central dot) işareti: dilate intrahepatik biliyer kanallar içinde portal ven dallarının görülmesidir. BT ve MR'da kistik yapılar içinde kontrast tutan küçük noktalar olarak görünür. Bu bulgu Caroli'yi basit kistlerden veya kistik tümörlerden ayırır. MRCP ile safra kanallarıyla bağlantı da gösterilebilir.",
        "level": 2
    },
    {
        "id": "q_transplant_complication",
        "concept_id": "liver_transplant_imaging",
        "type": "multiple_choice",
        "question": "Karaciğer transplantasyonu sonrası ilk haftalarda en ciddi ve acil tedavi gerektiren vasküler komplikasyon hangisidir?",
        "options": [
            "Portal ven stenozu",
            "Hepatik ven trombozu",
            "Hepatik arter trombozu",
            "IVC darlığı"
        ],
        "correct": 2,
        "explanation": "Hepatik arter trombozu (HAT) transplantasyon sonrası en ciddi vasküler komplikasyondur — greft kaybına ve ölüme yol açabilir. Erken HAT (%4-12) akut karaciğer yetmezliği ile prezente olur. Doppler US'de hepatik arterde akım yokluğu veya tardus-parvus dalga formu erken bulgu. Acil retransplantasyon veya revaskülasyon gerektirir.",
        "level": 2
    },
    {
        "id": "q_liver_trauma_active_bleeding",
        "concept_id": "liver_trauma_findings",
        "type": "multiple_choice",
        "question": "Travma BT'sinde aktif hepatik kanamanın BT bulgusu nedir?",
        "options": [
            "Karaciğerde hipodens laserasyon hattı",
            "Arteryel fazda lezyonda kontrast extravazasyonu (kırmızı nokta işareti)",
            "Periportal düşük dansiteli halo",
            "Subkapsüler hematom"
        ],
        "correct": 1,
        "explanation": "Aktif kanama: arteryel fazda kontrast extravazasyonu — 'kırmızı nokta' veya 'aktif blush' olarak adlandırılır. Kontrast portal/geç fazda büyür veya yayılır. Bu bulgu acil anjiyoembolizasyon veya cerrahi endikasyonudur. Laserasyon, periportal ödem ve hematom aktif kanama işareti değil — statik yaralanma bulgularıdır.",
        "level": 2
    },
]


# ── SEED FONKSİYONLARI ────────────────────────────────────────────────────────

def seed_concepts(tx):
    for c in CONCEPTS:
        tx.run("""
            MERGE (c:Concept {id: $id})
            SET c.name = $name, c.organ = $organ, c.level = $level,
                c.category = $category, c.summary = $summary,
                c.why_matters = $why_matters, c.key_points = $key_points,
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
            SET q.concept_id = $concept_id, q.type = $type,
                q.question = $question, q.options = $options,
                q.correct = $correct, q.explanation = $explanation,
                q.level = $level
        """, **q)
        tx.run("""
            MATCH (q:Question {id: $q_id})
            MATCH (c:Concept {id: $c_id})
            MERGE (q)-[:TESTS]->(c)
        """, q_id=q["id"], c_id=q["concept_id"])
    return len(QUESTIONS)


# ── ÇALIŞTIR ──────────────────────────────────────────────────────────────────
print("\n── Katman 2 tamamlama yükleniyor...")
with driver.session() as session:
    n = session.execute_write(seed_concepts)
    print(f"✓ {n} Concept düğümü")

with driver.session() as session:
    n = session.execute_write(seed_prerequisites)
    print(f"✓ {n} PREREQUISITE_OF ilişkisi")

with driver.session() as session:
    n = session.execute_write(seed_concept_diagnosis)
    print(f"✓ {n} RELATES_TO ilişkisi")

with driver.session() as session:
    n = session.execute_write(seed_questions)
    print(f"✓ {n} Question düğümü")

driver.close()
print(f"""
✓ Katman 2 tamamlandı.
  Yeni Concepts   : {len(CONCEPTS)}
  Yeni Önkoşullar : {len(PREREQUISITES)}
  Yeni Sorular    : {len(QUESTIONS)}
""")

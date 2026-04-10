from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

CONCEPTS = [
    {
        "id": "dd_jaundice_algorithm",
        "name": "Sarılık Ayırıcı Tanı Algoritması — Tıkayıcı vs Hepatoselüler",
        "organ": "liver",
        "level": 4,
        "category": "technique",
        "summary": "Sarılıkta görüntülemenin rolü: tıkayıcı (obstrüktif) vs hepatoselüler ayırımı. US ilk basamak — safra yolu dilatasyonu tıkayıcıya işaret eder. Seviye ve neden tespiti sıradaki adım.",
        "why_matters": "Sarılık acil serviste çok sık. Radyolog US raporunda 'intrahepatik safra yolları dilate' yazınca klinisyen ERCP veya PTC planlar. Doğru yönlendirme kritik.",
        "key_points": [
            "US ilk basamak: safra yolu dilatasyonu var mı?",
            "İntrahepatik dilatasyon + ekstrahepatik normal → hiler tıkanma",
            "Ekstrahepatik dilatasyon → distal tıkanma (taş, pankreas başı, ampüller)",
            "Tıkayıcı sarılık görüntüleme sırası: US → MRCP → BT evreleme",
            "Hepatoselüler sarılık: karaciğer parankimi patolojisi — görüntüleme non-spesifik",
            "Geçiş noktası (transition point): dilate ile normal safra yolu arasındaki seviye",
            "BT vs MRCP: BT vasküler invazyon için üstün, MRCP duktus tutulumu için"
        ],
        "source": "EASL 2022, ACG 2024, AJR Hilar CCA"
    },
    {
        "id": "dd_multiple_lesions",
        "name": "Çok Sayıda Karaciğer Lezyonu — Sistematik Yaklaşım",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "Karaciğerde çok sayıda lezyon: metastaz, lenfoma, multifokal HKH, multipl hemanjiom, apse, sarkoidoz. Klinik bağlam ve lezyon karakteristikleri birlikte değerlendirilmeli.",
        "why_matters": "Birden fazla lezyon görünce refleks 'metastaz' tehlikeli. Multipl hemanjiom çok sık. Lezyon karakteristiklerine sistematik bakmadan karar vermek hata.",
        "key_points": [
            "Tüm lezyonlar aynı görünüyor + bilinen primer → Metastaz önce",
            "Tüm lezyonlar T2 ampul bulb + fill-in → Multipl hemanjiom",
            "Çok küçük (<1 cm) multipl + immünosüprese → Fungal mikro-apse",
            "Siroz + multipl nodül → Multifokal HKH — LI-RADS her lezyon için ayrı",
            "Multipl hipodens + lenfadenopati + splenomegali → Lenfoma",
            "Multipl + kalsifiye + kemoterapi öyküsü → Burn-out metastaz",
            "Değişken boyut + değişken görünüm → Primer ve sekonder birlikte olabilir"
        ],
        "source": "ACG 2024, LI-RADS v2018, Radiology Key"
    },
    {
        "id": "dd_liver_size_evaluation",
        "name": "Karaciğer Boyutu Değerlendirmesi — Hepatomegali ve Atrofi",
        "organ": "liver",
        "level": 4,
        "category": "technique",
        "summary": "Normal karaciğer boyutu, hepatomegali kriterleri ve lobar atrofi değerlendirmesi. Boyut değişikliği patolojinin göstergesi olabilir.",
        "why_matters": "Hepatomegali 'büyük karaciğer' demek değil — nedenini söylemek lazım. Sağ lob atrofisi + kaudat büyüme Budd-Chiari işareti. Raporlama standardı.",
        "key_points": [
            "Normal KC kranio-kaudal çap: <15 cm mid-klavikular hatta",
            "Hepatomegali nedenleri: konjesyon, infiltrasyon, depolama hastalığı, yağlanma",
            "Sağ lob atrofisi + kaudat büyüme → Budd-Chiari (portal ven tıkanması da)",
            "Sol lob hipertrofisi + sağ lob atrofisi → Kronik portal ven oklüzyonu",
            "Lobar atrofi + ipsilateral safra yolu dilatasyonu → Kolanjiyokarsinom",
            "Diffüz küçük KC + nodüler kontur → Siroz (end-stage)",
            "BT volumetri: transplantasyon öncesi remnant hacim hesabı"
        ],
        "source": "Radiology Key, ACR, EASL 2018"
    },
    {
        "id": "dd_fever_liver_lesion",
        "name": "Ateş + Karaciğer Lezyonu — Klinik Entegrasyon",
        "organ": "liver",
        "level": 4,
        "category": "pathology",
        "summary": "Ateş eşliğinde karaciğer lezyonu: apse, kolanjit, ekinokokkoz, tümör nekrozu veya lenfoma. Klinik bulgular görüntülemeyi tamamlar.",
        "why_matters": "Ateşli hastada karaciğer lezyonu = apse refleksi tehlikeli. Tümör nekrozu, lenfoma ve kolanjit de ateşle prezente olabilir. Sistematik ayırım şart.",
        "key_points": [
            "Ateş + lökositoz + sağ üst kadran ağrı → Apse önce",
            "Ateş + sarılık + titreme (Charcot üçlüsü) → Kolanjit — acil ERCP",
            "Ateş + karaciğer lezyonu + eozinofili → Parazitik (ekinokokkoz, askaris)",
            "Ateş + bilinen primer + yeni lezyon → Tümör nekrozu veya süperenfeksiyon",
            "Ateş + lenfadenopati + DWI kısıtlama → Lenfoma düşün",
            "CEUS apse tanısında yararlı: rim enhancement + merkez avasküler",
            "Amipli apse: seyahat öyküsü + tek büyük lezyon + seroloji pozitif"
        ],
        "source": "ACG 2024, EASL, Radiology Key"
    },
    {
        "id": "dd_post_chemotherapy_liver",
        "name": "Kemoterapi Sonrası Karaciğer Değişiklikleri",
        "organ": "liver",
        "level": 4,
        "category": "technique",
        "summary": "Kemoterapi karaciğerde sinüzoidal obstrüksiyon sendromu, steatohepatit ve pseudoprogresyon yapabilir. Bu değişiklikleri gerçek progresyondan ayırt etmek kritik.",
        "why_matters": "Kemoterapi sonrası 'yeni lezyon' veya 'büyüyen lezyon' her zaman tümör değil. Kemoterapi toksisitesi veya pseudoprogresyon olabilir. Yanlış yorum tedaviyi değiştirir.",
        "key_points": [
            "Sinüzoidal obstrüksiyon sendromu (SOS/VOD): periportal ödem + hepatomegali",
            "Steatohepatit: oxaliplatin sonrası NASH benzeri → yeşil karaciğer",
            "Pseudoprogresyon: immünoterapi sonrası geçici büyüme — sonra küçülme",
            "Kalsifiye metastaz: yanıt işareti — progresyon değil",
            "Burn-out: fibrotik skar + enhancement yok — aktif lezyon değil",
            "mRECIST: enhancing komponent ölçülür — nekroz dahil edilmez",
            "Karşılaştırmalı okuma zorunlu: önceki görüntülemelerle karşılaştırmadan rapor yazma"
        ],
        "source": "ACG 2024, mRECIST, Radiology Key Chemotherapy Liver"
    },
    {
        "id": "dd_biliary_dilation_algorithm",
        "name": "Safra Yolu Dilatasyonu — Seviye ve Neden Tespiti",
        "organ": "liver",
        "level": 4,
        "category": "technique",
        "summary": "Safra yolu dilatasyonunda radyolog iki soruyu cevaplamalı: hangi seviyede tıkanma var? Neden? MRCP bu soruları en iyi cevaplayan modalitedir.",
        "why_matters": "Doğru seviye tespiti cerrahiyi planlar. Hiler tıkanmada sağ-sol sistemler ayrı mı? Pankreas başında kitle mi? Bu sorular yanıtsız kalırsa ERCP boşa gider.",
        "key_points": [
            "Seviye 1 (intahepatik): periferik kanal dilatasyonu — hiler kitle veya karsinomatozis",
            "Seviye 2 (hilar): her iki sistem dilate, common hepatik normal → Klatskin",
            "Seviye 3 (suprapankreatik CBD): pankreas başı lezyonu, periampüller",
            "Normal CBD çapı: <7 mm (<10 mm kolesistektomi sonrası)",
            "MRCP altın standart: non-invazif, TÜM sistem gösterilir",
            "BT: kitle, vasküler invazyon, lenfadenopati için üstün",
            "Geçiş noktasının MPR ile gösterilmesi: 3 boyutlu değerlendirme şart"
        ],
        "source": "EASL 2022, ACG 2024, AJR MRCP"
    },
]

# ── ÖNKOŞULLAR ────────────────────────────────────────────────────────────────
PREREQUISITES = [
    {"from": "liver_biliary_anatomy",      "to": "dd_jaundice_algorithm"},
    {"from": "liver_systematic_reading",   "to": "dd_jaundice_algorithm"},
    {"from": "liver_lab_tests",           "to": "dd_jaundice_algorithm"},
    {"from": "liver_biliary_anatomy",      "to": "dd_biliary_dilation_algorithm"},
    {"from": "dd_jaundice_algorithm",      "to": "dd_biliary_dilation_algorithm"},

    {"from": "metastasis_patterns_full",   "to": "dd_multiple_lesions"},
    {"from": "hemangioma_variants",        "to": "dd_multiple_lesions"},
    {"from": "lirads_lr_categories_decision","to": "dd_multiple_lesions"},

    {"from": "liver_anatomy_segments",     "to": "dd_liver_size_evaluation"},
    {"from": "liver_cirrhosis_imaging",    "to": "dd_liver_size_evaluation"},
    {"from": "liver_budd_chiari",          "to": "dd_liver_size_evaluation"},

    {"from": "liver_abscess_types",        "to": "dd_fever_liver_lesion"},
    {"from": "dd_multiple_lesions",        "to": "dd_fever_liver_lesion"},

    {"from": "pitfall_burnout_metastasis", "to": "dd_post_chemotherapy_liver"},
    {"from": "metastasis_patterns_full",   "to": "dd_post_chemotherapy_liver"},
    {"from": "liver_systematic_reading",   "to": "dd_post_chemotherapy_liver"},
]

# ── CONCEPT → DIAGNOSIS ───────────────────────────────────────────────────────
CONCEPT_DIAGNOSIS = [
    {"concept": "dd_jaundice_algorithm",       "diagnosis": "klatskin_tumor", "relation": "DIAGNOSTIC_PATHWAY"},
    {"concept": "dd_jaundice_algorithm",       "diagnosis": "psc",            "relation": "DIAGNOSTIC_PATHWAY"},
    {"concept": "dd_biliary_dilation_algorithm","diagnosis": "klatskin_tumor", "relation": "TECHNIQUE_FOR"},
    {"concept": "dd_multiple_lesions",         "diagnosis": "metastasis",     "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_multiple_lesions",         "diagnosis": "liver_lymphoma", "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_fever_liver_lesion",       "diagnosis": "abscess",        "relation": "DIFFERENTIAL_FOR"},
    {"concept": "dd_post_chemotherapy_liver",  "diagnosis": "metastasis",     "relation": "PITFALL_FOR"},
]

# ── SORULAR ───────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "id": "q_jaundice_level",
        "concept_id": "dd_jaundice_algorithm",
        "type": "multiple_choice",
        "question": "US'de intrahepatik safra yolları dilate, ekstrahepatik CBD normal. Tıkanma seviyesi nerede?",
        "options": [
            "Distal CBD — pankreas başı",
            "Sfinkter Oddi seviyesi",
            "Hiler bölge — bifürkasyon",
            "Hepatoselüler sarılık — safra yolu tıkanması yok"
        ],
        "correct": 2,
        "explanation": "İntrahepatik dilatasyon + normal ekstrahepatik CBD → tıkanma hiler bölgede (bifürkasyon veya hemen üstü). Klatskin tümörü, hilar metastaz, Caroli hastalığı ayırıcı tanılar. Distal tıkanma (pankreas başı, taş) ekstrahepatik CBD'yi de genişletir.",
        "level": 4
    },
    {
        "id": "q_multiple_t2_bright",
        "concept_id": "dd_multiple_lesions",
        "type": "multiple_choice",
        "question": "Bilinen malignite olmayan hastada karaciğerde 5-6 adet, değişken boyutta, T2 ampul bulb gösteren, periferik nodüler enhancement + fill-in lezyonlar. Tanı?",
        "options": [
            "Metastaz — bilinen primer yoksa da ekarte edilmeli",
            "Multipl hemanjiom — T2 ampul bulb + fill-in patern tanısal",
            "Multifokal HKH — LI-RADS değerlendirmesi",
            "Fungal apse — multipl küçük lezyonlar"
        ],
        "correct": 1,
        "explanation": "T2 ampul bulb + periferik nodüler enhancement + progresif fill-in → multipl hemanjiom. Bilinen malignite yoksa ve tüm lezyonlar aynı tipik patern gösteriyorsa biyopsi gerekmez. Onkoloji hastasında aynı bulgular görülse bile hemanjiom düşünülmeli — biyopsi veya CEUS ile konfirme edilir.",
        "level": 4
    },
    {
        "id": "q_charcot_triad",
        "concept_id": "dd_fever_liver_lesion",
        "type": "multiple_choice",
        "question": "Ateş + sarılık + sağ üst kadran ağrısı (Charcot üçlüsü). Görüntülemede ne aranır ve acil yapılacak işlem nedir?",
        "options": [
            "Karaciğer lezyonu — biyopsi",
            "Safra yolu dilatasyonu + tıkanma nedeni — acil ERCP/PTC",
            "HKH — multifazik BT",
            "Apse — drenaj"
        ],
        "correct": 1,
        "explanation": "Charcot üçlüsü = akut kolanjit. Akut kolanjit biliyer obstrüksiyon + bakteriyel enfeksiyon. US'de safra yolu dilatasyonu + tıkanma nedeni (taş, kitle) araştırılır. Acil dekompresyon gerekli: ERCP (tercih) veya PTC. Tedavi gecikmesi sepsis ve ölüme yol açar. Tokyo kriterleri 2018 kolanjit yönetimi için referans.",
        "level": 4
    },
    {
        "id": "q_post_chemo_calcification",
        "concept_id": "dd_post_chemotherapy_liver",
        "type": "multiple_choice",
        "question": "Kolorektal kanser kemoterapi sonrası kontrolde önceki 2 cm metastaz lokalizasyonunda 8 mm kalsifik odak. Yorum?",
        "options": [
            "Yeni lezyon — progresyon, tedavi değişikliği",
            "Radyolojik yanıt — burn-out/kalsifiye metastaz, aktif tümör değil",
            "Hidatik kist gelişimi",
            "Biyopsi gerekli — belirsiz"
        ],
        "correct": 1,
        "explanation": "Bilinen metastaz lokalizasyonunda küçülen + kalsifiye lezyon = radyolojik yanıt işareti. Burn-out/kalsifiye metastaz özellikle mucinöz kolorektal kanserde görülür. Enhancement yoksa aktif tümör değil. Önceki görüntülemelerle karşılaştırma şart. mRECIST: sadece en büyük enhancing komponent ölçülür.",
        "level": 4
    },
]


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

print("\n── Katman 4 ek conceptler yükleniyor...")
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
print(f"\n✓ Katman 4 tamamlandı — {len(CONCEPTS)} ek concept, {len(QUESTIONS)} soru")

import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hiphopologist API",
    description="Random Hiphopologist lyrics — like kanye.rest but Persian 💊",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

LINES = [
    # ── Ghors ──
    {"quote": "همه چی بعد تو شده شروع", "song": "Ghors"},
    {"quote": "شهر ما سیاهه عشق ما گرون", "song": "Ghors"},
    {"quote": "نمی‌گیریم از کسی اجازه", "song": "Ghors"},
    {"quote": "چشم‌هاتو وا کن", "song": "Ghors"},
    {"quote": "آسمون مال ما بود یادته؟", "song": "Ghors"},
    {"quote": "من که دست‌هاتو ول نمی‌کنم", "song": "Ghors"},
    {"quote": "بیا دوباره خاطره بسازیم", "song": "Ghors"},
    {"quote": "تو باد و برف و بارون", "song": "Ghors"},
    {"quote": "این جمعه دوتایی می‌کنیم فرار", "song": "Ghors"},
    {"quote": "فیریک‌ها میان و میرن تو بمون", "song": "Ghors"},
    {"quote": "بدن داغ تو برا من کوکه", "song": "Ghors"},
    # ── AZHIR ──
    {"quote": "هرجایی بحث رپ بود من اونجام", "song": "AZHIR"},
    {"quote": "دکتر کیه؟ خودمون مریضیم", "song": "AZHIR"},
    {"quote": "رپ‌کن بودم حتی تو کلینیک", "song": "AZHIR"},
    {"quote": "هاستلر احتیاج نداره اثبات", "song": "AZHIR"},
    {"quote": "هنوزم رپ می‌کنم واسه صلح", "song": "AZHIR"},
    {"quote": "منو ساکت نمی‌کنه این دفعه", "song": "AZHIR"},
    {"quote": "شدم پیکاسو، مثِ پیکاشون", "song": "AZHIR"},
    {"quote": "تو می‌خواستی بشم دکتر، پسرت لجند شده تو خیابون", "song": "AZHIR"},
    {"quote": "مازندران با من شده شیکاگو", "song": "AZHIR"},
    {"quote": "هر شب، هر صبح، هر روز و یکسره آژیر مامور و", "song": "AZHIR"},
    {"quote": "مامان هرشب برام می‌کرد گریه", "song": "AZHIR"},
    {"quote": "بیشتر گوش بده، باز کن چشمات", "song": "AZHIR"},
    # ── Nabz ──
    {"quote": "Traps بیشتر اَ پزشکی حال میده", "song": "Nabz"},
    {"quote": "احیاش کردم الان داره نبض", "song": "Nabz"},
    {"quote": "مافیاها منو دوس ندارن", "song": "Nabz"},
    {"quote": "دکتر رپ‌فا، نمیشه تسلیم", "song": "Nabz"},
    {"quote": "میشم جراح رپ، منو بِبُره", "song": "Nabz"},
    {"quote": "لیریکال جینیس میام بالا", "song": "Nabz"},
    {"quote": "قسم خوردم واس نجات آدما", "song": "Nabz"},
    {"quote": "اون سروش بود می‌رفت پِی بقیه، هیپ‌هاپولوژیست میره پِی خودش", "song": "Nabz"},
    # ── Rose ──
    {"quote": "من به کسی باج نمیدم", "song": "Rose"},
    {"quote": "هر روزو زندگی می‌کنم مث روز آخر", "song": "Rose"},
    {"quote": "آدما بهت راست نمیگن", "song": "Rose"},
    {"quote": "قلب آدما سیاهه آهن و پولی", "song": "Rose"},
    {"quote": "تنت پره زخمه اثر تیر قضاوت", "song": "Rose"},
    {"quote": "بدون ضد گلوله جلو گلوله‌هاتم", "song": "Rose"},
    {"quote": "شدم گرگ صاف نگاه کنم تو چشم هیولا", "song": "Rose"},
    {"quote": "برو علف آتیش بزن بیشتر از چهارشنبه‌سوری", "song": "Rose"},
    # ── Cardi ──
    {"quote": "رو صحنه می‌درخشم، انگار خدام", "song": "Cardi"},
    {"quote": "این بازی گرفت ازم رفیقامو", "song": "Cardi"},
    {"quote": "چون بودم قوی‌تر اَ آرزوهام", "song": "Cardi"},
    {"quote": "اَ رپ فا می‌کنم تجارت", "song": "Cardi"},
    {"quote": "خیابون الان برا منه", "song": "Cardi"},
    {"quote": "یه زمان پایین بودیم توی بندو، الانم نوک برج", "song": "Cardi"},
    # ── Nabayad ──
    {"quote": "من دقیقا شدم همون چیزی و که نباید", "song": "Nabayad"},
    {"quote": "پس زندگی کن به همون فرمولی که نباید", "song": "Nabayad"},
    {"quote": "نذاشتم آدما بکنن حال منو داغون", "song": "Nabayad"},
    {"quote": "داداشا کنارم می‌مونن، چاقالا فرارم می‌کنن", "song": "Nabayad"},
    {"quote": "اومدم بمونم نه اینکه فِید شم", "song": "Nabayad"},
    {"quote": "یه روز با پول میرم از این کشور", "song": "Nabayad"},
    {"quote": "یادم نمیره از کجا شد شروع", "song": "Nabayad"},
    {"quote": "مامان نگرانم نی، اگه ضعیف بودم اینا سوارم می‌شدن", "song": "Nabayad"},
]


@app.get("/")
def root():
    return {
        "name": "Hiphopologist API",
        "description": "Random Hiphopologist lyrics — like kanye.rest but Persian 💊",
        "endpoints": {
            "random quote": "GET /quote",
            "quote by song": "GET /quote?song=AZHIR",
            "all songs": "GET /songs",
            "all quotes": "GET /quotes",
        },
    }


@app.get("/quote")
def get_quote(song: str = None):
    pool = LINES
    if song:
        pool = [l for l in LINES if l["song"].lower() == song.lower()]
        if not pool:
            return {"error": f"No quotes found for song '{song}'"}
    return random.choice(pool)


@app.get("/songs")
def get_songs():
    songs = sorted(set(l["song"] for l in LINES))
    return {"songs": songs, "count": len(songs)}


@app.get("/quotes")
def get_all_quotes():
    return {"quotes": LINES, "count": len(LINES)}

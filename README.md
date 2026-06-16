# Hiphopologist API 💊
> Random Hiphopologist lyrics — like kanye.rest but Persian

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | API info |
| GET | `/quote` | Random lyric |
| GET | `/quote?song=AZHIR` | Random lyric from a specific song |
| GET | `/songs` | List all songs |
| GET | `/quotes` | All lyrics |

### Example response
```json
{
  "quote": "مازندران با من شده شیکاگو",
  "song": "AZHIR"
}
```

---

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://localhost:8000

---

## Deploy to Railway (free, recommended)

1. Go to https://railway.app and sign up (free)
2. Click **New Project → Deploy from GitHub repo**
3. Push these 3 files to a GitHub repo first:
   - `main.py`
   - `requirements.txt`
   - `Procfile`
4. Connect that repo on Railway
5. Railway auto-detects Python and deploys it
6. Click **Settings → Domains → Generate Domain**
7. Your API is live at something like `https://hiphopologist-api.up.railway.app/quote` 🎉

## Deploy to Render (alternative, also free)

1. Go to https://render.com and sign up
2. Click **New → Web Service**
3. Connect your GitHub repo
4. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **Deploy**
6. Your URL appears at the top of the dashboard

---

## Share with friends

Once live, your friends can use it like:
```js
const res = await fetch("https://your-url.railway.app/quote");
const data = await res.json();
console.log(data.quote); // Persian lyric 🔥
```

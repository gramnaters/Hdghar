"""
HDGharTV Stremio<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HDGharTV — Stremio Addon</title>
<link rel="icon" type="image/png" href="https://hdghartv.cc/favicon.png">
<link rel="apple-touch-icon" href="https://hdghartv.cc/logo.png">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
:root {
    --bg-color: #0a0a0c;
    --primary-accent: #E50914;
    --secondary-accent: #ff2a36;
    --text-main: #e5e5e5;
    --glass-border: rgba(229, 9, 20, 0.15);
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: 'Outfit', sans-serif;
    background-color: var(--bg-color);
    background-image:
        radial-gradient(circle at 50% 20%, rgba(229, 9, 20, 0.08) 0%, transparent 55%),
        radial-gradient(circle at 50% 85%, rgba(255, 42, 54, 0.05) 0%, transparent 45%);
    color: var(--text-main);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow-x: hidden;
}
.container {
    max-width: 480px;
    width: 100%;
    padding: 3rem 2rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.logo {
    width: 110px;
    height: 110px;
    margin-bottom: 1.5rem;
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 12px 40px rgba(229, 9, 20, 0.25);
    transform: rotate(-5deg);
    transition: transform 0.3s ease;
}
.logo:hover { transform: rotate(0deg) scale(1.05); }
.logo img { width: 100%; height: 100%; object-fit: cover; }
h1 {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
    background: linear-gradient(to right, #fff, var(--primary-accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 1.1rem;
    font-weight: 300;
    color: var(--text-main);
    margin-bottom: 2.5rem;
    line-height: 1.6;
}
.form-group {
    margin-bottom: 1.5rem;
    width: 100%;
    text-align: left;
}
.form-group label {
    display: block;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: rgba(255,255,255,0.6);
}
.select-wrap { position: relative; width: 100%; }
.select-wrap select {
    width: 100%;
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid var(--glass-border);
    background: rgba(255, 255, 255, 0.05);
    color: #fff;
    font-size: 1rem;
    font-family: 'Outfit', sans-serif;
    outline: none;
    appearance: none;
    cursor: pointer;
    transition: border-color 0.3s ease;
}
.select-wrap select:focus { border-color: var(--primary-accent); }
.select-wrap select option { background: #1a1a1e; color: #fff; }
.select-arrow {
    position: absolute; right: 1rem; top: 50%;
    transform: translateY(-50%); pointer-events: none;
    width: 16px; height: 16px; opacity: 0.5;
}
/* Manifest URL box — wider, rounded, shows full URL */
.manifest-box {
    width: 100%;
    margin-top: 0.5rem;
    margin-bottom: 0.85rem;
    padding: 0.85rem 1.25rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    font-family: 'Outfit', monospace;
    font-size: 0.78rem;
    color: rgba(255,255,255,0.5);
    word-break: break-all;
    text-align: center;
    line-height: 1.5;
    min-height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.btn-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.85rem;
    width: 100%;
}
.install-btn {
    display: inline-block;
    width: 100%;
    background: linear-gradient(135deg, var(--primary-accent), var(--secondary-accent));
    color: #fff;
    text-decoration: none;
    padding: 1.1rem 2rem;
    font-size: 1.15rem;
    font-weight: 800;
    border-radius: 50px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.3s ease;
    box-shadow: 0 8px 25px rgba(229, 9, 20, 0.25);
}
.install-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(229, 9, 20, 0.35);
}
.copy-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    width: 100%;
    background: transparent;
    color: var(--text-main);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 0.85rem 2rem;
    font-size: 0.95rem;
    font-weight: 500;
    font-family: 'Outfit', sans-serif;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
}
.copy-btn:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.25);
    color: #fff;
}
.copy-btn svg { width: 16px; height: 16px; fill: currentColor; opacity: 0.7; }
.nuvio-note {
    margin-top: 1rem;
    font-size: 0.75rem;
    color: rgba(255,255,255,0.3);
    text-align: center;
}
@media (max-width: 480px) {
    .container { padding: 2rem 1.25rem; }
    h1 { font-size: 2.4rem; }
}
</style>
</head>
<body>
<div class="container">
    <div class="logo">
        <img src="https://hdghartv.cc/logo.png" alt="HDGharTV">
    </div>
    <h1>HDGharTV</h1>
    <p class="subtitle">Movies & series with multi-audio support.<br>Select your preferences below.</p>

    <div class="form-group">
        <label>Audio Language</label>
        <div class="select-wrap">
            <select id="language">
                <option value="all">All Languages</option>
                <option value="hindi">Hindi</option>
                <option value="english">English</option>
                <option value="tamil">Tamil</option>
                <option value="telugu">Telugu</option>
                <option value="malayalam">Malayalam</option>
                <option value="punjabi">Punjabi</option>
                <option value="bengali">Bengali</option>
                <option value="marathi">Marathi</option>
                <option value="kannada">Kannada</option>
            </select>
            <svg class="select-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
    </div>

    <div class="form-group">
        <label>Category</label>
        <div class="select-wrap">
            <select id="category">
                <option value="all">All Categories</option>
                <option value="bollywood">Bollywood</option>
                <option value="hollywood">Hollywood</option>
                <option value="south indian">South Indian</option>
                <option value="punjabi">Punjabi</option>
            </select>
            <svg class="select-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
    </div>

    <div class="manifest-box" id="manifestUrl">Loading...</div>

    <div class="btn-group">
        <a href="#" id="install-link" class="install-btn">Install in Stremio</a>
        <button id="copy-btn" class="copy-btn">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
            Copy Manifest URL
        </button>
    </div>
    <div class="nuvio-note">For Nuvio: copy URL above &rarr; paste in addon settings.</div>
</div>
<script>
const installBtn = document.getElementById("install-link");
const copyBtn = document.getElementById("copy-btn");
const langSelect = document.getElementById("language");
const catSelect = document.getElementById("category");
const manifestBox = document.getElementById("manifestUrl");

function getConfigPath() {
    const lang = langSelect.value;
    const cat = catSelect.value;
    const configObj = {language: lang, category: cat};
    const encoded = btoa(JSON.stringify(configObj)).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
    return encoded + "/";
}

function getBaseUrl() {
    return window.location.href.replace(/\/$/, "");
}

function updateLinks() {
    const configPath = getConfigPath();
    const baseUrlRaw = window.location.href.replace("https://", "").replace("http://", "").replace(/\/$/, "");
    const manifestUrl = getBaseUrl() + "/" + configPath + "manifest.json";
    manifestBox.textContent = manifestUrl;
    installBtn.href = "stremio://" + baseUrlRaw + "/" + configPath + "manifest.json";
}

copyBtn.addEventListener("click", () => {
    const configPath = getConfigPath();
    const manifestUrl = getBaseUrl() + "/" + configPath + "manifest.json";
    navigator.clipboard.writeText(manifestUrl);
    const originalHTML = copyBtn.innerHTML;
    copyBtn.innerHTML = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg> Copied!';
    setTimeout(() => { copyBtn.innerHTML = originalHTML; }, 2000);
});

langSelect.addEventListener("change", updateLinks);
catSelect.addEventListener("change", updateLinks);
updateLinks();
</script>
</body>
</html>"""
import os
import httpx
from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
import base64

HDGHARTV_API = "https://hdghartv.cc/api"

app = FastAPI(title="HDGharTV Stremio Addon", version="2.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_client():
    return httpx.AsyncClient(timeout=15.0, follow_redirects=True)

async def fetch_api(path: str, params: dict = None):
    url = f"{HDGHARTV_API}{path}"
    async with await get_client() as client:
        r = await client.get(url, params=params)
    if r.status_code != 200:
        return None
    return r.json()

async def fetch_movie(movie_id: str):
    mongo_id = movie_id.replace("hdghar-movie-", "")
    return await fetch_api(f"/movies/public/{mongo_id}")

async def fetch_series(series_id: str):
    mongo_id = series_id.replace("hdghar-series-", "")
    return await fetch_api(f"/series/public/{mongo_id}")

def make_meta(item: dict, content_type: str) -> dict:
    item_id = item.get("_id", item.get("id", ""))
    stremio_id = f"hdghar-{content_type}-{item_id}"
    genres = []
    for g in item.get("genres", []):
        if isinstance(g, dict):
            genres.append(g.get("name", ""))
        elif isinstance(g, str):
            genres.append(g)
    poster = item.get("posterPath") or item.get("poster") or ""
    if poster and not poster.startswith("http"):
        poster = f"https://image.tmdb.org/t/p/original{poster}"
    return {
        "id": stremio_id,
        "type": content_type,
        "name": item.get("title", "Unknown"),
        "poster": poster,
        "background": item.get("backdropPath", poster),
        "genres": genres,
        "year": item.get("releaseDate", item.get("year", "")),
        "description": item.get("overview", ""),
        "imdbRating": str(item.get("voteAverage", "")) if item.get("voteAverage") else "",
    }

def parse_config(config_str: str) -> dict:
    try:
        padding = 4 - (len(config_str) % 4)
        if padding != 4:
            config_str += "=" * padding
        decoded = base64.urlsafe_b64decode(config_str).decode("utf-8")
        return json.loads(decoded)
    except Exception:
        return {}

# ============================================================
# Manifest
# ============================================================
def build_manifest(config: dict = None):
    language = config.get("language", "all") if config else "all"
    category = config.get("category", "all") if config else "all"
    catalogs = [
        {"type": "movie", "id": "hdghar-movies", "name": "All Movies"},
        {"type": "series", "id": "hdghar-series", "name": "All Series"},
        {"type": "movie", "id": "hdghar-bollywood", "name": "Bollywood"},
        {"type": "movie", "id": "hdghar-hollywood", "name": "Hollywood"},
        {"type": "movie", "id": "hdghar-south", "name": "South Indian"},
        {"type": "movie", "id": "hdghar-punjabi", "name": "Punjabi"},
        {"type": "movie", "id": "hdghar-trending", "name": "Trending"},
        {"type": "movie", "id": "hdghar-search", "name": "Search Movies", "extra": [{"name": "search", "isRequired": True}]},
        {"type": "series", "id": "hdghar-search-series", "name": "Search Series", "extra": [{"name": "search", "isRequired": True}]},
    ]
    return {
        "id": "com.hdghartv.stremio",
        "version": "2.1.0",
        "name": "HDGharTV",
        "description": f"Movies & series from HDGharTV — multi-audio. Lang: {language}, Cat: {category}",
        "logo": "https://hdghartv.cc/logo.png",
        "resources": ["catalog", "meta", "stream"],
        "types": ["movie", "series"],
        "idPrefixes": ["hdghar"],
        "catalogs": catalogs,
        "behaviorHints": {"configurable": True, "configurationRequired": False},
    }

@app.get("/manifest.json")
async def manifest_default():
    return build_manifest()

@app.get("/{config}/manifest.json")
async def manifest_configured(config: str):
    return build_manifest(parse_config(config))

# ============================================================
# Catalog (both default and configured)
# ============================================================
async def handle_catalog(catalog_id: str, content_type: str, config: dict = None):
    filter_lang = config.get("language", "all") if config else "all"
    filter_cat = config.get("category", "all") if config else "all"
    metas = []
    try:
        if catalog_id in ("hdghar-movies", "hdghar-bollywood", "hdghar-hollywood", "hdghar-south", "hdghar-punjabi", "hdghar-trending"):
            params = {"page": 1, "limit": 100}
            if catalog_id == "hdghar-trending":
                params["sort"] = "popularity"
            data = await fetch_api("/movies/public", params)
            if data:
                for item in data.get("data", []):
                    cats = item.get("categories", [])
                    if catalog_id == "hdghar-bollywood" and "Bollywood" not in cats:
                        continue
                    if catalog_id == "hdghar-hollywood" and "Hollywood" not in cats:
                        continue
                    if catalog_id == "hdghar-south" and "South Indian" not in cats:
                        continue
                    if catalog_id == "hdghar-punjabi" and "Punjabi" not in cats:
                        continue
                    if filter_cat != "all" and filter_cat.capitalize() not in cats:
                        continue
                    if filter_lang != "all":
                        spoken = []
                        for s in item.get("spokenLanguages", []):
                            if isinstance(s, dict):
                                spoken.append(s.get("name", "").lower())
                            elif isinstance(s, str):
                                spoken.append(s.lower())
                        if filter_lang.lower() not in spoken:
                            continue
                    metas.append(make_meta(item, "movie"))
        elif catalog_id == "hdghar-series":
            data = await fetch_api("/series/public", {"page": 1, "limit": 100})
            if data:
                for item in data.get("data", []):
                    metas.append(make_meta(item, "series"))
    except Exception as e:
        print(f"Catalog error: {e}")
    return {"metas": metas}

@app.get("/catalog/movie/{catalog_id}.json")
@app.get("/catalog/series/{catalog_id}.json")
async def catalog(catalog_id: str, request: Request):
    content_type = "movie" if "movie" in str(request.url.path) else "series"
    return await handle_catalog(catalog_id, content_type)

@app.get("/{config}/catalog/movie/{catalog_id}.json")
@app.get("/{config}/catalog/series/{catalog_id}.json")
async def catalog_configured(config: str, catalog_id: str, request: Request):
    content_type = "movie" if "movie" in str(request.url.path) else "series"
    return await handle_catalog(catalog_id, content_type, parse_config(config))

# ============================================================
# Search (both default and configured)
# ============================================================
async def handle_search(catalog_id: str, search: str, content_type: str, config: dict = None):
    filter_lang = config.get("language", "all") if config else "all"
    api_key = "movies" if content_type == "movie" else "series"
    metas = []
    try:
        data = await fetch_api("/search", {"q": search})
        if data:
            for item in data.get(api_key, []):
                if isinstance(item, dict):
                    if filter_lang != "all":
                        spoken = []
                        for s in item.get("spokenLanguages", []):
                            if isinstance(s, dict):
                                spoken.append(s.get("name", "").lower())
                            elif isinstance(s, str):
                                spoken.append(s.lower())
                        if filter_lang.lower() not in spoken:
                            continue
                    metas.append(make_meta(item, content_type))
    except Exception as e:
        print(f"Search error: {e}")
    return {"metas": metas}

@app.get("/catalog/movie/{catalog_id}/search={search}.json")
@app.get("/catalog/series/{catalog_id}/search={search}.json")
async def search(catalog_id: str, search: str, request: Request):
    content_type = "movie" if "/catalog/movie/" in str(request.url.path) else "series"
    return await handle_search(catalog_id, search, content_type)

@app.get("/{config}/catalog/movie/{catalog_id}/search={search}.json")
@app.get("/{config}/catalog/series/{catalog_id}/search={search}.json")
async def search_configured(config: str, catalog_id: str, search: str, request: Request):
    content_type = "movie" if "/catalog/movie/" in str(request.url.path) else "series"
    return await handle_search(catalog_id, search, content_type, parse_config(config))

# ============================================================
# Meta (both default and configured — THIS WAS THE BUG)
# ============================================================
async def handle_meta(content_type: str, id: str):
    if content_type == "movie":
        data = await fetch_movie(id)
    else:
        data = await fetch_series(id)
    if not data:
        raise HTTPException(404, "Not found")
    meta = make_meta(data, content_type)
    if content_type == "series":
        videos = []
        for season in data.get("seasons", []):
            season_num = season.get("seasonNumber", season.get("number", 1))
            for ep in season.get("episodes", []):
                ep_num = ep.get("episodeNumber", ep.get("number", 1))
                videos.append({
                    "id": f"{id}:{season_num}:{ep_num}",
                    "title": f"S{season_num}E{ep_num} - {ep.get('title', '')}",
                    "season": season_num,
                    "episode": ep_num,
                })
        meta["videos"] = videos
    return {"meta": meta}

@app.get("/meta/movie/{id}.json")
async def meta_movie(id: str):
    return await handle_meta("movie", id)

@app.get("/meta/series/{id}.json")
async def meta_series(id: str):
    return await handle_meta("series", id)

# THE FIX: Configured meta routes
@app.get("/{config}/meta/movie/{id}.json")
async def meta_movie_configured(config: str, id: str):
    return await handle_meta("movie", id)

@app.get("/{config}/meta/series/{id}.json")
async def meta_series_configured(config: str, id: str):
    return await handle_meta("series", id)

# ============================================================
# Stream (both default and configured — THIS WAS ALSO MISSING)
# ============================================================
async def handle_stream_movie(id: str):
    movie = await fetch_movie(id)
    if not movie:
        return {"streams": []}
    streams = []
    for link in movie.get("streamingLinks", []):
        if not link.get("isActive", True):
            continue
        url = link.get("url", "")
        if not url:
            continue
        streams.append({
            "name": "HDGharTV",
            "title": f"HDGharTV | {link.get('quality', '?')} | {movie.get('title', '')}",
            "url": url,
            "behaviorHints": {
                "notWebReady": True,
                "proxyHeaders": {"request": {"User-Agent": "Mozilla/5.0", "Referer": "https://hdghartv.cc/"}}
            }
        })
    return {"streams": streams}

async def handle_stream_series(id: str, season: str, episode: str):
    if not season or not episode:
        return {"streams": []}
    series = await fetch_series(id)
    if not series:
        return {"streams": []}
    s_num = int(season)
    e_num = int(episode)
    streams = []
    for s in series.get("seasons", []):
        if s.get("seasonNumber", s.get("number", 0)) != s_num:
            continue
        for ep in s.get("episodes", []):
            if ep.get("episodeNumber", ep.get("number", 0)) != e_num:
                continue
            for link in ep.get("streamingLinks", []):
                if not link.get("isActive", True):
                    continue
                url = link.get("url", "")
                if not url:
                    continue
                streams.append({
                    "name": "HDGharTV",
                    "title": f"HDGharTV | {link.get('quality', '?')} | S{s_num}E{e_num}",
                    "url": url,
                    "behaviorHints": {
                        "notWebReady": True,
                        "proxyHeaders": {"request": {"User-Agent": "Mozilla/5.0", "Referer": "https://hdghartv.cc/"}}
                    }
                })
    return {"streams": streams}

@app.get("/stream/movie/{id}.json")
async def stream_movie(id: str):
    return await handle_stream_movie(id)

@app.get("/stream/series/{id}.json")
@app.get("/stream/series/{id}:{season}.json")
@app.get("/stream/series/{id}:{season}:{episode}.json")
async def stream_series(id: str, season: Optional[str] = None, episode: Optional[str] = None):
    return await handle_stream_series(id, season, episode)

# THE FIX: Configured stream routes
@app.get("/{config}/stream/movie/{id}.json")
async def stream_movie_configured(config: str, id: str):
    return await handle_stream_movie(id)

@app.get("/{config}/stream/series/{id}.json")
@app.get("/{config}/stream/series/{id}:{season}.json")
@app.get("/{config}/stream/series/{id}:{season}:{episode}.json")
async def stream_series_configured(config: str, id: str, season: Optional[str] = None, episode: Optional[str] = None):
    return await handle_stream_series(id, season, episode)

# ============================================================
# Configure page — MovieBox style UI
# ============================================================
@app.get("/")
async def root():
    return RedirectResponse(url="/configure")

@app.get("/configure")
async def configure_page():
    return HTMLResponse(CONFIGURE_HTML)

@app.get("/health")
async def health():
    return {"status": "ok"}

CONFIGURE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HDGharTV — Stremio Addon</title>
<link rel="icon" type="image/png" href="https://hdghartv.cc/favicon.png">
<link rel="apple-touch-icon" href="https://hdghartv.cc/logo.png">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0a0c;--accent:#E50914;--accent2:#ff2a36;--text:#e5e5e5;--glass:rgba(229,9,20,0.15);--card:rgba(255,255,255,0.03)}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Outfit',sans-serif;background:var(--bg);background-image:radial-gradient(circle at 50% 20%,rgba(229,9,20,0.08) 0%,transparent 55%),radial-gradient(circle at 50% 85%,rgba(255,42,54,0.05) 0%,transparent 45%);color:var(--text);min-height:100vh;display:flex;align-items:center;justify-content:center;overflow-x:hidden}
.wrap{max-width:480px;width:100%;padding:3rem 2rem;text-align:center;display:flex;flex-direction:column;align-items:center}
/* Logo: black inside, red outside ring, glassmorphism */
.logo{width:110px;height:110px;margin-bottom:1.5rem;border-radius:28px;background:linear-gradient(135deg,var(--accent),var(--accent2));padding:3px;box-shadow:0 12px 40px rgba(229,9,20,0.25),0 0 0 1px rgba(255,255,255,0.05) inset;transform:rotate(-5deg);transition:transform 0.3s}
.logo:hover{transform:rotate(0) scale(1.05)}
.logo-inner{width:100%;height:100%;border-radius:25px;background:#0a0a0c;overflow:hidden;display:flex;align-items:center;justify-content:center;position:relative}
.logo-inner::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,0.1),transparent 50%);border-radius:25px;pointer-events:none}
.logo-inner img{width:70%;height:70%;object-fit:contain;filter:drop-shadow(0 2px 8px rgba(229,9,20,0.3))}
h1{font-size:3rem;font-weight:800;margin-bottom:.5rem;letter-spacing:-1px;background:linear-gradient(to right,#fff,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.sub{font-size:1.1rem;font-weight:300;margin-bottom:2.5rem;line-height:1.6}
/* Glass card */
.card{width:100%;background:var(--card);border:1px solid rgba(255,255,255,0.06);border-radius:20px;padding:2rem;backdrop-filter:blur(10px);box-shadow:0 8px 32px rgba(0,0,0,0.3),0 0 0 1px rgba(255,255,255,0.02) inset;margin-bottom:1.5rem}
.fg{margin-bottom:1.5rem;width:100%;text-align:left}
.fg label{display:block;font-size:.9rem;font-weight:600;margin-bottom:.5rem;color:rgba(255,255,255,0.6)}
.sw{position:relative;width:100%}
.sw select{width:100%;padding:1rem;border-radius:12px;border:1px solid var(--glass);background:rgba(255,255,255,0.05);color:#fff;font-size:1rem;font-family:'Outfit',sans-serif;outline:none;appearance:none;cursor:pointer;transition:all .3s}
.sw select:focus{border-color:var(--accent);background:rgba(229,9,20,0.05)}
.sw select option{background:#0a0a0c;color:#fff}
.sa{position:absolute;right:1rem;top:50%;transform:translateY(-50%);pointer-events:none;width:16px;height:16px;opacity:.5}
/* Install button above manifest box */
.ib{display:inline-block;width:100%;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;text-decoration:none;padding:1.1rem 2rem;font-size:1.15rem;font-weight:800;border-radius:50px;letter-spacing:1px;text-transform:uppercase;transition:all .3s;box-shadow:0 8px 25px rgba(229,9,20,0.25);margin-bottom:1rem}
.ib:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(229,9,20,0.35)}
/* Manifest box */
.mbox{width:100%;padding:.85rem 1.25rem;background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.08);border-radius:16px;font-family:monospace;font-size:.78rem;color:rgba(255,255,255,0.4);word-break:break-all;text-align:center;line-height:1.5;min-height:50px;display:flex;align-items:center;justify-content:center;margin-bottom:.85rem}
.cb{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;width:100%;background:transparent;color:var(--text);border:1px solid rgba(255,255,255,0.12);padding:.85rem 2rem;font-size:.95rem;font-weight:500;font-family:'Outfit',sans-serif;border-radius:50px;cursor:pointer;transition:all .3s}
.cb:hover{background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.25);color:#fff}
.cb svg{width:16px;height:16px;fill:currentColor;opacity:.7}
.note{margin-top:.5rem;font-size:.75rem;color:rgba(255,255,255,0.25);text-align:center}
@media(max-width:480px){.wrap{padding:2rem 1.25rem}h1{font-size:2.4rem}.card{padding:1.5rem}}
</style>
</head>
<body>
<div class="wrap">
<div class="logo"><div class="logo-inner"><img src="https://hdghartv.cc/logo.png" alt="HDGharTV"></div></div>
<h1>HDGharTV</h1>
<p class="sub">Movies & series with multi-audio support.<br>Select your preferences below.</p>
<div class="card">
<div class="fg"><label>Audio Language</label><div class="sw"><select id="language"><option value="all">All Languages</option><option value="hindi">Hindi</option><option value="english">English</option><option value="tamil">Tamil</option><option value="telugu">Telugu</option><option value="malayalam">Malayalam</option><option value="punjabi">Punjabi</option><option value="bengali">Bengali</option><option value="marathi">Marathi</option><option value="kannada">Kannada</option></select><svg class="sa" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div></div>
<div class="fg"><label>Category</label><div class="sw"><select id="category"><option value="all">All Categories</option><option value="bollywood">Bollywood</option><option value="hollywood">Hollywood</option><option value="south indian">South Indian</option><option value="punjabi">Punjabi</option></select><svg class="sa" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div></div>
</div>
<a href="#" id="ilink" class="ib">Install in Stremio</a>
<div class="mbox" id="murl">Loading...</div>
<button id="cbtn" class="cb"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg> Copy Manifest URL</button>
<div class="note">For Nuvio: copy URL &rarr; paste in addon settings.</div>
</div>
<script>
var ilink=document.getElementById("ilink"),cbtn=document.getElementById("cbtn"),ls=document.getElementById("language"),cs=document.getElementById("category"),mb=document.getElementById("murl");
function gp(){var l=ls.value,c=cs.value,o={language:l,category:c},e=btoa(JSON.stringify(o)).replace(/\+/g,"-").replace(/\//g,"_").replace(/=+$/,"");return e+"/"}
function bu(){return window.location.href.replace(/\/$/,"")}
function ul(){var p=gp(),r=window.location.href.replace("https://","").replace("http://","").replace(/\/$/,""),u=bu()+"/"+p+"manifest.json";mb.textContent=u;ilink.href="stremio://"+r+"/"+p+"manifest.json"}
cbtn.addEventListener("click",function(){var u=bu()+"/"+gp()+"manifest.json";navigator.clipboard.writeText(u);var h=cbtn.innerHTML;cbtn.innerHTML='<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg> Copied!';setTimeout(function(){cbtn.innerHTML=h},2000)});
ls.addEventListener("change",ul);cs.addEventListener("change",ul);ul();
</script>
</body></html>"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=False)

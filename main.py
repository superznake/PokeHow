from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()


@app.get("/minecraft/how", response_class=HTMLResponse)
async def root():
    html_path = Path("templates/index.html")
    html_content = html_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

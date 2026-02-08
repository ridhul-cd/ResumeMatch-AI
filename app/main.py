import os
from pathlib import Path
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Resume Match AI", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR / "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/test")
def test():
    return {"message": "Server is responding"}

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(router)
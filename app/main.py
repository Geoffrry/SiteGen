import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .generator import generate_website
import uuid

os.makedirs("static/generated-sites", exist_ok=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, business_name: str = Form(...), business_type: str = Form(...)):
    uid = str(uuid.uuid4())
    output_zip = f"static/generated-sites/{uid}.zip"
    generate_website(business_name, business_type, output_zip)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "zip_path": f"/{output_zip}"
    })

@app.get("/download/{file_name}")
def download(file_name: str):
    path = f"static/generated-sites/{file_name}"
    return FileResponse(path, media_type="application/zip", filename=file_name)

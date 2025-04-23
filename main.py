from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text_from_pdf
from email_generator import generate_email
import shutil
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request





# For future frontend use
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate_email/")
async def generate_email_route(
    resume: UploadFile,
    job_description: str = Form(...)
):
    with open(resume.filename, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    resume_text = extract_text_from_pdf(resume.filename)
    email_text = generate_email(resume_text, job_description)

    return {"email": email_text}

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    print("Rendering homepage...")
    return templates.TemplateResponse("index.html", {"request": request})

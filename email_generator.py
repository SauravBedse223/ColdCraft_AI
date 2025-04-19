import os
import google.generativeai as genai
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()
genai.configure(api_key="AIzaSyABKjLcBNCLlojiE9JfV3WBjj92Y7_ZfhE")

def generate_email(resume_text, job_description):
    prompt = f"""
You are an AI assistant that writes short, professional cold emails for job applications.

Given the resume and job description below, write a crisp email (5-7 lines max) for applying to the job.

--- RESUME ---
{resume_text}

--- JOB DESCRIPTION ---
{job_description}

--- EMAIL ---
"""

    model = genai.GenerativeModel("gemini-1.5-pro-002")
    response = model.generate_content(prompt)
    return response.text

import os
import google.generativeai as genai
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()
genai.configure(api_key="Your API KEY")

def generate_email(resume_text, job_description):
    prompt = f"""
    You are an AI email assistant specialized in generating professional and concise cold emails for job seekers.

Given a candidate's resume text and a job description, craft a short email (5–7 lines max) that:

- Clearly states the candidate’s intent to apply.
- Highlights 2–3 relevant strengths or experiences tailored to the job.
- You can make use of bullet points if needed
- Maintains a polite, professional tone.
- Ends with a call to action or expression of interest.

Avoid repeating resume content verbatim. Keep the language impactful but to the point. Use a simple subject line suitable for email.

Given the resume and job description below, write a crisp email (5-7 lines max) for applying to the job.
Also you can use bullets points if needed.


--- RESUME ---
{resume_text}

--- JOB DESCRIPTION ---
{job_description}

--- EMAIL ---
"""

    model = genai.GenerativeModel("gemini-1.5-pro-002")
    response = model.generate_content(prompt)
    return response.text

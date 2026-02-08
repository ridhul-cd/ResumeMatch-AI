from google import genai
from google.genai import types

from app.core.config import LLM_API_KEY,MODEL_NAME
from app.schemas.analyze import AnalyzeResponse

client = genai.Client(api_key=LLM_API_KEY)

def analyze_resume(resume_text: str, job_description: str) -> AnalyzeResponse:

    prompt = f"""
You are an AI assistant that compares a resume and a job description.

Return ONLY valid JSON in the following format:

{{
  "match_score": number between 0 and 100,
  "matched_skills": [string],
  "missing_skills": [string],
  "suggestions": [string]
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type = 'application/json',
            response_schema= AnalyzeResponse,
        )
    )
    return response.parsed
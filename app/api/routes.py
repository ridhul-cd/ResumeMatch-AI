from fastapi import APIRouter

from app.schemas.analyze import AnalyzeResponse,    AnalyzeRequest
from app.services.llm_service import analyze_resume

router = APIRouter()

@router.get("/health_check")
def health_check() -> dict:
    return {"status": "ok"}

@router.post('/resume_analyze',response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    return analyze_resume(
        request.resume_text,
        request.job_description
    )
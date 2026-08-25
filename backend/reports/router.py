import uuid
import datetime
from fastapi import APIRouter
from backend.reports.schemas import ReportRequest, ReportResponse

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/generate", response_model=ReportResponse)
async def generate_report(req: ReportRequest):
    rep_id = str(uuid.uuid4())
    return ReportResponse(
        report_id=rep_id,
        report_type=req.report_type,
        format=req.format,
        status="READY",
        download_url=f"/api/v1/reports/{rep_id}/download",
        generated_at=datetime.datetime.utcnow()
    )

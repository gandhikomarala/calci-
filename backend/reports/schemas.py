from typing import Optional, List, Dict, Any
import datetime
from pydantic import BaseModel

class ReportRequest(BaseModel):
    report_type: str  # CHURN_EXECUTIVE, MODEL_PERFORMANCE, DATA_QUALITY, DRIFT_ANALYSIS
    format: str = "PDF"
    filters: Optional[Dict[str, Any]] = None

class ReportResponse(BaseModel):
    report_id: str
    report_type: str
    format: str
    status: str = "READY"
    download_url: str
    generated_at: datetime.datetime

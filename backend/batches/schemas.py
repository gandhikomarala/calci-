from typing import Optional, List
import datetime
from pydantic import BaseModel

class BatchJobCreate(BaseModel):
    batch_name: str
    model_version_tag: str = "lightgbm-v1"
    input_file_path: str

class BatchJobResponse(BaseModel):
    id: str
    batch_name: str
    model_version_tag: str
    status: str
    total_records: int
    processed_records: int
    successful_records: int
    failed_records: int
    duration_seconds: Optional[float] = None
    created_at: datetime.datetime

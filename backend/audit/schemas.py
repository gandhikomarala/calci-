from typing import Optional, Dict, Any
import datetime
from pydantic import BaseModel

class AuditLogResponse(BaseModel):
    id: str
    actor: str
    action: str
    resource: str
    resource_id: Optional[str] = None
    ip_address: Optional[str] = None
    status: str
    created_at: datetime.datetime

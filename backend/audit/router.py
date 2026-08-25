from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from packages.database.session import get_db_session
from packages.database.models.audit import AuditLog
from backend.audit.schemas import AuditLogResponse

router = APIRouter(prefix="/audit", tags=["Audit Trail"])

@router.get("", response_model=List[AuditLogResponse])
async def list_audit_logs(session: AsyncSession = Depends(get_db_session)):
    stmt = select(AuditLog).order_by(desc(AuditLog.created_at)).limit(100)
    res = await session.execute(stmt)
    return list(res.scalars().all())

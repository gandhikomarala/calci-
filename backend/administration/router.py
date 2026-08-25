from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from packages.database.session import get_db_session
from packages.database.models.settings import SystemSetting

router = APIRouter(prefix="/administration", tags=["Administration"])

@router.get("/settings")
async def get_settings(session: AsyncSession = Depends(get_db_session)):
    stmt = select(SystemSetting)
    res = await session.execute(stmt)
    return list(res.scalars().all())

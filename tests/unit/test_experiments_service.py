"""Unit test for Experiment Domain Service."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from backend.experiments.service import ExperimentService
from backend.experiments.schemas import ExperimentCreate, ExperimentFilterParams
from backend.core.exceptions import NotFoundError

@pytest.mark.asyncio
async def test_experiments_list_items():
    mock_session = AsyncMock()
    service = ExperimentService(mock_session)
    service.repo.list_filtered = AsyncMock(return_value=([], 0))

    params = ExperimentFilterParams(page=1, page_size=20)
    items, total = await service.list_items(params)
    assert items == []
    assert total == 0

@pytest.mark.asyncio
async def test_experiments_get_by_id():
    mock_session = AsyncMock()
    service = ExperimentService(mock_session)
    mock_entity = MagicMock(id="entity-uuid-123")
    service.repo.get_by_id = AsyncMock(return_value=mock_entity)

    entity = await service.get_by_id("entity-uuid-123")
    assert entity.id == "entity-uuid-123"

@pytest.mark.asyncio
async def test_experiments_get_by_id_not_found():
    mock_session = AsyncMock()
    service = ExperimentService(mock_session)
    service.repo.get_by_id = AsyncMock(return_value=None)

    with pytest.raises(NotFoundError):
        await service.get_by_id("non-existent-uuid")

@pytest.mark.asyncio
async def test_experiments_create_item():
    mock_session = AsyncMock()
    service = ExperimentService(mock_session)
    service.repo.create = AsyncMock()

    req = ExperimentCreate(name="Enterprise Test", description="Automated Test Entity")
    res = await service.create(req)
    assert res is not None

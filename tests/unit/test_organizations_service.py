"""Unit test for Organization Domain Service."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from backend.organizations.service import OrganizationService
from backend.organizations.schemas import OrganizationCreate, OrganizationFilterParams
from backend.core.exceptions import NotFoundError

@pytest.mark.asyncio
async def test_organizations_list_items():
    mock_session = AsyncMock()
    service = OrganizationService(mock_session)
    service.repo.list_filtered = AsyncMock(return_value=([], 0))

    params = OrganizationFilterParams(page=1, page_size=20)
    items, total = await service.list_items(params)
    assert items == []
    assert total == 0

@pytest.mark.asyncio
async def test_organizations_get_by_id():
    mock_session = AsyncMock()
    service = OrganizationService(mock_session)
    mock_entity = MagicMock(id="entity-uuid-123")
    service.repo.get_by_id = AsyncMock(return_value=mock_entity)

    entity = await service.get_by_id("entity-uuid-123")
    assert entity.id == "entity-uuid-123"

@pytest.mark.asyncio
async def test_organizations_get_by_id_not_found():
    mock_session = AsyncMock()
    service = OrganizationService(mock_session)
    service.repo.get_by_id = AsyncMock(return_value=None)

    with pytest.raises(NotFoundError):
        await service.get_by_id("non-existent-uuid")

@pytest.mark.asyncio
async def test_organizations_create_item():
    mock_session = AsyncMock()
    service = OrganizationService(mock_session)
    service.repo.create = AsyncMock()

    req = OrganizationCreate(name="Enterprise Test", description="Automated Test Entity")
    res = await service.create(req)
    assert res is not None

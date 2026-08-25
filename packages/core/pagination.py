"""Pagination utilities."""

import math
from typing import List, TypeVar, Sequence
from packages.core.types import PaginatedResponse

T = TypeVar("T")

def paginate_sequence(items: Sequence[T], total: int, page: int, page_size: int) -> PaginatedResponse[T]:
    total_pages = max(math.ceil(total / page_size), 1) if page_size > 0 else 1
    return PaginatedResponse(
        items=list(items),
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        has_next=page < total_pages,
        has_prev=page > 1,
    )

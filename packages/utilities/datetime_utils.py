"""Datetime formatting and conversion helpers."""

import datetime
from typing import Optional

def now_utc() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)

def format_iso(dt: Optional[datetime.datetime]) -> Optional[str]:
    if dt is None:
        return None
    return dt.isoformat()

def parse_iso(iso_str: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(iso_str)

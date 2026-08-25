"""TransactionSimulator: Real-time transaction generator and live streaming emitter."""

import httpx
from typing import Dict, Any, List, Optional

class TransactionSimulator:
    def __init__(self, base_url: str = "http://localhost:8000/api/v1", api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "User-Agent": "FinGuard-Python-SDK/1.0.0",
            "Content-Type": "application/json",
        }
        if api_key:
            self.headers["X-API-Key"] = api_key

    async def get_status(self) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{self.base_url}/health", headers=self.headers)
            return resp.json()

"""Device Fingerprints, Emulator Signatures, and IP Clusters Fixture Generator."""

import random
import uuid
import datetime
from typing import List, Dict, Any

def generate_devices_fixtures(count: int = 500) -> List[Dict[str, Any]]:
    items = []
    base_time = datetime.datetime.utcnow() - datetime.timedelta(days=60)
    for i in range(count):
        items.append({
            "id": str(uuid.uuid4()),
            "code": f"FIX-{i:06d}",
            "name": f"Enterprise Generated {i}",
            "is_active": True,
            "created_at": (base_time + datetime.timedelta(minutes=i * 15)).isoformat() + "Z",
            "updated_at": (base_time + datetime.timedelta(minutes=i * 15)).isoformat() + "Z",
            "metadata": {"seed_index": i, "environment": "fixture"}
        })
    return items

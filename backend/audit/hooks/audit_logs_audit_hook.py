"""Audit Trail State Diff Interceptor for AuditLog."""

import datetime
from typing import Dict, Any, Optional
from backend.core.logging import get_logger

logger = get_logger("audit_logs_audit_hook")

class AuditLogAuditHook:
    @staticmethod
    def record_diff(before: Optional[Dict[str, Any]], after: Optional[Dict[str, Any]], actor_id: Optional[str] = None) -> Dict[str, Any]:
        diff = {}
        if before and after:
            for k in set(before.keys()).union(after.keys()):
                if before.get(k) != after.get(k):
                    diff[k] = {"old": before.get(k), "new": after.get(k)}
        
        audit_record = {
            "entity": "AuditLog",
            "actor_id": actor_id,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "diff": diff,
            "action": "UPDATE" if before and after else ("CREATE" if after else "DELETE")
        }
        logger.info("Recorded AuditLog audit trail record", action=audit_record["action"])
        return audit_record

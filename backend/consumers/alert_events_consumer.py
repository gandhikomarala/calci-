"""Asynchronous Event Consumer & Webhook Notifier for AlertEvent."""

from typing import Dict, Any, Optional
from backend.core.logging import get_logger

logger = get_logger("alert_events_consumer")

class AlertEventConsumer:
    @staticmethod
    async def process_event(event_type: str, payload: Dict[str, Any]) -> bool:
        logger.info("Processing AlertEvent domain event", event_type=event_type, payload=payload)
        if event_type.endswith(".created"):
            return await AlertEventConsumer._handle_created(payload)
        elif event_type.endswith(".updated"):
            return await AlertEventConsumer._handle_updated(payload)
        return True

    @staticmethod
    async def _handle_created(payload: Dict[str, Any]) -> bool:
        logger.info("AlertEvent entity creation event processed successfully")
        return True

    @staticmethod
    async def _handle_updated(payload: Dict[str, Any]) -> bool:
        logger.info("AlertEvent entity update event processed successfully")
        return True

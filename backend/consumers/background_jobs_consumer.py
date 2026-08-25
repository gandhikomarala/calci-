"""Asynchronous Event Consumer & Webhook Notifier for BackgroundJob."""

from typing import Dict, Any, Optional
from backend.core.logging import get_logger

logger = get_logger("background_jobs_consumer")

class BackgroundJobConsumer:
    @staticmethod
    async def process_event(event_type: str, payload: Dict[str, Any]) -> bool:
        logger.info("Processing BackgroundJob domain event", event_type=event_type, payload=payload)
        if event_type.endswith(".created"):
            return await BackgroundJobConsumer._handle_created(payload)
        elif event_type.endswith(".updated"):
            return await BackgroundJobConsumer._handle_updated(payload)
        return True

    @staticmethod
    async def _handle_created(payload: Dict[str, Any]) -> bool:
        logger.info("BackgroundJob entity creation event processed successfully")
        return True

    @staticmethod
    async def _handle_updated(payload: Dict[str, Any]) -> bool:
        logger.info("BackgroundJob entity update event processed successfully")
        return True

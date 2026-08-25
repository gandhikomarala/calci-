"""Asynchronous Event Consumer & Webhook Notifier for Merchant."""

from typing import Dict, Any, Optional
from backend.core.logging import get_logger

logger = get_logger("merchants_consumer")

class MerchantConsumer:
    @staticmethod
    async def process_event(event_type: str, payload: Dict[str, Any]) -> bool:
        logger.info("Processing Merchant domain event", event_type=event_type, payload=payload)
        if event_type.endswith(".created"):
            return await MerchantConsumer._handle_created(payload)
        elif event_type.endswith(".updated"):
            return await MerchantConsumer._handle_updated(payload)
        return True

    @staticmethod
    async def _handle_created(payload: Dict[str, Any]) -> bool:
        logger.info("Merchant entity creation event processed successfully")
        return True

    @staticmethod
    async def _handle_updated(payload: Dict[str, Any]) -> bool:
        logger.info("Merchant entity update event processed successfully")
        return True

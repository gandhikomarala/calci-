"""Notification Domain Package for FinGuard AI (In-app and outgoing alert notifications for users)."""

from backend.notifications.router import router as notifications_router
from backend.notifications.service import NotificationService
from backend.notifications.repository import NotificationRepository
from backend.notifications.schemas import NotificationResponse, NotificationCreate, NotificationUpdate, NotificationFilterParams

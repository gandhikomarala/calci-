"""NotificationTemplate Domain Package for FinGuard AI (Configurable alert notification message templates)."""

from backend.notification_templates.router import router as notification_templates_router
from backend.notification_templates.service import NotificationTemplateService
from backend.notification_templates.repository import NotificationTemplateRepository
from backend.notification_templates.schemas import NotificationTemplateResponse, NotificationTemplateCreate, NotificationTemplateUpdate, NotificationTemplateFilterParams

"""CustomerLocation Domain Package for FinGuard AI (Customer primary and historical residential/work locations)."""

from backend.customer_locations.router import router as customer_locations_router
from backend.customer_locations.service import CustomerLocationService
from backend.customer_locations.repository import CustomerLocationRepository
from backend.customer_locations.schemas import CustomerLocationResponse, CustomerLocationCreate, CustomerLocationUpdate, CustomerLocationFilterParams

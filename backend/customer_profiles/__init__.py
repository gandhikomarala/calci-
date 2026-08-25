"""CustomerProfile Domain Package for FinGuard AI (360 behavioral profiles, baseline spending, home regions, primary devices)."""

from backend.customer_profiles.router import router as customer_profiles_router
from backend.customer_profiles.service import CustomerProfileService
from backend.customer_profiles.repository import CustomerProfileRepository
from backend.customer_profiles.schemas import CustomerProfileResponse, CustomerProfileCreate, CustomerProfileUpdate, CustomerProfileFilterParams

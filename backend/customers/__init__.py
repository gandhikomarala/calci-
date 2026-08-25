"""Customer Domain Package for FinGuard AI (Banking customer entities, KYC status, and risk categorizations)."""

from backend.customers.router import router as customers_router
from backend.customers.service import CustomerService
from backend.customers.repository import CustomerRepository
from backend.customers.schemas import CustomerResponse, CustomerCreate, CustomerUpdate, CustomerFilterParams

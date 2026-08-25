"""InvestigationAssignment Domain Package for FinGuard AI (Analyst case assignments, workload distribution, and SLAs)."""

from backend.investigation_assignments.router import router as investigation_assignments_router
from backend.investigation_assignments.service import InvestigationAssignmentService
from backend.investigation_assignments.repository import InvestigationAssignmentRepository
from backend.investigation_assignments.schemas import InvestigationAssignmentResponse, InvestigationAssignmentCreate, InvestigationAssignmentUpdate, InvestigationAssignmentFilterParams

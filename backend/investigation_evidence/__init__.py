"""InvestigationEvidence Domain Package for FinGuard AI (Evidence items (transaction screenshots, IP logs, device traces))."""

from backend.investigation_evidence.router import router as investigation_evidence_router
from backend.investigation_evidence.service import InvestigationEvidenceService
from backend.investigation_evidence.repository import InvestigationEvidenceRepository
from backend.investigation_evidence.schemas import InvestigationEvidenceResponse, InvestigationEvidenceCreate, InvestigationEvidenceUpdate, InvestigationEvidenceFilterParams

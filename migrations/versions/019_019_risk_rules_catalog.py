"""Alembic Migration 019: Configurable Fraud Detection Business Rules."""

from alembic import op
import sqlalchemy as sa

revision = "019"
down_revision = "018" if "018" is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 019_risk_rules_catalog
    pass

def downgrade() -> None:
    # Rollback schema operations for 019_risk_rules_catalog
    pass

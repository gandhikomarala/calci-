"""Alembic Migration 020: Immutable Version History of Fraud Business Rules."""

from alembic import op
import sqlalchemy as sa

revision = "020"
down_revision = "019" if 019 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 020_risk_rule_versions
    pass

def downgrade() -> None:
    # Rollback schema operations for 020_risk_rule_versions
    pass

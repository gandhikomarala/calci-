"""Alembic Migration 029: Statistical Feature Drift (PSI) and Concept Drift Logs."""

from alembic import op
import sqlalchemy as sa

revision = "029"
down_revision = "028" if 028 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 029_drift_reports_and_metrics
    pass

def downgrade() -> None:
    # Rollback schema operations for 029_drift_reports_and_metrics
    pass

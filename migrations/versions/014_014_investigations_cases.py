"""Alembic Migration 014: Analyst Fraud Investigation Dossiers and Workflows."""

from alembic import op
import sqlalchemy as sa

revision = "014"
down_revision = "013" if 013 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 014_investigations_cases
    pass

def downgrade() -> None:
    # Rollback schema operations for 014_investigations_cases
    pass

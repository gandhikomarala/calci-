"""Alembic Migration 003: Customers, 360 Financial Profiles, and Risk Tiers."""

from alembic import op
import sqlalchemy as sa

revision = "003"
down_revision = "002" if 002 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 003_customers_and_profiles
    pass

def downgrade() -> None:
    # Rollback schema operations for 003_customers_and_profiles
    pass

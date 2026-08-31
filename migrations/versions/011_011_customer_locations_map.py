"""Alembic Migration 011: Customer Historical and Home Residential Locations."""

from alembic import op
import sqlalchemy as sa

revision = "011"
down_revision = "010" if 010 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 011_customer_locations_map
    pass

def downgrade() -> None:
    # Rollback schema operations for 011_customer_locations_map
    pass

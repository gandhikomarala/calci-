"""Alembic Migration 007: Merchants, Category Codes (MCCs), and Risk Ratings."""

from alembic import op
import sqlalchemy as sa

revision = "007"
down_revision = "006" if "006" is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 007_merchants_and_categories
    pass

def downgrade() -> None:
    # Rollback schema operations for 007_merchants_and_categories
    pass

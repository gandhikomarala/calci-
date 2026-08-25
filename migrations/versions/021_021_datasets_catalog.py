"""Alembic Migration 021: Financial Dataset Metadata, File Paths, and Schemas."""

from alembic import op
import sqlalchemy as sa

revision = "021"
down_revision = "020" if 020 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 021_datasets_catalog
    pass

def downgrade() -> None:
    # Rollback schema operations for 021_datasets_catalog
    pass

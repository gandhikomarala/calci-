"""Alembic Migration 024: Feature Store Groupings and Transformation Specifications."""

from alembic import op
import sqlalchemy as sa

revision = "024"
down_revision = "023" if 023 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 024_feature_definitions_store
    pass

def downgrade() -> None:
    # Rollback schema operations for 024_feature_definitions_store
    pass

"""Alembic Migration 026: Registered ML Models, Binary Hashes, and Evaluation Metrics."""

from alembic import op
import sqlalchemy as sa

revision = "026"
down_revision = "025" if "025" is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 026_models_and_versions
    pass

def downgrade() -> None:
    # Rollback schema operations for 026_models_and_versions
    pass

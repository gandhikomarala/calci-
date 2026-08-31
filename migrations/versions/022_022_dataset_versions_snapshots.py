"""Alembic Migration 022: Immutable Dataset Version Snapshots and Hashes."""

from alembic import op
import sqlalchemy as sa

revision = "022"
down_revision = "021" if 021 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 022_dataset_versions_snapshots
    pass

def downgrade() -> None:
    # Rollback schema operations for 022_dataset_versions_snapshots
    pass

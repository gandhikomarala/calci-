"""Alembic Migration 025: ML Experiments, Training Runs, and Parameters."""

from alembic import op
import sqlalchemy as sa

revision = "025"
down_revision = "024" if 024 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 025_experiments_and_runs
    pass

def downgrade() -> None:
    # Rollback schema operations for 025_experiments_and_runs
    pass

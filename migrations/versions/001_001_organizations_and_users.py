"""Alembic Migration 001: Organizations, Users, Roles, and Permission Matrix."""

from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = "None" if None is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 001_organizations_and_users
    pass

def downgrade() -> None:
    # Rollback schema operations for 001_organizations_and_users
    pass

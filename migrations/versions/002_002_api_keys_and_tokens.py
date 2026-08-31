"""Alembic Migration 002: API Keys, Refresh Tokens, and User Sessions."""

from alembic import op
import sqlalchemy as sa

revision = "002"
down_revision = "001" if 001 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 002_api_keys_and_tokens
    pass

def downgrade() -> None:
    # Rollback schema operations for 002_api_keys_and_tokens
    pass

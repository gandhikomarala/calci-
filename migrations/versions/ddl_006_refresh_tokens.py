"""Alembic Migration: Explicit DDL Definition for refresh_tokens."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_006_refresh_tokens"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE refresh_tokens (id UUID PRIMARY KEY, user_id UUID REFERENCES users(id), token_hash VARCHAR(255) NOT NULL, is_revoked BOOLEAN DEFAULT FALSE, expires_at TIMESTAMPTZ NOT NULL, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_refresh_tokens_created_at ON refresh_tokens (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS refresh_tokens CASCADE;")

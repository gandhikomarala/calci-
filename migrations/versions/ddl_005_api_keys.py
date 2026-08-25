"""Alembic Migration: Explicit DDL Definition for api_keys."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_005_api_keys"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE api_keys (id UUID PRIMARY KEY, user_id UUID REFERENCES users(id), key_hash VARCHAR(255) NOT NULL, name VARCHAR(100), expires_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_api_keys_created_at ON api_keys (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS api_keys CASCADE;")

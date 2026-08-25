"""Alembic Migration: Explicit DDL Definition for sessions."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_007_sessions"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE user_sessions (id UUID PRIMARY KEY, user_id UUID REFERENCES users(id), ip_address VARCHAR(45), user_agent TEXT, last_activity TIMESTAMPTZ NOT NULL, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_sessions_created_at ON sessions (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS sessions CASCADE;")

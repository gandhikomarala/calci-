"""Alembic Migration: Explicit DDL Definition for audit_logs."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_030_audit_logs"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE audit_logs (id UUID PRIMARY KEY, actor_id UUID, action VARCHAR(100) NOT NULL, resource VARCHAR(100) NOT NULL, payload JSONB, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_audit_logs_created_at ON audit_logs (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS audit_logs CASCADE;")

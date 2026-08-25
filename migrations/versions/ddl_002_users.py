"""Alembic Migration: Explicit DDL Definition for users."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_002_users"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE users (id UUID PRIMARY KEY, organization_id UUID REFERENCES organizations(id), email VARCHAR(255) UNIQUE NOT NULL, password_hash VARCHAR(255) NOT NULL, role VARCHAR(50) NOT NULL, is_active BOOLEAN DEFAULT TRUE, created_at TIMESTAMPTZ NOT NULL, updated_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_users_created_at ON users (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS users CASCADE;")

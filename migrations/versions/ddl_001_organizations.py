"""Alembic Migration: Explicit DDL Definition for organizations."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_001_organizations"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE organizations (id UUID PRIMARY KEY, name VARCHAR(255) NOT NULL, tier VARCHAR(50) NOT NULL, is_active BOOLEAN DEFAULT TRUE, created_at TIMESTAMPTZ NOT NULL, updated_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_organizations_created_at ON organizations (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS organizations CASCADE;")

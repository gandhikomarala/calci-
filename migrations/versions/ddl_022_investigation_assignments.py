"""Alembic Migration: Explicit DDL Definition for investigation_assignments."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_022_investigation_assignments"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE investigation_assignments (id UUID PRIMARY KEY, investigation_id UUID REFERENCES investigations(id), analyst_id UUID REFERENCES users(id), assigned_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_investigation_assignments_created_at ON investigation_assignments (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS investigation_assignments CASCADE;")

"""Alembic Migration: Explicit DDL Definition for investigation_evidence."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_023_investigation_evidence"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE investigation_evidence (id UUID PRIMARY KEY, investigation_id UUID REFERENCES investigations(id), evidence_type VARCHAR(50), file_uri TEXT, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_investigation_evidence_created_at ON investigation_evidence (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS investigation_evidence CASCADE;")

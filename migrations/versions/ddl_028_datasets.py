"""Alembic Migration: Explicit DDL Definition for datasets."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_028_datasets"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE datasets (id UUID PRIMARY KEY, name VARCHAR(255) NOT NULL, storage_path TEXT NOT NULL, row_count BIGINT, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_datasets_created_at ON datasets (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS datasets CASCADE;")

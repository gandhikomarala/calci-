"""Alembic Migration: Explicit DDL Definition for investigation_comments."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_024_investigation_comments"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE investigation_comments (id UUID PRIMARY KEY, investigation_id UUID REFERENCES investigations(id), author_id UUID REFERENCES users(id), content TEXT NOT NULL, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_investigation_comments_created_at ON investigation_comments (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS investigation_comments CASCADE;")

"""Alembic Migration: Explicit DDL Definition for model_versions."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_029_model_versions"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE model_versions (id UUID PRIMARY KEY, model_name VARCHAR(100) NOT NULL, version_tag VARCHAR(50) NOT NULL, stage VARCHAR(50) NOT NULL, artifact_uri TEXT, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_model_versions_created_at ON model_versions (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS model_versions CASCADE;")

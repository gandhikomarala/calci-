"""Alembic Migration: Explicit DDL Definition for risk_scores."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_025_risk_scores"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE risk_scores (id UUID PRIMARY KEY, transaction_id UUID REFERENCES transactions(id), probability NUMERIC(6,4), score INTEGER, decision VARCHAR(50), created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_risk_scores_created_at ON risk_scores (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS risk_scores CASCADE;")

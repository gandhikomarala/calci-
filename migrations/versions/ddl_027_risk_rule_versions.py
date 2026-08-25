"""Alembic Migration: Explicit DDL Definition for risk_rule_versions."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_027_risk_rule_versions"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE risk_rule_versions (id UUID PRIMARY KEY, rule_id UUID REFERENCES risk_rules(id), version_num INTEGER NOT NULL, schema JSONB, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_risk_rule_versions_created_at ON risk_rule_versions (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS risk_rule_versions CASCADE;")

"""Alembic Migration: Explicit DDL Definition for risk_rules."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_026_risk_rules"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE risk_rules (id UUID PRIMARY KEY, rule_code VARCHAR(100) UNIQUE NOT NULL, condition_expression TEXT NOT NULL, weight NUMERIC(4,2), is_active BOOLEAN DEFAULT TRUE);
    CREATE INDEX IF NOT EXISTS ix_risk_rules_created_at ON risk_rules (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS risk_rules CASCADE;")

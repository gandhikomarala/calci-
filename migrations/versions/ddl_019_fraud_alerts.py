"""Alembic Migration: Explicit DDL Definition for fraud_alerts."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_019_fraud_alerts"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE fraud_alerts (id UUID PRIMARY KEY, transaction_id UUID REFERENCES transactions(id), risk_score INTEGER NOT NULL, severity VARCHAR(50) NOT NULL, status VARCHAR(50) NOT NULL, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_fraud_alerts_created_at ON fraud_alerts (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS fraud_alerts CASCADE;")

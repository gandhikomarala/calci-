"""Alembic Migration: Explicit DDL Definition for investigations."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_021_investigations"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE investigations (id UUID PRIMARY KEY, alert_id UUID REFERENCES fraud_alerts(id), analyst_id UUID REFERENCES users(id), status VARCHAR(50) NOT NULL, decision VARCHAR(50), created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_investigations_created_at ON investigations (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS investigations CASCADE;")

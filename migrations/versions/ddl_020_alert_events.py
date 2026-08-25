"""Alembic Migration: Explicit DDL Definition for alert_events."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_020_alert_events"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE alert_events (id UUID PRIMARY KEY, alert_id UUID REFERENCES fraud_alerts(id), action VARCHAR(50) NOT NULL, actor_id UUID, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_alert_events_created_at ON alert_events (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS alert_events CASCADE;")

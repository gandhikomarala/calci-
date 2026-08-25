"""Alembic Migration: Explicit DDL Definition for transaction_events."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_012_transaction_events"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE transaction_events (id UUID PRIMARY KEY, transaction_id UUID REFERENCES transactions(id), event_type VARCHAR(50) NOT NULL, payload JSONB, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_transaction_events_created_at ON transaction_events (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS transaction_events CASCADE;")

"""Alembic Migration: Explicit DDL Definition for customer_devices."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_016_customer_devices"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE customer_devices (id UUID PRIMARY KEY, customer_id UUID REFERENCES customers(id), device_id UUID REFERENCES devices(id), is_trusted BOOLEAN DEFAULT TRUE, last_seen TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_customer_devices_created_at ON customer_devices (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS customer_devices CASCADE;")

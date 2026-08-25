"""Alembic Migration: Explicit DDL Definition for devices."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_015_devices"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE devices (id UUID PRIMARY KEY, device_fingerprint VARCHAR(255) UNIQUE NOT NULL, device_type VARCHAR(50), is_emulator BOOLEAN DEFAULT FALSE, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_devices_created_at ON devices (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS devices CASCADE;")

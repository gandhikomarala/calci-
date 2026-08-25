"""Alembic Migration: Explicit DDL Definition for locations."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_017_locations"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE locations (id UUID PRIMARY KEY, region_code VARCHAR(50) NOT NULL, latitude NUMERIC(9,6), longitude NUMERIC(9,6), country_iso VARCHAR(10), created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_locations_created_at ON locations (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS locations CASCADE;")

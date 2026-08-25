"""Alembic Migration: Explicit DDL Definition for customer_locations."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_018_customer_locations"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE customer_locations (id UUID PRIMARY KEY, customer_id UUID REFERENCES customers(id), location_id UUID REFERENCES locations(id), is_primary BOOLEAN DEFAULT TRUE);
    CREATE INDEX IF NOT EXISTS ix_customer_locations_created_at ON customer_locations (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS customer_locations CASCADE;")

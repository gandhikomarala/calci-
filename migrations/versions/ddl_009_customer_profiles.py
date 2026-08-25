"""Alembic Migration: Explicit DDL Definition for customer_profiles."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_009_customer_profiles"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE customer_profiles (id UUID PRIMARY KEY, customer_id UUID REFERENCES customers(id), avg_amount NUMERIC(12,2), home_region VARCHAR(50), primary_device VARCHAR(50), created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_customer_profiles_created_at ON customer_profiles (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS customer_profiles CASCADE;")

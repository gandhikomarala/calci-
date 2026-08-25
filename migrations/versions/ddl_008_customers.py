"""Alembic Migration: Explicit DDL Definition for customers."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_008_customers"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE customers (id UUID PRIMARY KEY, customer_code VARCHAR(50) UNIQUE NOT NULL, kyc_status VARCHAR(50) NOT NULL, risk_rating VARCHAR(50) NOT NULL, created_at TIMESTAMPTZ NOT NULL, updated_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_customers_created_at ON customers (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS customers CASCADE;")

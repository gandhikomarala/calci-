"""Alembic Migration: Explicit DDL Definition for accounts."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_010_accounts"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE accounts (id UUID PRIMARY KEY, customer_id UUID REFERENCES customers(id), account_number VARCHAR(50) UNIQUE NOT NULL, balance NUMERIC(14,2) DEFAULT 0.00, currency VARCHAR(10) NOT NULL, status VARCHAR(50) NOT NULL, created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_accounts_created_at ON accounts (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS accounts CASCADE;")

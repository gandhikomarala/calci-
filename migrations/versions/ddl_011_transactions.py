"""Alembic Migration: Explicit DDL Definition for transactions."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_011_transactions"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE transactions (id UUID PRIMARY KEY, transaction_code VARCHAR(50) UNIQUE NOT NULL, account_id UUID REFERENCES accounts(id), amount NUMERIC(12,2) NOT NULL, currency VARCHAR(10) NOT NULL, channel VARCHAR(50), payment_method VARCHAR(50), timestamp TIMESTAMPTZ NOT NULL, is_fraud INTEGER DEFAULT 0);
    CREATE INDEX IF NOT EXISTS ix_transactions_created_at ON transactions (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS transactions CASCADE;")

"""Alembic Migration: Explicit DDL Definition for merchants."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_013_merchants"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE merchants (id UUID PRIMARY KEY, merchant_code VARCHAR(50) UNIQUE NOT NULL, name VARCHAR(255) NOT NULL, mcc_category VARCHAR(100), risk_level VARCHAR(50), created_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_merchants_created_at ON merchants (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS merchants CASCADE;")

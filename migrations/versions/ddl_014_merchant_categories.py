"""Alembic Migration: Explicit DDL Definition for merchant_categories."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_014_merchant_categories"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE merchant_categories (id UUID PRIMARY KEY, mcc_code VARCHAR(20) UNIQUE NOT NULL, name VARCHAR(100), is_high_risk BOOLEAN DEFAULT FALSE);
    CREATE INDEX IF NOT EXISTS ix_merchant_categories_created_at ON merchant_categories (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS merchant_categories CASCADE;")

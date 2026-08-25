"""Alembic Migration: Explicit DDL Definition for permissions."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_004_permissions"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE permissions (id UUID PRIMARY KEY, permission_code VARCHAR(100) UNIQUE NOT NULL, description TEXT, module VARCHAR(50) NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_permissions_created_at ON permissions (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS permissions CASCADE;")

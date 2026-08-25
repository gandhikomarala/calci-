"""Alembic Migration: Explicit DDL Definition for user_roles."""

from alembic import op
import sqlalchemy as sa

revision = "ddl_003_user_roles"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE user_roles (id UUID PRIMARY KEY, user_id UUID REFERENCES users(id), role_code VARCHAR(50) NOT NULL, granted_at TIMESTAMPTZ NOT NULL);
    CREATE INDEX IF NOT EXISTS ix_user_roles_created_at ON user_roles (created_at);
    """)

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS user_roles CASCADE;")

"""Alembic Migration 004: Banking Accounts, Currency Balances, and Limits."""

from alembic import op
import sqlalchemy as sa

revision = "004"
down_revision = "003" if 003 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 004_accounts_and_balances
    pass

def downgrade() -> None:
    # Rollback schema operations for 004_accounts_and_balances
    pass

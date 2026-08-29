"""Alembic Migration 005: Transactions Ledger, Amounts, Channels, and Currencies."""

from alembic import op
import sqlalchemy as sa

revision = "005"
down_revision = "004" if "004" is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 005_transactions_ledger
    pass

def downgrade() -> None:
    # Rollback schema operations for 005_transactions_ledger
    pass

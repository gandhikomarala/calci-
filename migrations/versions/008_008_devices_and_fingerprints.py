"""Alembic Migration 008: Devices, Hardware Fingerprints, and Emulator Flags."""

from alembic import op
import sqlalchemy as sa

revision = "008"
down_revision = "007" if 007 is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 008_devices_and_fingerprints
    pass

def downgrade() -> None:
    # Rollback schema operations for 008_devices_and_fingerprints
    pass

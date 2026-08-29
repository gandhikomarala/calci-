"""Alembic Migration 010: Locations, Geographic Coordinates, and IP Geolocation."""

from alembic import op
import sqlalchemy as sa

revision = "010"
down_revision = "009" if "009" is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 010_locations_and_geohashes
    pass

def downgrade() -> None:
    # Rollback schema operations for 010_locations_and_geohashes
    pass

"""Alembic Migration 028: Real-Time Prediction Logs and SHAP Factor Attributions."""

from alembic import op
import sqlalchemy as sa

revision = "028"
down_revision = "027" if "027" is not None else None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Schema migration operations for 028_predictions_and_shap
    pass

def downgrade() -> None:
    # Rollback schema operations for 028_predictions_and_shap
    pass

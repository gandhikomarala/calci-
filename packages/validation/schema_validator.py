"""Schema assertion and data type validation."""

from typing import Dict, Any, List, Tuple
import pandas as pd

REQUIRED_COLUMNS = {
    "customer_id": "string",
    "signup_date": "datetime",
    "subscription_type": "string",
    "contract_type": "string",
    "monthly_charge": "numeric",
    "total_spend": "numeric",
    "tenure_months": "numeric",
}

class SchemaValidator:
    @staticmethod
    def validate_schema(df: pd.DataFrame) -> Tuple[bool, List[str]]:
        errors: List[str] = []
        for col, expected_type in REQUIRED_COLUMNS.items():
            if col not in df.columns:
                errors.append(f"Missing mandatory column '{col}'")
                continue
            
            if expected_type == "numeric" and not pd.api.types.is_numeric_dtype(df[col]):
                errors.append(f"Column '{col}' expected numeric type, got {df[col].dtype}")
                
        return len(errors) == 0, errors

"""Stratified train/validation/test dataset splitting with reproducible seeds."""

from typing import Tuple, Optional
import pandas as pd
from sklearn.model_selection import train_test_split

class DatasetSplitter:
    @staticmethod
    def split(
        df: pd.DataFrame,
        target_column: str = "churn",
        test_size: float = 0.20,
        val_size: float = 0.10,
        seed: int = 42
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        stratify = df[target_column] if target_column in df.columns else None
        
        train_val, test = train_test_split(
            df,
            test_size=test_size,
            random_state=seed,
            stratify=stratify
        )
        
        if val_size > 0:
            val_ratio = val_size / (1.0 - test_size)
            stratify_val = train_val[target_column] if target_column in train_val.columns else None
            train, val = train_test_split(
                train_val,
                test_size=val_ratio,
                random_state=seed,
                stratify=stratify_val
            )
            return train, val, test
        
        return train_val, pd.DataFrame(), test

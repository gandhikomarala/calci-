"""High-performance dataset ingestion and reader supporting CSV, JSON, and Parquet."""

import io
from pathlib import Path
from typing import Union, Optional
import pandas as pd
from packages.core.exceptions import DatasetError

class DatasetLoader:
    @staticmethod
    def load(file_source: Union[str, Path, bytes, io.BytesIO], data_format: str = "CSV") -> pd.DataFrame:
        try:
            fmt = data_format.upper()
            if isinstance(file_source, bytes):
                file_source = io.BytesIO(file_source)
                
            if fmt == "CSV":
                return pd.read_csv(file_source)
            elif fmt == "PARQUET":
                return pd.read_parquet(file_source)
            elif fmt == "JSON":
                return pd.read_json(file_source)
            else:
                raise DatasetError(f"Unsupported data format: {data_format}")
        except Exception as e:
            raise DatasetError(f"Failed to load dataset: {str(e)}")

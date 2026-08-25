"""PyArrow and Parquet storage optimization."""

from pathlib import Path
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

class ParquetHandler:
    @staticmethod
    def write_parquet(df: pd.DataFrame, output_path: Path, compression: str = "snappy") -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, str(output_path), compression=compression)

    @staticmethod
    def read_parquet(input_path: Path) -> pd.DataFrame:
        table = pq.read_table(str(input_path))
        return table.to_pandas()

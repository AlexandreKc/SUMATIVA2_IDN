import pandas as pd
import yaml
from pathlib import Path

class DataCatalog:
    def __init__(self, config_path: str = "catalog.yml"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    def load(self, name: str):
        entry = self.config.get(name)
        if not entry:
            raise ValueError(f"Dataset '{name}' no encontrado en el catálogo.")
        path = Path(entry["path"])
        dtype = entry.get("type", "csv")

        if dtype == "csv":
            return pd.read_csv(path)
        elif dtype == "parquet":
            return pd.read_parquet(path)
        elif dtype == "excel":
            return pd.read_excel(path)
        else:
            raise ValueError(f"Tipo de archivo no soportado: {dtype}")

    def save(self, name: str, df: pd.DataFrame):
        entry = self.config.get(name)
        if not entry:
            raise ValueError(f"Dataset '{name}' no encontrado en el catálogo.")
        path = Path(entry["path"])
        dtype = entry.get("type", "csv")

        if dtype == "csv":
            df.to_csv(path, index=False)
        elif dtype == "parquet":
            df.to_parquet(path, index=False)
        elif dtype == "excel":
            df.to_excel(path, index=False)
        else:
            raise ValueError(f"Tipo de archivo no soportado: {dtype}")
import pandas as pd
import os

def load_csv(file_name: str, base_path="data/raw/") -> pd.DataFrame:
    # Carrega um arquivo CSV da pasta data/raw.
    full_path = os.path.join(base_path, file_name)
    print(f"Extraindo {file_name}...")
    return pd.read_csv(full_path)
    
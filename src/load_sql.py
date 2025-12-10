import os
import sqlite3
import pandas as pd

def load_to_sqlite(df: pd.DataFrame, db_path="data/processed/olist.db", table_name="orders_processed"):
    """Carrega o dataframe em um banco SQLite."""

    # Garante que a pasta processed existe
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    print(f"🟦 Criando ou conectando ao banco SQLite: {db_path}")

    # Conecta ao banco
    conn = sqlite3.connect(db_path)

    print(f"📤 Carregando dados na tabela '{table_name}'...")

    # Carrega o DF no SQLite
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Dados carregados com sucesso no banco SQLite!")

def save_processed(df, filename="orders_processed.csv", base_path="data/processed/"):
    """Salva o dataframe transformado na pasta processed."""
    full_path = base_path + filename
    print(f"Salvando dataset transformado em {full_path} ...")
    df.to_csv(full_path, index=False)
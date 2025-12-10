from extract import load_csv
from transform import transform_orders
from load import save_processed
from load_sql import load_to_sqlite

from extract import load_csv
from transform import transform_orders
from load import save_processed
from load_sql import load_to_sqlite

def run_pipeline():

    print("\nIniciando Pipeline ETL Olist...\n")

    # EXTRACT
    orders = load_csv("olist_orders_dataset.csv")
    items = load_csv("olist_order_items_dataset.csv")
    customers = load_csv("olist_customers_dataset.csv")

    # TRANSFORM
    df_final = transform_orders(orders, items, customers)

    # LOAD - CSV
    save_processed(df_final)

    # LOAD - SQLite
    load_to_sqlite(df_final)

    print("\nPipeline ETL finalizado com sucesso!\n")

if __name__ == "__main__":
    run_pipeline()

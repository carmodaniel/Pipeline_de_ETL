import pandas as pd

def transform_orders(orders: pd.DataFrame, items: pd.DataFrame, customers: pd.DataFrame):
    print("🔧 Transformando dados...")

    # Convertendo datas
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")

    # Criar coluna: tempo de entrega real
    orders["delivery_time_days"] = (
        orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
    ).dt.days

    # Criar coluna: atraso da entrega
    orders["delivery_delay_days"] = (
        orders["order_delivered_customer_date"] - orders["order_estimated_delivery_date"]
    ).dt.days

    # Juntar com items (somatório por pedido)
    items_grouped = items.groupby("order_id").agg(
        total_items=("order_item_id", "count"),
        total_value=("price", "sum"),
        total_freight=("freight_value", "sum")
    ).reset_index()

    orders = orders.merge(items_grouped, on="order_id", how="left")

    # Juntar com clientes (cidade + estado)
    orders = orders.merge(customers[['customer_id','customer_city','customer_state']], 
                          on="customer_id",
                          how="left")

    return orders

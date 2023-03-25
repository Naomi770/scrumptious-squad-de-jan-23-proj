import pandas as pd
#  eventually this will need to be changed to read the parquet files from the aws s3 bucket
df_address = pd.read_csv('./database_access/data/csv/address.csv')
df_counterparty = pd.read_csv('./database_access/data/csv/counterparty.csv')
df_currency = pd.read_csv('./database_access/data/csv/currency.csv')
df_department = pd.read_csv('./database_access/data/csv/department.csv')
df_design = pd.read_csv('./database_access/data/csv/design.csv')
df_payment_type = pd.read_csv('./database_access/data/csv/payment_type.csv')
df_payment = pd.read_csv('./database_access/data/csv/payment.csv')
df_purchase_order = pd.read_csv('./database_access/data/csv/purchase_order.csv')
df_sales_order = pd.read_csv('./database_access/data/csv/sales_order.csv')
df_staff = pd.read_csv('./database_access/data/csv/staff.csv')
df_transaction = pd.read_csv('./database_access/data/csv/transaction.csv')

def create_facts_sales_order_table():
    
    sales_order_table = pd.DataFrame() 
    sales_order_table.insert(0, "sales_record_id", range(1, 1 + len(df_sales_order)))
    sales_order_table["sales_order_id"] = df_sales_order["sales_order_id"]
    sales_order_table["created_date"] = df_sales_order["created_at"]
    sales_order_table["created_time"] = df_sales_order["created_at"]
    sales_order_table["last_updated_date"] = df_sales_order["last_updated"]
    sales_order_table["last_updated_time"] = df_sales_order["last_updated"]
    sales_order_table["sales_staff_id"] = df_sales_order["staff_id"]
    sales_order_table["counterparty_id"] = df_sales_order["counterparty_id"]
    sales_order_table["units_sold"] = df_sales_order["units_sold"]
    sales_order_table["unit_price"] = df_sales_order["unit_price"]
    sales_order_table["currency_id"] = df_sales_order["currency_id"]
    sales_order_table["design_id"] = df_sales_order["design_id"]
    sales_order_table["agreed_payment_date"] = df_sales_order["agreed_payment_date"]
    sales_order_table["agreed_delivery_date"] = df_sales_order["agreed_delivery_date"]
    sales_order_table["agreed_delivery_location_id"] = df_sales_order["agreed_delivery_location_id"]


    return sales_order_table


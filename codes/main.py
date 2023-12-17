import pandas as pd

# loading orders.csv as dataframe
df=pd.read_csv("orders.csv")

# getting total sale per order
df['total_sales'] = df['product_price'] * df['quantity']

# changing order date to datetime format
df['order_date']=pd.to_datetime(df['order_date'],infer_datetime_format=True)


print("Sale Per Month")
print(df.groupby(df.order_date.dt.month)['product_price'].sum())

print("Sale by per product")
print(df.groupby('product_name')['total_sales'].sum())

print("Sale by per customer")
print(df.groupby('customer_id')['total_sales'].sum())


print("Top 10 Customers")
print(df.groupby('customer_id')['total_sales'].sum().nlargest(n=10))





import pandas as pd

sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"],
}

df = pd.DataFrame(sales_data)
print(df)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

df["revenue"] = df["price"] * df["quantity"]
print(df[["product", "revenue"]])
print(f"Total revenue: {df['revenue'].sum()}")

gorakhpur_sales = df[df["city"] == "Gorakhpur"]
print(gorakhpur_sales[["product", "quantity", "revenue"]])
print(df.groupby("category")["revenue"].sum())
print(df.groupby("city")["revenue"].sum())

product_revenue = df.groupby("product")["revenue"].sum()
print(f"Top product: {product_revenue.idxmax()}")

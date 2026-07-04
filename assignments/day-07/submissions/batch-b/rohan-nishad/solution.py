from pathlib import Path
import csv

base_dir = Path(__file__).resolve().parent
csv_file = base_dir / "sales_data.csv"

csv_file.write_text(
    "order_id,product,category,price,quantity,city\n"
    "ORD-001,Python Course,Online Course,999,2,Gorakhpur\n"
    "ORD-002,Data Analytics Course,Online Course,1499,1,Lucknow\n"
    "ORD-003,AI Workshop,Workshop,799,3,Gorakhpur\n"
    "ORD-004,Python Course,Online Course,999,1,Deoria\n"
    "ORD-005,Data Analytics Course,Online Course,1499,2,Gorakhpur\n"
    "ORD-006,AI Workshop,Workshop,799,1,Lucknow\n",
    encoding="utf-8",
)

with csv_file.open(newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

orders = len(rows)
print(f"Total orders: {orders}")

total_units = sum(int(row["quantity"]) for row in rows)
print(f"Total units sold: {total_units}")

total_revenue = sum(int(row["price"]) * int(row["quantity"]) for row in rows)
print(f"Total revenue: {total_revenue}")

average_order_revenue = round(total_revenue / orders, 2)
print(f"Average order revenue: {average_order_revenue}")

category_revenue = {}
for row in rows:
    category = row["category"]
    revenue = int(row["price"]) * int(row["quantity"])
    category_revenue[category] = category_revenue.get(category, 0) + revenue
print(category_revenue)

city_revenue = {}
for row in rows:
    city = row["city"]
    revenue = int(row["price"]) * int(row["quantity"])
    city_revenue[city] = city_revenue.get(city, 0) + revenue
print(city_revenue)

product_revenue = {}
for row in rows:
    product = row["product"]
    revenue = int(row["price"]) * int(row["quantity"])
    product_revenue[product] = product_revenue.get(product, 0) + revenue
print(f"Top product: {max(product_revenue, key=product_revenue.get)}")

gorakhpur_ids = [row["order_id"] for row in rows if row["city"] == "Gorakhpur"]
print(f"Gorakhpur order IDs: {gorakhpur_ids}")

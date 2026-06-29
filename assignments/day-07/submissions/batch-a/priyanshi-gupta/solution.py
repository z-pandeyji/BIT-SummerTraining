import csv

filename = "sales_data.csv"

orders = []

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        orders.append(row)

#1
print("Total orders:", len(orders))

# 2
total_units = sum(order["quantity"] for order in orders)
print("Total units sold:", total_units)

# 3
total_revenue = sum(
    order["price"] * order["quantity"]
    for order in orders
)
print("Total revenue:", total_revenue)

# 4
average_revenue = total_revenue / len(orders)
print("Average order revenue:", round(average_revenue, 2))

# Question 5: Category Revenue Report
category_revenue = {}

for order in orders:
    category = order["category"]
    revenue = order["price"] * order["quantity"]

    if category not in category_revenue:
        category_revenue[category] = 0

    category_revenue[category] += revenue

print("Category revenue:", category_revenue)

# 6
city_revenue = {}

for order in orders:
    city = order["city"]
    revenue = order["price"] * order["quantity"]

    if city not in city_revenue:
        city_revenue[city] = 0

    city_revenue[city] += revenue

print("City revenue:", city_revenue)

# 7
product_revenue = {}

for order in orders:
    product = order["product"]
    revenue = order["price"] * order["quantity"]

    if product not in product_revenue:
        product_revenue[product] = 0

    product_revenue[product] += revenue

top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)

# 8
gorakhpur_orders = [
    order["order_id"]
    for order in orders
    if order["city"] == "Gorakhpur"
]

print("Gorakhpur order IDs:", gorakhpur_orders)
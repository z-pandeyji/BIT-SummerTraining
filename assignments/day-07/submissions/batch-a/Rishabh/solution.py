import csv

# Read CSV file
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Question 1: Total orders
print("Total orders:", len(rows))

# Question 2: Total units sold
total_units = 0
for row in rows:
    total_units += int(row["quantity"])
print("Total units sold:", total_units)

# Question 3: Total revenue
total_revenue = 0
for row in rows:
    revenue = int(row["price"]) * int(row["quantity"])
    total_revenue += revenue
print("Total revenue:", total_revenue)

# Question 4: Average order revenue
average_revenue = total_revenue / len(rows)
print("Average order revenue:", round(average_revenue, 2))

# Question 5: Category revenue report
category_revenue = {}

for row in rows:
    category = row["category"]
    revenue = int(row["price"]) * int(row["quantity"])

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)

# Question 6: City revenue report
city_revenue = {}

for row in rows:
    city = row["city"]
    revenue = int(row["price"]) * int(row["quantity"])

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)

# Question 7: Top product
product_revenue = {}

for row in rows:
    product = row["product"]
    revenue = int(row["price"]) * int(row["quantity"])

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)

# Question 8: Gorakhpur orders
gorakhpur_orders = []

for row in rows:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)s
sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"}
]

#1
print("Total orders:", len(sales))

#2
total_quantity = 0
for item in sales:
    total_quantity += item["quantity"]
print("Total units sold:", total_quantity)

#3
total_revenue = 0
for item in sales:
    total_revenue += item["price"] * item["quantity"]
print("Total revenue:", total_revenue)

#4
gorakhpur_revenue = 0
for item in sales:
    if item["city"] == "Gorakhpur":
        gorakhpur_revenue += item["price"] * item["quantity"]
print("Gorakhpur revenue:", gorakhpur_revenue)

#5
category_revenue = {}
for item in sales:
    revenue = item["price"] * item["quantity"]

    if item["category"] in category_revenue:
        category_revenue[item["category"]] += revenue
    else:
        category_revenue[item["category"]] = revenue

print(category_revenue)

#6
city_revenue = {}
for item in sales:
    revenue = item["price"] * item["quantity"]

    if item["city"] in city_revenue:
        city_revenue[item["city"]] += revenue
    else:
        city_revenue[item["city"]] = revenue

print(city_revenue)

#7
product_revenue = {}
for item in sales:
    revenue = item["price"] * item["quantity"]

    if item["product"] in product_revenue:
        product_revenue[item["product"]] += revenue
    else:
        product_revenue[item["product"]] = revenue

top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)

#8
high_volume_products = []

for item in sales:
    if item["quantity"] >= 2:
        high_volume_products.append(item["product"])

print(high_volume_products)
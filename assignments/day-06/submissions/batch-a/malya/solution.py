# Day 6 Assignment
# Use only basic Python lists, dictionaries, loops, conditions, and functions. Do not use Pandas, NumPy, or any external library.

# Use this sales data in your program:
sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]

#1: Count Orders
# Expected Output-->Total orders: 6
total_orders = len(sales)
print("Total orders:", total_orders)


#2: Count Units Sold
# Expected Output:
# Total units sold: 10
total_units = 0
for record in sales:
    total_units += record["quantity"]
print("Total units sold:", total_units)


#3: Calculate Total Revenue
# Expected Output:
# Total revenue: 10690
total_revenue = 0
for record in sales:
    revenue = record["price"] * record["quantity"]
    total_revenue += revenue
print("Total revenue:", total_revenue)


#4: Filter Sales by City
# Expected Output:
# Gorakhpur revenue: 7393
gorakhpur_revenue = 0
for record in sales:
    if record["city"] == "Gorakhpur":
        revenue = record["price"] * record["quantity"]
        gorakhpur_revenue += revenue
print("Gorakhpur revenue:", gorakhpur_revenue)


#5: Revenue by Category
# Expected Output:
# {'Online Course': 7494, 'Workshop': 3196}
category_revenue = {}
for record in sales:
    category = record["category"]
    revenue = record["price"] * record["quantity"]
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue
print(category_revenue)


#6: Revenue by City
# Expected Output:
# {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
city_revenue = {}
for record in sales:
    city = record["city"]
    revenue = record["price"] * record["quantity"]
    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue
print(city_revenue)



#7: Best-Selling Product by Revenue
# Expected Output:
# Top product: Data Analytics Course
product_revenue = {}
for record in sales:
    product = record["product"]
    revenue = record["price"] * record["quantity"]

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue
top_product = ""
max_revenue = 0
for product in product_revenue:
    if product_revenue[product] > max_revenue:
        max_revenue = product_revenue[product]
        top_product = product
print("Top product:", top_product)


#8: High-Volume Products
# Expected Output:
# ['Python Course', 'AI Workshop', 'Data Analytics Course']
high_volume_products = []
for record in sales:
    if record["quantity"] >= 2:
        high_volume_products.append(record["product"])
print(high_volume_products)
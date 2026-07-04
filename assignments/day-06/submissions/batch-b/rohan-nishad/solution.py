sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]

print(f"Total orders: {len(sales)}")
print(f"Total units sold: {sum(item['quantity'] for item in sales)}")

total_revenue = sum(item['price'] * item['quantity'] for item in sales)
print(f"Total revenue: {total_revenue}")

gorakhpur_revenue = sum(item['price'] * item['quantity'] for item in sales if item['city'] == "Gorakhpur")
print(f"Gorakhpur revenue: {gorakhpur_revenue}")

category_revenue = {}
for item in sales:
    category_revenue[item['category']] = category_revenue.get(item['category'], 0) + item['price'] * item['quantity']
print(category_revenue)

city_revenue = {}
for item in sales:
    city_revenue[item['city']] = city_revenue.get(item['city'], 0) + item['price'] * item['quantity']
print(city_revenue)

product_revenue = {}
for item in sales:
    product_revenue[item['product']] = product_revenue.get(item['product'], 0) + item['price'] * item['quantity']

print(f"Top product: {max(product_revenue, key=product_revenue.get)}")

high_volume_products = [item['product'] for item in sales if item['quantity'] >= 2]
print(high_volume_products)

#assignment 7

#Question 1: Read the CSV File(Read all rows from sales_data.csv and print the total number of orders.)
# Expected Output:Total orders: 6

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    next(reader) 
    count = 0
    for row in reader:
        count += 1

print("Total orders:", count)


#Question 2: Total Units Sold(Calculate and print the total quantity sold.)
# Expected Output:Total units sold: 10

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    total_units = 0
    for row in reader:
        total_units += int(row["quantity"])  
        
print("Total units sold:", total_units)


#Question 3: Total Revenue(Calculate and print the total revenue from the CSV data.)
# Expected Output:Total revenue: 10690

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    total_revenue = 0
    for row in reader:
        total_revenue += int(row["price"]) * int(row["quantity"])

print("Total revenue:", total_revenue)


#Question 4: Average Order Revenue(Calculate total revenue divided by total orders. Round the result to 2 decimal places.)
# Expected Output:Average order revenue: 1781.67

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    total_revenue = 0
    total_orders = 0
    
    for row in reader:
        total_orders += 1
        total_revenue += int(row["price"]) * int(row["quantity"])

average_order_revenue = round(total_revenue / total_orders, 2)
print("Average order revenue:", average_order_revenue)


#Question 5: Category Revenue Report(Create and print a dictionary of total revenue by category.)
# Expected Output:{'Online Course': 7494, 'Workshop': 3196}

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    category_revenue = {}

    for row in reader:
        revenue = int(row["price"]) * int(row["quantity"])
        category = row["category"]
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue

print(category_revenue)


#Question 6: City Revenue Report(Create and print a dictionary of total revenue by city.)
# Expected Output:{'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    city_revenue = {}

    for row in reader:
        revenue = int(row["price"]) * int(row["quantity"])
        city = row["city"]
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue

print(city_revenue)


#Question 7: Top Product(Find the product with the highest total revenue and print it.)
# Expected Output:Top product: Data Analytics Course

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    product_revenue = {}

    for row in reader:
        revenue = int(row["price"]) * int(row["quantity"])
        product = row["product"]
        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

# Find product with maximum revenue
top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)


#Question 8: Gorakhpur Orders(Create a list of order_id values where the city is "Gorakhpur". Keep the CSV order and print the list.)
# Expected Output:Gorakhpur order IDs: ['ORD-001', 'ORD-003', 'ORD-005']

import csv

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    gorakhpur_orders = []

    for row in reader:
        if row["city"] == "Gorakhpur":
            gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)





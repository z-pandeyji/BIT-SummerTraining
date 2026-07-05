with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    total_order = 0
    
    for row in data:
        total_order += 1
        
    print(f"Total orders: {total_order}")
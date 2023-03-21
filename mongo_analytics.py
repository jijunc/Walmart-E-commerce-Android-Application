from pymongo import MongoClient
from datetime import datetime

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Connect to the "analytics" database and "sales" collection
db = client["analytics"]
sales = db["sales"]

# Insert sample data
sample_data = [
    {"product_id": 1, "product_name": "Laptop", "units_sold": 5, "date": datetime(2023, 1, 2)},
    {"product_id": 2, "product_name": "Smartphone", "units_sold": 3, "date": datetime(2023, 1, 2)},
    {"product_id": 3, "product_name": "Tablet", "units_sold": 2, "date": datetime(2023, 1, 2)},
    {"product_id": 1, "product_name": "Laptop", "units_sold": 4, "date": datetime(2023, 1, 3)},
    {"product_id": 2, "product_name": "Smartphone", "units_sold": 6, "date": datetime(2023, 1, 3)},
    {"product_id": 3, "product_name": "Tablet", "units_sold": 3, "date": datetime(2023, 1, 3)},
    {"product_id": 1, "product_name": "Laptop", "units_sold": 7, "date": datetime(2023, 1, 4)},
    {"product_id": 2, "product_name": "Smartphone", "units_sold": 5, "date": datetime(2023, 1, 4)},
    {"product_id": 3, "product_name": "Tablet", "units_sold": 1, "date": datetime(2023, 1, 4)}
]

sales.insert_many(sample_data)

# Total units sold
total_units_sold = sales.aggregate([
    {"$group": {"_id": None, "total": {"$sum": "$units_sold"}}}
])

print("Total units sold:", list(total_units_sold)[0]["total"])

# Units sold per product
units_sold_per_product = sales.aggregate([
    {"$group": {"_id": "$product_name", "total": {"$sum": "$units_sold"}}}
])

print("\nUnits sold per product:")
for product in units_sold_per_product:
    print(product["_id"], ":", product["total"])

# Daily sales
daily_sales = sales.aggregate([
    {"$group": {"_id": "$date", "total": {"$sum": "$units_sold"}}}
])

print("\nDaily sales:")
for day in daily_sales:
    print(day["_id"].strftime("%Y-%m-%d"), ":", day["total"])

# Close the connection
client.close()

import pandas as pd

def load_sales_data():
    return pd.read_csv("sales_data.csv")

def total_units_sold(sales_data):
    return sales_data["units_sold"].sum()

def units_sold_per_product(sales_data):
    return sales_data.groupby("product_name")["units_sold"].sum()

def daily_sales(sales_data):
    return sales_data.groupby("date")["units_sold"].sum()

def main():
    sales_data = load_sales_data()
    
    print("Total units sold:", total_units_sold(sales_data))
    print("\nUnits sold per product:")
    print(units_sold_per_product(sales_data))
    print("\nDaily sales:")
    print(daily_sales(sales_data))

if __name__ == "__main__":
    main()
In this example, the load_sales_data function loads sales data from the CSV file using pandas. The total_units_sold, units_sold_per_product, and daily_sales functions perform various data analytics operations on the sales data, such as calculating the total units sold, units sold per product, and daily sales, respectively.

Run the analytics.py script to see the results:

bash
Copy code
python analytics.py
Remember that this is a simple example. In real-world applications, data analytics can involve more complex calculations and data manipulation. You may also use additional libraries, like NumPy and matplotlib, for advanced analytics and data visualization.




Jijun Chen
can you use MongoDB for data analytics
Yes, you can use




Jijun Chen
how to use Google cloud platform as cloud database? can you show the real code?
To use Google Cloud Platform (GCP) as a cloud database, you can utilize Cloud Firestore or Cloud SQL. Cloud Firestore is a NoSQL database, while Cloud SQL is a fully managed relational database service.

Here, I'll demonstrate how to use Cloud Firestore with Python:

First, you need to create a new GCP project or use an existing one. Visit the GCP Console: https://console.cloud.google.com/

Enable the Firestore API for your project. Go to "Navigation menu > Firestore" and select "Create database."

Choose either "Production" or "Test" mode, and then pick a location for your database.

Install the required libraries:

bash
Copy code
pip install google-cloud-firestore
Set up authentication:

a. Go to the GCP Console: https://console.cloud.google.com/

b. Navigate to "IAM & Admin > Service accounts."

c. Click "Create Service Account," give it a name and description, and click "Create."

d. Grant the "Cloud Datastore User" role to the service account.

e. Click "Done" and then click the newly created service account.

f. Under "Keys," click "Add Key" and choose "JSON."

g. Save the JSON file, which contains your key, to your local machine.

Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON key file:

bash
Copy code
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"
Now, you can use Cloud Firestore in your Python code. Here's a simple example:
python
Copy code
from google.cloud import firestore

# Initialize Firestore
db = firestore.Client()

# Add a document to the 'users' collection
doc_ref = db.collection("users").document("user1")
doc_ref.set({
    "name": "John Doe",
    "age": 30,
    "city": "New York"
})

# Fetch a document from the 'users' collection
doc = db.collection("users").document("user1").get()
print(f"User data: {doc.to_dict()}")

# Query documents in the 'users' collection
users_ref = db.collection("users")
query = users_ref.where("age", ">=", 18).stream()

for user in query:
    print(f"{user.id} => {user.to_dict()}")
In this example, we first import the Firestore library and initialize a Firestore client.




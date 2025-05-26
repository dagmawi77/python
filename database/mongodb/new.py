from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to database
db = client["mydatabase"]

# Create or connect to collection
collection = db["mycollection"]

# Insert a document
doc = {"name": "John", "age": 30}
collection.insert_one(doc)

# Retrieve document
for item in collection.find():
    print(item)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabase"]
mycol=mydb["customers"]
myquery = { "address": "Highway 37" }

mycol.delete_one(myquery)

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")


x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")

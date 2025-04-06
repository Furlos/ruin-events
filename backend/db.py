import pymongo

# Step 1: Set up the database connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

user_collection = db["user"]
event_collection = db["event"]
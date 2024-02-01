from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
# replace the admin and <password> you have create before connect
uri = os.getenv("MONGODB_CONNECT_STRING") 
print(uri)
uri = "mongodb+srv://admin:admin123@cluster0.sizb9bz.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Create mongodb
db = client.kit
users_collection = db["users"]
conversations_collection = db["conversations"]
messages_collection = db["messages"]

def mongo_test_connection(): 
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
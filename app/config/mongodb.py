from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.settings import Settings

settings = Settings()
uri = settings.MONGODB_CONNECT_STRING
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
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import Settings

settings=Settings()
uri=settings.MONGODB_CONNECT_STRING
# There are 2 way to connect mongodb. 
# pymongo for synchronous Python applications.
# motor for asynchronous Python applications

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = AsyncIOMotorClient(uri)

# Create DB
db = client["kit"]
# db = client.kit
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
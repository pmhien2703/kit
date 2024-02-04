from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
# replace the admin and <password> you have create before connect
uri = os.getenv("MONGODB_CONNECT_STRING") 
print(uri)
uri = "mongodb+srv://admin:admin123@cluster0.sizb9bz.mongodb.net/?retryWrites=true&w=majority"

# There are 2 way to connect mongodb. 
# pymongo for synchronous Python applications.
# motor for asynchronous Python applications

# Create a new client and connect to the server

def get_db():
    client = AsyncIOMotorClient(uri)
    db = client["kit"]
    return db
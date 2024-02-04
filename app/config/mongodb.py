from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("MONGODB_CONNECT_STRING") 

# Create a new client and connect to the server
def get_db():
    client = AsyncIOMotorClient(uri)
    db = client["kit"]
    try:
        yield db
    finally:
        client.close()
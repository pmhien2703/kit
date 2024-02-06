from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import Settings

settings=Settings()
uri=settings.MONGODB_CONNECT_STRING

# Create a new client and connect to the server
def get_db():
    client = AsyncIOMotorClient(uri)
    db = client["kit"]
    try:
        yield db
    finally:
        client.close()
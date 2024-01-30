from typing import Union
from config.mongodb import mongo_test_connection
from fastapi import FastAPI
from api.users_router import user_router
from api.conversations_router import conversations_router
from api.messages_router import messages_router

app = FastAPI()
app.include_router(user_router)
app.include_router(conversations_router)
app.include_router(messages_router)

mongo_test_connection()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
from pydantic import BaseModel
from bson import ObjectId

# This is message database store the content of DM or Group Chat
class MessageModel(BaseModel):
    sender_id: ObjectId
    content: str
    chat_id: ObjectId
    read_by: list[ObjectId] #objectID list of user
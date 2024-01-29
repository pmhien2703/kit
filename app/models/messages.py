from pydantic import BaseModel
from bson import ObjectId

# This is message database store the content of DM or Group Chat
class MessageModel(BaseModel):
    sender: ObjectId # object id of user sender
    content: str
    chat: ObjectId #objectId of chat
    readby: list[ObjectId] #objectID list of user
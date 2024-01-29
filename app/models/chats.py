from pydantic import BaseModel
from bson import ObjectId
from mongoengine import Document, StringField, ListField, ReferenceField, BooleanField

class ChatModel(BaseModel):
    isGroupChat: bool # false = this is DM, true = this is a group chat
    users: list[ObjectId] # DM only have 2 users, Group chat > 2 users
    groupAdmin: ObjectId # DM don't have this field
    chatName: str
    latestMessage: ObjectId
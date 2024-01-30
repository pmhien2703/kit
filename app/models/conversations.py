from pydantic import BaseModel
from bson import ObjectId
from mongoengine import Document, StringField, ListField, ReferenceField, BooleanField

class ConversationModel(BaseModel):
    is_channel: bool = False 
    users: list[ObjectId] # DM only have 2 users, Group chat > 2 users
    group_admin: ObjectId | None
    channel_name: str
    latest_message: ObjectId
    
from pydantic import BaseModel
from bson.objectid import ObjectId
from mongoengine import Document, StringField, EmailField

class UserModel(BaseModel):
    username: str
    password: str
    fullname: str
    email: str
    avatar: str
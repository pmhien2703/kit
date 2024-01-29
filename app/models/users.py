from pydantic import BaseModel, EmailStr
from bson.objectid import ObjectId
from mongoengine import Document, StringField, EmailField

class UserModel(BaseModel):
    username: str = None | None
    password: str = None | None
    fullname: str = None | None
    email: EmailStr
    avatar: str = None | None
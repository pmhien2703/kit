from pydantic import BaseModel, EmailStr
from bson import ObjectId

class UserModel(BaseModel):
    username: str = None
    password: str = None
    fullname: str = None
    email: EmailStr
    avatar: str = None
from pydantic import BaseModel, EmailStr
from bson import ObjectId

class UserModel(BaseModel):
    username: str = None | None
    password: str = None | None
    fullname: str = None | None
    email: EmailStr
    avatar: str = None | None
from fastapi import APIRouter
from utils.users_serialize import individual_user, list_users
from config.mongodb import users_collection
from models.users import UserModel
from bson import ObjectId

user_router = APIRouter(prefix="/api/v1/user", tags=["User"])

@user_router.get("/")
async def get_users():
    users = users_collection.find()
    return list_users(users)

@user_router.post("/")
async def create_user(user: UserModel):
    check_user = users_collection.find_one({"email": user.email})
    if check_user:
        return {"message": "user already exist"}
    
    new_user = users_collection.insert_one(dict(user))
    result = users_collection.find_one({"_id": new_user.inserted_id})
    return individual_user(result)

@user_router.put("/{id}")
async def update_user(id: str, user: UserModel):
    updated_user = users_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return {"message": "Update success", "updated_user": individual_user(updated_user)}
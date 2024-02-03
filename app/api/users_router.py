from fastapi import APIRouter
from utils.users_serialize import individual_user, list_users
from config.mongodb import users_collection
from models.users import UserModel
from bson import ObjectId

user_router = APIRouter(prefix="/api/v1/user", tags=["User"])

@user_router.get("/")
async def get_users():
    users = await users_collection.find().to_list(None)
    return list_users(users)

@user_router.post("/")
async def create_user(user: UserModel):
    check_user = await users_collection.find_one({"email": user.email})
    if check_user:
        return {"message": "user already exist"}
    
    new_user = await users_collection.insert_one(dict(user))
    result = await users_collection.find_one({"_id": new_user.inserted_id})
    return individual_user(result)

@user_router.put("/{id}")
async def update_user(id: str, user: UserModel):
    updated_user = await users_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return {"message": "Update success", "updated_user": individual_user(updated_user)}
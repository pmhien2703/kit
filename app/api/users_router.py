from fastapi import APIRouter, Depends
from repositories.user import UserRepository
from utils.users_serialize import individual_user, list_users

user_router = APIRouter(prefix="/api/v1/user", tags=["User"])

@user_router.get("/{id}")
async def get_users(id: str, userRepo: UserRepository = Depends()):
    users = await userRepo.get_by_id(id)
    return users

# @user_router.post("/")
# async def create_user(user: UserModel):
#     check_user = await users_collection.find_one({"email": user.email})
#     if check_user:
#         return {"message": "user already exist"}
    
#     new_user = await users_collection.insert_one(dict(user))
#     result = await users_collection.find_one({"_id": new_user.inserted_id})
#     return individual_user(result)

# @user_router.put("/{id}")
# async def update_user(id: str, user: UserModel):
#     updated_user = await users_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
#     return {"message": "Update success", "updated_user": individual_user(updated_user)}
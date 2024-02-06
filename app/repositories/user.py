from fastapi import Depends
from .base import BaseRepository
from bson import ObjectId
from app.utils.users_serialize import individual_user, list_users
from app.config.mongodb import get_db
from app.models.users import UserModel


class UserRepository(BaseRepository):
    def __init__(self, users_collection) -> None:
        self.users_collection = users_collection

    async def get_by_id(self, id: str) -> dict:
        return individual_user(await self.users_collection.find_one({"_id": ObjectId(id)}))

    async def get_all(self):
        return await list_users(self.users_collection.find())

    async def create(self, user: UserModel):
        await self.users_collection.insert_one(user)

    async def update(self,id: str,  user: UserModel):
        await self.users_collection.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})

    async def remove(self, id: str):
        await self.users_collection.delete_one({"_id": ObjectId(id)})
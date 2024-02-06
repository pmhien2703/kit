from typing import Annotated
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import Depends
from app.config.mongodb import get_db
from app.repositories.user import UserRepository


class RepositoryManager:
    _db: AsyncIOMotorDatabase
    _user: UserRepository

    def __init__(self, db: Annotated[AsyncIOMotorDatabase,Depends(get_db)]) -> None:
        self._db = db
        self._user = None

    @property
    def user(self) -> UserRepository:
        if(self._user is None):
            self._user = UserRepository(self._db["users"])
        return self._user
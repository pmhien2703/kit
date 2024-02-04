from http import HTTPStatus
from fastapi import APIRouter, Depends
from models.users import UserModel
from repositories.user import UserRepository

user_router = APIRouter(prefix="/api/v1/user", tags=["User"])

@user_router.get("/{id}")
async def get_user(id: str, user_repo: UserRepository = Depends()) -> dict:
    users = await user_repo.get_by_id(id)
    return users

@user_router.get("/")
async def get_users(user_repo: UserRepository = Depends()) -> list[UserModel]:
    users = await user_repo.get_all()
    return users

@user_router.post("/")
async def create_user(user: UserModel, user_repo: UserRepository = Depends()):
    await user_repo.create(dict(user))
    return HTTPStatus.NO_CONTENT

@user_router.put("/{id}")
async def update_user(id: str, user: UserModel, user_repo: UserRepository = Depends()):
    await user_repo.update(id, user)
    return HTTPStatus.NO_CONTENT

@user_router.delete("/{id}")
async def update_user(id: str, user_repo: UserRepository = Depends()):
    await user_repo.remove(id)
    return HTTPStatus.NO_CONTENT

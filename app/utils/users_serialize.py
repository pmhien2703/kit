from app.models.users import UserModel

def individual_user(user) -> dict:
  return {
    "id": str(user["_id"]),
    "username": user["username"],
    "password": user["password"],
    "fullname": user["fullname"],
    "email": user["email"],
    "avatar": user["avatar"],
  }

#TODO Cuong will change this function to dynamic later
async def list_users(users) -> list[UserModel]:
  return [individual_user(user) for user in await users.to_list(100)]

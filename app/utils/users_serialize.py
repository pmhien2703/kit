def individual_user(user) -> dict:
  return {
    "id": str(user["_id"]),
    "username": user["username"],
    "password": user["password"],
    "fullname": user["fullname"],
    "email": user["email"],
    "avatar": user["avatar"],
  }

def list_users(users) -> list:
  return [individual_user(user) for user in users]

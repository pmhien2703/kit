from app.utils.users_serialize import individual_user, list_users

def individual_conversation(conversation) -> dict:
  return {
    "id": str(conversation["_id"]),
    "is_channel": conversation["is_channel"],
    "users": list_users(conversation["users"]),
    "group_admin": individual_user(conversation["group_admin"]),
    "channel_name": conversation["channel_name"],
    "latest_message": conversation["latest_message"],
  }
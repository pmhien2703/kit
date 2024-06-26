from pydantic import BaseModel
from typing import List, Optional

class ConversationModel(BaseModel):
    is_channel: bool = False 
    users: List[str]
    group_admin: Optional[str] = None
    channel_name: str
    latest_message: str


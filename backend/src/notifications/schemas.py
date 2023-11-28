from datetime import datetime 

from pydantic import BaseModel 


class NotificationRead(BaseModel):
    id: int 
    user_id: int 
    text: str 
    created_at: datetime
    is_read: bool 


class NotificationCreate(BaseModel):
    user_id: int
    text: str 


class NotificationList(BaseModel):
    notifications: list[NotificationRead] = []

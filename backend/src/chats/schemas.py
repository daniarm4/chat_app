from datetime import datetime

from pydantic import BaseModel, field_validator


class ChatRead(BaseModel):
    id: int 


class UserChats(BaseModel):
    chats: list[tuple[str, int]]


class ChatUsersAssociationCreate(BaseModel):
    users_username: list[str] 

    @field_validator('users_username')
    @classmethod
    def validate_user_length(cls, users_username: list[str]) -> list[str]:
        if len(users_username) != 2: 
            raise ValueError('User list must contain 2 elements')
        return users_username


class MessageRead(BaseModel):
    id: int 
    chat_id: int 
    sender_id: int 
    text: str 
    created_at: datetime 
    is_read: bool


class MessageList(BaseModel):
    messages: list[MessageRead]


class MessageCreate(BaseModel):
    chat_id: int
    sender_id: int 
    text: str 

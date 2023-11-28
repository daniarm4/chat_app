from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, Depends, WebSocket
from fastapi.websockets import WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.chats.websocket_manager import WebsocketConnectionManager
from src.chats.service import (
    create_chat_users_association, 
    create_chat as create_chat_, 
    get_chat_by_id_or_none,
    get_chat_messages as get_chat_messages_,
    get_all_user_chats,
    get_chat_by_two_users_or_none,
    create_message as create_message_
)
from src.chats.exceptions import ChatNotFoundException, ChatAlreadyExistsException
from src.chats.schemas import (
    ChatUsersAssociationCreate, 
    ChatRead,
    MessageList,
    UserChats,
    MessageCreate,
    MessageRead
)
from src.users.auth import get_current_user
from src.users.models import User

router = APIRouter(prefix='/chats')
ws_manager = WebsocketConnectionManager()


@router.post('/', response_model=ChatRead)
async def create_chat(assoc: ChatUsersAssociationCreate,
                      session: Annotated[AsyncSession, Depends(get_async_session)]):
    exists_chat = await get_chat_by_two_users_or_none(session=session, 
                                                      first_user_username=assoc.users_username[0],
                                                      second_user_username=assoc.users_username[1])
    if exists_chat:
        raise ChatAlreadyExistsException()
    chat = create_chat_(session=session)
    await session.commit()
    assoc_chat = await create_chat_users_association(session=session, assoc=assoc, chat_id=chat.id)
    await session.commit()
    return assoc_chat


@router.get('/by_user', response_model=UserChats)
async def get_chats_by_user_id(current_user: Annotated[User, Depends(get_current_user)],
                               session: Annotated[AsyncSession, Depends(get_async_session)]):
    chats = await get_all_user_chats(session=session, user_id=current_user.id)
    return {'chats': chats}


@router.get('/{chat_id}/messages', response_model=MessageList)    
async def get_chat_messages(chat_id: int,
                            session: Annotated[AsyncSession, Depends(get_async_session)],
                            current_user: Annotated[User, Depends(get_current_user)]):
    messages = await get_chat_messages_(chat_id=chat_id,
                                        session=session)
    return {'messages': messages}


@router.websocket('/ws/{chat_id}')
async def chat_websocket(websocket: WebSocket,
                        chat_id: int,
                        session: Annotated[AsyncSession, Depends(get_async_session)]):
    chat = await get_chat_by_id_or_none(session, chat_id=chat_id)
    if not chat:
        raise ChatNotFoundException()
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            message_data = data['message']
            message_create = MessageCreate(
                text=message_data['text'],
                sender_id=message_data['sender_id'],
                chat_id=message_data['chat_id']
            )
            await ws_manager.broadcast(json_data={
                'message': {
                    'text': message_data['text'], 
                    'sender_id': message_data['sender_id'],
                    'chat_id': message_data['chat_id'],
                    'created_at': str(datetime.now()),
                }}
            )
            await create_message_(session=session, message_create=message_create)
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)

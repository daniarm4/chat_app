from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.notifications.schemas import (
    NotificationCreate, 
    NotificationRead, 
    NotificationList
)
from src.notifications.service import (
    create_notification as create_notification_, 
    get_notification_by_id_or_none, 
    get_notifications_by_user,
    mark_as_read,
    delete_notification,
    delete_notifications_by_user
)
from src.notifications.exceptions import NotificationNotFoundException
from src.users.service import get_user_by_id_or_none
from src.users.exceptions import UserNotFoundException
from src.users.models import User
from src.users.auth import get_current_user

router = APIRouter(prefix='/notifications')


@router.post('/', response_model=NotificationRead)
async def create_notification(notification_create: NotificationCreate,
                              session: Annotated[AsyncSession, Depends(get_async_session)]):
    user = await get_user_by_id_or_none(session=session, user_id=notification_create.user_id)
    if not user:
        raise UserNotFoundException()
    notification = create_notification_(session=session, 
                                        notification_create=notification_create)
    await session.commit() 
    return notification


@router.get('/by_user', response_model=NotificationList)
async def get_notifications_by_user_id(current_user: Annotated[User, Depends(get_current_user)],
                                       session: Annotated[AsyncSession, Depends(get_async_session)]):
    notifications = await get_notifications_by_user(session=session, 
                                                    user_id=current_user.id)
    return {'notifications': notifications}


@router.get('/{notification_id}', response_model=NotificationRead)
async def get_notification_by_id(notification_id: int,
                                 current_user: Annotated[User, Depends(get_current_user)],
                                 session: Annotated[AsyncSession, Depends(get_async_session)]):
    notification = await get_notification_by_id_or_none(session=session, 
                                                        notification_id=notification_id,
                                                        user_id=current_user.id)
    if not notification:
        raise NotificationNotFoundException()
    return notification


@router.post('/as_read', response_model=NotificationRead)
async def mark_notification_as_read(notification_id: int,
                                    current_user: Annotated[User, Depends(get_current_user)],
                                    session: Annotated[AsyncSession, Depends(get_async_session)]):
    notification = await get_notification_by_id_or_none(session=session, 
                                                        notification_id=notification_id,
                                                        user_id=current_user.id)
    if not notification:
        raise NotificationNotFoundException()
    await mark_as_read(session=session,
                       notification_id=notification_id,
                       user_id=current_user.id)
    await session.commit()
    return notification


@router.delete('/by_user', response_model=None)
async def delete_notifications_by_user_id(current_user: Annotated[User, Depends(get_current_user)],
                                          session: Annotated[AsyncSession, Depends(get_async_session)]):
    await delete_notifications_by_user(session=session, user_id=current_user.id)
    await session.commit()
    return None 


@router.delete('/{notification_id}', response_model=None)
async def delete_notification(notification_id: int, 
                              current_user: Annotated[User, Depends(get_current_user)],
                              session: Annotated[AsyncSession, Depends(get_async_session)]):
    notification = await get_notification_by_id_or_none(session=session,
                                                        notification_id=notification_id,
                                                        user_id=current_user.id)
    if not notification:
        raise NotificationNotFoundException()
    await delete_notification(session=session, notification=notification)
    await session.commit()
    return None

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, and_

from src.notifications.models import Notification
from src.notifications.schemas import NotificationCreate


def create_notification(session: AsyncSession, 
                        notification_create: NotificationCreate) -> Notification:
    notification = Notification(
        user_id=notification_create.user_id,
        text=notification_create.text
    )
    session.add(notification)
    return notification


async def get_notification_by_id_or_none(session: AsyncSession, 
                                         notification_id: int, 
                                         user_id: int) -> Notification | None:
    query = (
        select(Notification)
        .where(and_(Notification.id==notification_id, Notification.user_id==user_id))
    )
    notification = await session.scalar(query)
    return notification
    

async def get_notifications_by_user(session: AsyncSession, user_id: int) -> list[Notification]:
    query = select(Notification).where(Notification.user_id==user_id)
    result = await session.scalars(query)
    notifications = result.all()
    return notifications


async def delete_notification(session: AsyncSession, notification: Notification) -> None:
    await session.delete(notification)


async def mark_as_read(session: AsyncSession, notification_id: int, user_id: int) -> None:
    stmt = (
        update(Notification)
        .where(and_(Notification.id==notification_id, Notification.user_id==user_id))
        .values(is_read=True)
    )
    await session.execute(stmt)


async def delete_notifications_by_user(session: AsyncSession, user_id: int) -> None:
    stmt = (
        delete(Notification)
        .where(Notification.user_id==user_id)
    )
    await session.execute(stmt)

from sqlalchemy import select, or_, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User
from src.chats.models import Chat, Message
from src.chats.schemas import ChatUsersAssociationCreate, MessageCreate
from src.chats.assocs import assoc_chat_user


async def get_chat_by_id_or_none(session: AsyncSession, chat_id: int) -> Chat | None:
    chat = await session.get(Chat, chat_id)
    return chat


def create_chat(session: AsyncSession) -> Chat:
    chat = Chat()
    session.add(chat)
    return chat


async def get_all_user_chats(session: AsyncSession,
                             user_id: int):
    subquery = (
        select(Chat.id)
        .join(assoc_chat_user)
        .where(assoc_chat_user.c.user_id==user_id)
    )
    query = (
        select(User.username, assoc_chat_user.c.chat_id)
        .join(assoc_chat_user)
        .where(
            and_(
                assoc_chat_user.c.chat_id.in_(subquery),
                User.id != user_id
            )
        )
    )
    result = await session.execute(query)
    return result.all()


async def get_chat_by_two_users_or_none(session: AsyncSession,
                                        first_user_username: str,
                                        second_user_username: str):
    subquery = (
        select(Chat.id)
        .join(assoc_chat_user)
        .join(User)
        .where(User.username==first_user_username)
    )
    query = (
        select(Chat.id)
        .join(assoc_chat_user)
        .join(User)
        .where(
            and_(
                assoc_chat_user.c.chat_id.in_(subquery), 
                User.username==second_user_username
            )
        )
    )
    result = await session.scalar(query)
    return result


async def create_chat_users_association(session: AsyncSession, 
                                        assoc: ChatUsersAssociationCreate,
                                        chat_id: Chat):
    first_user_username, second_user_username = assoc.users_username[0], assoc.users_username[1]
    first_user, second_user = await session.scalars(
        select(User)
        .where(or_(User.username==first_user_username, User.username==second_user_username))
    )
    chat = await session.scalar(
        select(Chat)
        .where(Chat.id==chat_id)
    )
    chat.users = [first_user, second_user]
    return chat


async def get_chat_messages(session: AsyncSession,
                            chat_id: int) -> list[Message]:
    query = (
        select(Message)
        .where(Message.chat_id==chat_id)
        .order_by(Message.id)
    )    
    result = await session.scalars(query)
    messages = result.all()
    return messages


async def create_message(session: AsyncSession, message_create: MessageCreate) -> Message:
    message = Message(
        chat_id=message_create.chat_id,
        sender_id=message_create.sender_id,
        text=message_create.text
    )
    session.add(message)
    await session.commit()
    return message

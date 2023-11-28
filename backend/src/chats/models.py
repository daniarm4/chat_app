from datetime import datetime 

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func

from src.chats.assocs import assoc_chat_user
from src.database import Base 


class Chat(Base):
    __tablename__ = 'chat'

    id: Mapped[int] = mapped_column(primary_key=True)
    
    messages: Mapped[list['Message']] = relationship(back_populates='chat') 
    users: Mapped[list['User']] = relationship(secondary=assoc_chat_user, 
                                               back_populates='chats',
                                               lazy='selectin')


class Message(Base):
    __tablename__ = 'message'

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id', ondelete='CASCADE'))
    sender_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    is_read: Mapped[bool] = mapped_column(default=False)

    chat: Mapped['Chat'] = relationship(back_populates='messages', cascade='all, delete')
    sender: Mapped['User'] = relationship(back_populates='messages', cascade='all, delete')

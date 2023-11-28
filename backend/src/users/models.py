from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from src.chats.assocs import assoc_chat_user
from src.database import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    hashed_password: Mapped[str]
    avatar_url: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    
    chats: Mapped[list['Chat']] = relationship(secondary=assoc_chat_user, 
                                               back_populates='users',
                                               lazy='selectin')
    messages: Mapped['Message'] = relationship(back_populates='sender')
    notifications: Mapped[list['Notification']] = relationship(back_populates='user')
    
    def __repr__(self) -> str:
        return f"""User(
            id: {self.id},
            username: {self.username}
        )"""

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, func

from src.database import Base


class Notification(Base):
    __tablename__ = 'notification'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    text: Mapped[str] = mapped_column(String(50))
    is_read: Mapped[bool] = mapped_column(default=False)

    user: Mapped['User'] = relationship(back_populates='notifications')

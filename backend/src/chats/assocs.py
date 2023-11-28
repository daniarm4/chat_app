from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint

from src.database import Base 

assoc_chat_user = Table(
    'assoc_chat_user', 
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('chat_id', Integer, ForeignKey('chat.id', ondelete='CASCADE'), nullable=False),
    Column('user_id', Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False),
    UniqueConstraint('chat_id', 'user_id', name='idx_unique_chat_user')
)

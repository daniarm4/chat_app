from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.users.routers import router as user_router
from src.notifications.routers import router as notification_router
from src.chats.routers import router as chat_router

app = FastAPI()

app.include_router(user_router)
app.include_router(notification_router)
app.include_router(chat_router)

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://localhost:3000',
    'https://127.0.0.1:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
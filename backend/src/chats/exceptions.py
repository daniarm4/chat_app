from fastapi import status

from src.exceptions import BaseHTTPException


class ChatNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Chat with this credentials not found'


class ChatAlreadyExistsException(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Chat between two users has already been created'

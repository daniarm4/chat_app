from fastapi import status

from src.exceptions import BaseHTTPException


class NotificationNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Notitification with this credentials not found'

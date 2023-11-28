from fastapi import status

from src.exceptions import BaseHTTPException


class UserNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'User with this credentials not found'


class UserAlreadyExistsException(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'User with this credentials already exists'


class UserIsUnauthorized(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Could not validate credentials'

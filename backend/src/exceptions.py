from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    status_code = None 
    detail = None 
    headers = None 

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail, self.headers)

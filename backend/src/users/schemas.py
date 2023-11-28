from pydantic import BaseModel, Field, SecretStr, model_validator


class Tokens(BaseModel):
    access_token: str
    refresh_token: str 


class AccessToken(BaseModel):
    access_token: str


class UserBase(BaseModel):
    username: str = Field(max_length=50)
    is_active: bool = True


class UserLogin(BaseModel):
    username: str = Field(max_length=50)
    password: SecretStr = Field(min_length=8, max_length=16) 


class UserRead(UserBase):
    id: int


class UserCreate(UserBase):
    password: SecretStr = Field(min_length=8, max_length=16)
    re_password: SecretStr = Field(min_length=8, max_length=16)

    @model_validator(mode='after')
    def validate_passwords(self) -> 'UserCreate':
        password = self.password
        re_password = self.re_password

        if password != re_password: 
            raise ValueError('Passwords do not match')
        return self

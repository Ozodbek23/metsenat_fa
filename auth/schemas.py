from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class TokenSchemas(BaseModel):
    access_token: str
    refresh_token: str
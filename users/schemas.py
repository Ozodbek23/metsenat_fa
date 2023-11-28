from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    full_name: str
    is_active: bool


    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    username: str
    full_name: str
    password: str
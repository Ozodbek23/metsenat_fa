from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from config.dependencies import get_db
from users import services

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

security = HTTPBasic()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db, username: str, password: str):
    user = services.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_user(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
        db: Session = Depends(get_db)
):
    user = authenticate_user(db, credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid credentials')
    return user

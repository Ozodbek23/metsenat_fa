from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from users import services

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
SECRET_KEY = 'ThisISSecretKeyForMyProject'
ALGORITHM = 'HS256'


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


def create_access(user_id: int):
    exp = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        'sub': str(user_id),
        'exp': exp
    }
    access_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return access_token


def create_refresh(user_id: int):
    exp = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    payload = {
        'sub': str(user_id),
        'exp': exp
    }
    refresh_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return refresh_token

def decode_jwt(token:str) -> dict:
    try:
        decoded_token = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
        )
        return decoded_token if decoded_token['exp'] >= datetime.utcnow().timestamp() else None
    except:
        return {}
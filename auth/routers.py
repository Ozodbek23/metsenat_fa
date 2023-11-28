from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session

from auth import schemas
from auth.utils import authenticate_user, create_access, create_refresh
from config.dependencies import get_db

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/login/')
async def login(credentials: schemas.LoginSchema, db: Session = Depends(get_db)):
    user = authenticate_user(db, credentials.username, credentials.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    result = {
        'access_token': create_access(user_id=user.id),
        'refresh_token': create_refresh(user_id=user.id)
    }
    return result

    return
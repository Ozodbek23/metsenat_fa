from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic
from sqlalchemy.orm import Session
from auth.auth_bearer import JWTBearer

from config.dependencies import get_db
from users import schemas, services
from users.utils import get_current_user, get_password_hash

security = HTTPBasic()

router = APIRouter(prefix='/users', tags=['Users'])

@router.post('/', response_model=schemas.UserSchema)
async def create_user(user: schemas.UserCreateSchema , db:Session = Depends(get_db)):
    model = services.get_user_by_username(db, user.username)
    if model:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this username exists!")
    user.password = get_password_hash(user.password)
    model = services.create_user(db, user)
    return model



@router.get('/get-me/')
async def get_me(
        credentials = Depends(JWTBearer()),
        db: Session = Depends(get_db)
):
    user_id = credentials.get('sub')
    model = services.get_user_by_id(db, user_id)
    return model

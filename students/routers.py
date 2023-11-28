from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from config.dependencies import get_db
from students import schemas, services
from users.utils import get_current_user

router = APIRouter(prefix='/student', tags=['students'])


@router.get('/', response_model=List[schemas.StudentSchema])
async def get_students(skip: int = 0, limit: int = 25,
                       db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    students = services.get_students(skip, limit, db)
    return students


@router.post('/', response_model=schemas.StudentCreateSchema, status_code=201)
async def create_students(student: schemas.StudentCreateSchema, db: Session = Depends(get_db),
                          current_user=Depends(get_current_user)):
    model = services.create_student(db, student)
    return model


@router.get('/{student_id}/', response_model=schemas.StudentDetailSchema)
async def get_student_detail(student_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    model = services.get_student_by_id(db, student_id)

    if model:
        return model
    return HTTPException(status_code=404, detail=f'Student with id: {student_id} not found')


@router.put('/{student_id}/', response_model=schemas.StudentSchema)
async def update_student(student_id: int, student: schemas.StudentCreateSchema, db: Session = Depends(get_db),
                         current_user=Depends(get_current_user)):
    model = services.get_student_by_id(db, student_id)
    if not model:
        raise HTTPException(status_code=404, detail='Student not found')
    model = services.update_student_by_id(db, student, model)
    return model


@router.delete('/{student_id}/', status_code=204)
async def delete_student(student_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    model = services.get_student_by_id(db, student_id)
    if not model:
        raise HTTPException(status_code=404, detail='Stduent not found')
    model = services.delete_student(db, model)
    return {'delete': True}

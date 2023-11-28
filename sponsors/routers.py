from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from config.dependencies import get_db
from sponsors import schemas, services
from users.utils import get_current_user

router = APIRouter(prefix='/sponsors', tags=['Sponsors'])


@router.get('/', response_model=schemas.SponsorSchema)
async def get_sponsors(skip: int = 0, limit: int = 25, db: Session = Depends(get_db),
                       current_user=Depends(get_current_user)):
    sponsors = services.get_sponsors(skip, limit, db)
    return sponsors


@router.post('/', response_model=schemas.SponsorDetail)
async def create_sponsors(sponsor: schemas.SponsorCreate, db: Session = Depends(get_db),
                          current_user=Depends(get_current_user)):
    model = services.create_sponsor(db, sponsor)
    return model


@router.get('/{sponsor_id}/', response_model=schemas.SponsorDetail)
async def get_sponsor_detail(sponsor_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    model = services.get_sponsor_by_id(sponsor_id, db)
    if not model:
        raise HTTPException(status_code=404, detail='Sponsor not found')
    return model


@router.put('/{sponsor_id}/', response_model=schemas.SponsorSchema)
async def update_sponsor(sponsor_id: int, sponsor: schemas.SponsorCreate, db: Session = Depends(get_db),
                         current_user=Depends(get_current_user)):
    model = services.get_sponsor_by_id(sponsor_id, db)
    if not model:
        raise HTTPException(status_code=404, detail='Sponsor not found')

    model = services.update_sponsor(db, sponsor, model)
    return model


@router.delete('/{sponsor_id}/', status_code=204)
async def delete_sponsor(sponsor_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    model = services.get_sponsor_by_id(sponsor_id, db)
    if not model:
        raise HTTPException(status_code=404, detail='Sponsor not found')
    services.delete_sponsor(db, model)
    return {'deleted': True}

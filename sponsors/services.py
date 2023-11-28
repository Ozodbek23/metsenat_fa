from sponsors.models import Sponsors


def get_sponsors(skip, limit, db):
    return db.query(Sponsors).offset(skip).limit(limit).all()


def create_sponsor(db, sponsor):
    model = Sponsors(**sponsor.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def get_sponsor_by_id(sponsor_id, db):
    return db.query(Sponsors).filter(Sponsors.id == sponsor_id).first()


def update_sponsor(db, sponsor, model):
    for key, val in sponsor.dict().items():
        setattr(model, key, val)

    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def delete_sponsor(db , model):
    db.delete(model)
    db.commit()

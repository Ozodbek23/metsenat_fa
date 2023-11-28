from users.model import User


def create_user(db, user):
    model = User(**user.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def get_user_by_username(db, username):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db, user_id):
    return db.query
from students.models import Student


def get_students(skip, limit, db):
    return db.query(Student).offset(skip).limit(limit).all()


def create_student(db, student):
    model = Student(**student.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def get_student_by_id(db, student_id):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student_by_id(db, student, model):
    for key, val in student.dict().items():
        setattr(model, key, val)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def delete_student(db, model):
    db.delete(model)
    db.commit()
from sqlalchemy import Integer, Column, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base
from students.choices import StudentEducationType


class Institute(Base):

    __tablename__ = 'institute'

    id = Column(Integer , autoincrement=True , index=True, primary_key=True)
    name = Column(String(length=125))
    students = relationship('Student',  back_populates='institutes')

    def __str__(self):
        return f'{self.name}'




class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer , primary_key=True , index=True , autoincrement=True)
    full_name = Column(String(length=125))
    phone_number = Column(String(length=13))
    type = Column(Enum(StudentEducationType))
    institute = Column(Integer , ForeignKey('institute.id'))
    contract_amount = Column(Integer)
    institutes = relationship('Institute', back_populates='students')


    def __str__(self):
        return f'{self.full_name}'


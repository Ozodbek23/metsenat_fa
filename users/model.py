from sqlalchemy import Column, Integer, String, Boolean

from config.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(length=50), unique=True)
    full_name = Column(String(length=125))
    password = Column(String)
    is_active = Column(Boolean, default=True)

    def __str__(self):
        return f"{self.full_name}"
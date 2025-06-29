from sqlalchemy import Column, Integer, String, Boolean
from models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) #ЮЗЕРАЙДИ должен быть уникален блять, знаешь почему? потомучто блять
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
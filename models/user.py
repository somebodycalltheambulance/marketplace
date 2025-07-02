from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum
import enum
from models import Base


class RoleEnum(enum.Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) #ЮЗЕРАЙДИ должен быть уникален блять, знаешь почему? потомучто блять
    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SqlEnum(RoleEnum), nullable=False, default=RoleEnum.user)
    is_active = Column(Boolean, default=True)
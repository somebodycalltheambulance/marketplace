from pydantic import BaseModel, EmailStr
from enum import Enum


class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"

#Базовая схема - все общее
class UserBase(BaseModel):
    email: EmailStr
    username: str

#Для создания пользователя(регистрация)
class UserCreate(UserBase):
    password: str
    email: EmailStr
    role: RoleEnum = RoleEnum.user  # ПО ДЕФОЛТУ ОБЫЧНЫЙ ЮЗЕР


#Для отображения наружу( то шо видно(без пароля))
class UserOut(UserBase):
    id: int
    email: EmailStr
    role: RoleEnum

    class Config:
        from_attributes=True  #Позволяет работать с ORM моделями напрямую


#Эта хуета валидирует логин бзера
class UserLogin(BaseModel):
    email: EmailStr
    password: str
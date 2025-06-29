from pydantic import BaseModel, EmailStr

#Базовая схема - все общее
class UserBase(BaseModel):
    email: EmailStr
    username: str

#Для создания пользователя(регистрация)
class UserCreate(UserBase):
    password: str


#Для отображения наружу( то шо видно(без пароля))
class UserOut(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True  #Позволяет работать с ORM моделями напрямую


#Эта хуета валидирует логин бзера
class UserLogin(BaseModel):
    email: EmailStr
    password: str
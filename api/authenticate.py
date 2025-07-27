from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from auth.security import verify_password, create_access_token
from db.session import get_async_session
from models.user import User

auth_router = APIRouter()

@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_async_session)):
    user = db.query(User).filter(User.email==form_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Неверный e-mail")
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Неверный пароль")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut, UserLogin
from auth.auth import register_user
from db.session import get_db
from models.user import User
from auth.security import verify_password, create_access_token

auth_router = APIRouter()

@auth_router.post("/login")
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user =db.query(User).filter(User.email==user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid EMAIL SUKA")
    if not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid EMAIL BLYAT")
    
    access_token = create_access_token(data={'sub': str(user.id)})
    
    return {"acess_token": access_token,
            "token_type": "bearer"}
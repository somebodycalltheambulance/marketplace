from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut, UserLogin
from auth.auth import register_user
from db.session import get_db
from models.user import User
from auth.security import verify_password, create_access_token
from dependencies.auth import get_current_user

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = register_user(user, db)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return User

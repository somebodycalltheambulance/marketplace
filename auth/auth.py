from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.user import User
from schemas.user import UserCreate
from auth.security import hash_password


def register_user(user_data: UserCreate, db: Session) -> User:
    new_user = User(email=user_data.email,
                     username=user_data.username, 
                     hashed_password=hash_password(user_data.password),
                     )
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise ValueError("User with this email or username already exists")
    
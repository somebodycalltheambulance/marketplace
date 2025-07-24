from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.user import User
from schemas.user import UserCreate
from auth.security import hash_password

# Асинхронная регистрация пользователя
async def register_user(user_data: UserCreate, db: AsyncSession) -> User:
    new_user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hash_password(user_data.password),  # можно оставить sync
    )
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except IntegrityError:
        await db.rollback()
        raise ValueError("User with this email or username already exists")

    
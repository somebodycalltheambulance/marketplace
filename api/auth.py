from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserCreate, UserOut, UserLogin
from auth.auth import register_user
from db.session import get_async_session
from models.user import User
from auth.security import verify_password, create_access_token
from dependencies.auth import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_async_session),
):
    try:
        new_user = await register_user(user, db)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(
    user_data: UserLogin,
    db: AsyncSession = Depends(get_async_session),
):
    from sqlalchemy.future import select

    result = await db.execute(select(User).where(User.email == user_data.email))
    user = result.scalars().first()

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
async def get_me(user: User = Depends(get_current_user)):
    return user

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_async_session
from schemas.category import CategoryCreate, CategoryRead
from repositories.category import create_category, get_all_categories

router = APIRouter(prefix="/categories")


@router.post("/", response_model=CategoryRead)
async def create(category_data: CategoryCreate, db: AsyncSession = Depends(get_async_session)):
    return await create_category(db, category_data)


@router.get("/", response_model=list[CategoryRead])
async def read_all(db: AsyncSession = Depends(get_async_session)):
    return await get_all_categories(db)

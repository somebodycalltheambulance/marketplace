from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.category import CategoryCreate, CategoryRead
from repositories.category import create_category, get_all_categories

router = APIRouter(prefix="/categories")


@router.post("/", response_model=CategoryRead)
def create(category_data: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category_data)


@router.get("/", response_model=list[CategoryRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_categories(db)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.phones import PhoneCreate, PhoneRead
from repositories.phone import create_phone, get_all_phones

router = APIRouter(prefix="/phones")

@router.post("/", response_model=PhoneRead)
def create(phone_data: PhoneCreate, db: Session = Depends(get_db)):
    return create_phone(db, phone_data)

@router.get("/", response_model=list[PhoneRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_phones(db)

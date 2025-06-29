from sqlalchemy.orm import Session
from models.phone import Phone
from schemas.phones import PhoneCreate

def create_phone(db: Session, phone_data: PhoneCreate) -> Phone:
    phone = Phone(**phone_data.dict())
    db.add(phone)
    db.commit()
    db.refresh(phone)
    return phone

def get_all_phones(db: Session):
    return db.query(Phone).all()
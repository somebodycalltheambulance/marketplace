from pydantic import BaseModel
from typing import Optional

class PhoneBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int

class PhoneCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int

class PhoneRead(BaseModel):
    id: int

    class Config:
        orm_mode = True
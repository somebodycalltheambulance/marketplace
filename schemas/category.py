from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(BaseModel):
    name: str
    

class CategoryRead(BaseModel):
    id: int

    class Config:
        orm_mode = True
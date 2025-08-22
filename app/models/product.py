from pydantic import BaseModel

class Product(BaseModel):
    id: int
    ten: str
    gia: float

class ProductCreate(BaseModel):
    ten: str
    gia: float

from pydantic import BaseModel

class User(BaseModel):
    id: int
    ten: str
    tuoi: int
    sdt: str

class UserCreate(BaseModel):
    ten: str
    tuoi: int
    sdt: str

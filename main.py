from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Cho phép gọi API từ giao diện HTML/JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # cho phép tất cả origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# User
class User(BaseModel):
    id: int
    ten: str
    tuoi: int
    sdt: str

class UserCreate(BaseModel):
    ten: str
    tuoi: int
    sdt: str


db: List[User] = [
    User(id=1, ten="Nguyen Van A", tuoi=25, sdt="0123456789"),
    User(id=2, ten="Tran Thi B", tuoi=30, sdt="0987654321"),
]


def get_next_id():
    return max([u.id for u in db], default=0) + 1

@app.get("/users", response_model=List[User])
def get_users():
    return db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for u in db:
        if u.id == user_id:
            return u

@app.post("/users", response_model=User)
def add_user(user: UserCreate):
    new_user = User(id=get_next_id(), **user.dict())
    db.append(new_user)
    return new_user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    for i, u in enumerate(db):
        if u.id == user_id:
            updated_user = User(id=user_id, **user.dict())
            db[i] = updated_user
            return updated_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, u in enumerate(db):
        if u.id == user_id:
            db.pop(i)
            return {"message": "Xoá thành công"}

# Product
class Product(BaseModel):
    id: int
    ten: str
    gia: float

class ProductCreate(BaseModel):
    ten: str
    gia: float
db_products: List[Product] = [
    Product(id=1, ten="Iphone 15", gia=23000000),
    Product(id=2, ten="Laptop Dell", gia=18000000),
]
def get_next_product_id():
    return max([p.id for p in db_products], default=0) + 1

@app.get("/products", response_model=List[Product])
def get_products():
    return db_products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for p in db_products:
        if p.id == product_id:
            return p

@app.post("/products", response_model=Product)
def add_product(product: ProductCreate):
    new_product = Product(id=get_next_product_id(), **product.dict())
    db_products.append(new_product)
    return new_product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductCreate):
    for i, p in enumerate(db_products):
        if p.id == product_id:
            updated_product = Product(id=product_id, **product.dict())
            db_products[i] = updated_product
            return updated_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, p in enumerate(db_products):
        if p.id == product_id:
            db_products.pop(i)
            return {"message": "Xoá thành công"}

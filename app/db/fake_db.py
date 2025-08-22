from typing import List
from app.models.user import User
from app.models.product import Product

# Fake DB
db_users: List[User] = [
    User(id=1, ten="Nguyen Van A", tuoi=25, sdt="0123456789"),
    User(id=2, ten="Tran Thi B", tuoi=30, sdt="0987654321"),
]

db_products: List[Product] = [
    Product(id=1, ten="Iphone 15", gia=23000000),
    Product(id=2, ten="Laptop Dell", gia=18000000),
]

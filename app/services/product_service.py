from typing import List, Optional
from app.models.product import Product, ProductCreate
from app.db.fake_db import db_products

def get_next_id() -> int:
    return max([p.id for p in db_products], default=0) + 1

def get_products() -> List[Product]:
    return db_products

def get_product(product_id: int) -> Optional[Product]:
    for p in db_products:
        if p.id == product_id:
            return p
    return None

def add_product(product: ProductCreate) -> Product:
    new_product = Product(id=get_next_id(), **product.dict())
    db_products.append(new_product)
    return new_product

def update_product(product_id: int, product: ProductCreate) -> Optional[Product]:
    for i, p in enumerate(db_products):
        if p.id == product_id:
            updated_product = Product(id=product_id, **product.dict())
            db_products[i] = updated_product
            return updated_product
    return None

def delete_product(product_id: int) -> bool:
    for i, p in enumerate(db_products):
        if p.id == product_id:
            db_products.pop(i)
            return True
    return False

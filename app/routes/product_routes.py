from fastapi import APIRouter, HTTPException
from typing import List
from app.models.product import Product, ProductCreate
from app.services import product_service

router = APIRouter()

@router.get("/", response_model=List[Product])
def get_products():
    return product_service.get_products()

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=Product)
def add_product(product: ProductCreate):
    return product_service.add_product(product)

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductCreate):
    updated_product = product_service.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}")
def delete_product(product_id: int):
    success = product_service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Xoá thành công"}

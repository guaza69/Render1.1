from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Este router funciona como una mini-app independiente
router = APIRouter(
    prefix="/products",
    tags=["Products Service"]
)

# Modelo de datos exclusivo de Productos
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

fake_products_db = [
    {"id": 1, "name": "Laptop Developer", "price": 1200.50, "stock": 5},
    {"id": 2, "name": "Teclado Mecánico", "price": 85.00, "stock": 10}
]

@router.get("/", response_model=List[Product])
def get_products():
    return fake_products_db

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = next((p for p in fake_products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product
from fastapi import FastAPI, HTTPException
from botiga_db import read, create, update_units, delete_product, products_schema
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    description: str
    company: str
    price: float
    units: int
    subcategory_id: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def read_products():
    return products_schema(read())

@app.post("/create_product")
async def create_product(data: Product):
    name = data.name
    description = data.description
    company = data.company
    price = data.price
    units = data.units
    subcategory_id = data.subcategory_id
    product_id = create(name, description, company, price, units, subcategory_id)
    return {
        "msg": "Data successfully created",
        "product_id": product_id,
        "name": name
    }

@app.put("/update_units/{product_id}")
def update_product_units(product_id: int, units: int):
    update_units(product_id, units)

@app.delete("/delete_product/{product_id}")
def delete_product_endpoint(product_id: int):
    delete_product(product_id)

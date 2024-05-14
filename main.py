from fastapi import FastAPI, HTTPException
from botiga_db import product_schema, read, read_product, create, update_units, delete_product, read_all_products_info, products_schema
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

@app.get("/product/{product_id}")
def read_product_by_id(product_id: int):
    product = read_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product_schema(product)

@app.post("/product")
async def create_new_product(data: Product):
    product_id = create(
        data.name, data.description, data.company, data.price, data.units, data.subcategory_id
    )
    return {
        "msg": "Producto creado exitosamente",
        "product_id": product_id,
        "name": data.name
    }
# El put solo modifica UNIDADES de UN producto 
@app.put("/updateProductUnits/{product_id}")
def update_product(product_id: int, data: Product):
    update_units(product_id, data.units)
    return {"msg": "Producto actualizado exitosamente"}

@app.delete("/product/{product_id}")
def delete_product_by_id(product_id: int):
    delete_product(product_id)
    return {"msg": "Producto eliminado exitosamente"}

@app.get("/productAll")
def read_all_products_info_endpoint():
    return read_all_products_info()
 
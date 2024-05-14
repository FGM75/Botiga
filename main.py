import csv
from fastapi import FastAPI, File, HTTPException, UploadFile
from botiga_db import check_product_exists, check_subcategory_exists, create_category, create_product, create_subcategory, product_schema, read, read_product, create, update_category, update_subcategory, update_units, delete_product, read_all_products_info, products_schema, check_category_exists, update_product
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
def update_product_units(product_id: int, data: Product):
    update_units(product_id, data.units)
    return {"msg": "Producto actualizado exitosamente"}

@app.delete("/product/{product_id}")
def delete_product_by_id(product_id: int):
    delete_product(product_id)
    return {"msg": "Producto eliminado exitosamente"}

@app.get("/productAll")
def read_all_products_info_endpoint():
    return read_all_products_info()

@app.post("/loadProducts")
async def load_products(file: UploadFile = File(...)):
    try:
        with open(file.filename, "wb") as buffer:
            buffer.write(file.file.read())
        
        with open(file.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                category_name = row['nom_categoria']
                subcategory_name = row['nom_subcategoria']
                product_name = row['nom_producto']
                description = row['descripcion_producto']
                company = row['companyia']
                price = float(row['precio'])
                units = int(row['unidades'])

                category_id = check_category_exists(category_name)
                if category_id is None:
                    category_id = create_category(category_name)
                else:
                    update_category(category_name, category_id)

                subcategory_id = check_subcategory_exists(subcategory_name, category_id)
                if subcategory_id is None:
                    subcategory_id = create_subcategory(subcategory_name, category_id)
                else:
                    update_subcategory(subcategory_name, subcategory_id)

                product_id = check_product_exists(product_name, subcategory_id)
                if product_id is None:
                    create_product(product_name, description, company, price, units, subcategory_id)
                else:
                    update_product(product_name, description, company, price, units, product_id)

    except Exception as e:
        return {"status": "error", "message": f"Error de carga: {e}" }

    return {"status": "success", "message": "Carga CSV completa!"}
 
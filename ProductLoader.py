from fastapi import File, UploadFile, APIRouter
from typing import List
import csv
from datetime import datetime

router = APIRouter()

class ProductLoader:
    def __init__(self, file: UploadFile):
        self.file = file

    def load_products(self):
        try:
            categories = set()
            subcategories = set()
            products = []

            # Llegir el fitxer CSV
            contents = self.file.file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(contents)

            for row in reader:
                category = row.get('category')
                subcategory = row.get('subcategory')
                product_name = row.get('product_name')

                # Registrar categories i subcategories
                if category:
                    categories.add(category)
                if subcategory:
                    subcategories.add(subcategory)

                # Afegir producte
                products.append({
                    "category": category,
                    "subcategory": subcategory,
                    "product_name": product_name
                })

            # Processar categories
            for category in categories:
                if not self.category_exists(category):
                    self.create_category(category)
                else:
                    self.update_category(category)

            # Processar subcategories
            for subcategory in subcategories:
                if not self.subcategory_exists(subcategory):
                    self.create_subcategory(subcategory)
                else:
                    self.update_subcategory(subcategory)

            # Processar productes
            for product_data in products:
                category = product_data['category']
                subcategory = product_data['subcategory']
                product_name = product_data['product_name']

                if not self.product_exists(product_name):
                    self.create_product(category, subcategory, product_name)
                else:
                    self.update_product(product_name)

            return {"message": "Products loaded successfully"}

        except Exception as e:
            return {"message": f"Error loading products: {e}"}

    def category_exists(self, category):
        # Implementa la lògica per comprovar si la categoria existeix a la BD
        pass

    def create_category(self, category):
        # Implementa la lògica per crear una nova categoria a la BD
        pass

    def update_category(self, category):
        # Implementa la lògica per actualitzar la categoria a la BD
        pass

    def subcategory_exists(self, subcategory):
        # Implementa la lògica per comprovar si la subcategoria existeix a la BD
        pass

    def create_subcategory(self, subcategory):
        # Implementa la lògica per crear una nova subcategoria a la BD
        pass

    def update_subcategory(self, subcategory):
        # Implementa la lògica per actualitzar la subcategoria a la BD
        pass

    def product_exists(self, product_name):
        # Implementa la lògica per comprovar si el producte existeix a la BD
        pass

    def create_product(self, category, subcategory, product_name):
        # Implementa la lògica per crear un nou producte a la BD
        pass

    def update_product(self, product_name):
        # Implementa la lògica per actualitzar el producte a la BD
        pass

@router.post("/loadProducts")
async def load_products(file: UploadFile = File(...)):
    product_loader = ProductLoader(file)
    return product_loader.load_products()
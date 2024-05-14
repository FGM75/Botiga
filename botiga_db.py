from mysqlConnect import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM product")
        result = cur.fetchall()
    except Exception as e:
        return {"status": -1, "messages": f"Error de conexión: {e}"}
    finally:
        conn.close()
    return result

def read_product(product_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
        result = cur.fetchone()
    except Exception as e:
        return {"status": -1, "messages": f"Error de conexión: {e}"}
    finally:
        conn.close()
    return result

def create(name, description, company, price, units, subcategory_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "INSERT INTO product (name, description, company, price, units, subcategory_id) VALUES (%s,%s,%s,%s,%s,%s);"
        values = (name, description, company, price, units, subcategory_id)
        cur.execute(query, values)
        conn.commit()
        product_id = cur.lastrowid
    except Exception as e:
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        conn.close()
    return product_id

def update_units(product_id, units):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE product SET units = %s WHERE product_id = %s;"
        values = (units, product_id)
        cur.execute(query, values)
        conn.commit()
    except Exception as e:
        return {"status": -1, "messages": f"Error de conexión: {e}"}
    finally:
        conn.close()

def delete_product(product_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM product WHERE product_id = %s;"
        cur.execute(query, (product_id,))
        conn.commit()
    except Exception as e:
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        conn.close()

def read_all_products_info():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """
            SELECT c.name AS category_name, s.name AS subcategory_name, p.name AS product_name, p.company, p.price
            FROM product p
            JOIN subcategory s ON p.subcategory_id = s.subcategory_id
            JOIN category c ON s.category_id = c.category_id
        """
        cur.execute(query)
        result = cur.fetchall()
    except Exception as e:
        return {"status": -1, "messages": f"Error de conexión: {e}"}
    finally:
        conn.close()
    return result

def product_schema(product) -> dict:
    return {
        "product_id": product[0],
        "name": product[1],
        "description": product[2],
        "company": product[3],
        "price": product[4],
        "units": product[5],
        "subcategory_id": product[6]
    }

def products_schema(products) -> dict:
    return [product_schema(product) for product in products]
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

def check_category_exists(name):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT category_id FROM category WHERE name = %s"
        cur.execute(query, (name,))
        category = cur.fetchone()
        if category:
            return category[0]
        else:
            return None
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def create_category(name):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "INSERT INTO category (name) VALUES (%s)"
        cur.execute(query, (name,))
        conn.commit()
        category_id = cur.lastrowid
        return category_id
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def update_category(name, category_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE category SET name = %s WHERE category_id = %s"
        cur.execute(query, (name, category_id))
        conn.commit()
        updated_rows = cur.rowcount
        return updated_rows
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def check_subcategory_exists(name, category_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT subcategory_id FROM subcategory WHERE name = %s AND category_id = %s"
        cur.execute(query, (name, category_id))
        subcategory = cur.fetchone()
        if subcategory:
            return subcategory[0]
        else:
            return None
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def create_subcategory(name, category_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "INSERT INTO subcategory (name, category_id) VALUES (%s, %s)"
        cur.execute(query, (name, category_id))
        conn.commit()
        subcategory_id = cur.lastrowid
        return subcategory_id
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def update_subcategory(name, subcategory_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE subcategory SET name = %s WHERE subcategory_id = %s"
        cur.execute(query, (name, subcategory_id))
        conn.commit()
        updated_rows = cur.rowcount
        return updated_rows
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def check_product_exists(name, subcategory_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT product_id FROM product WHERE name = %s AND subcategory_id = %s"
        cur.execute(query, (name, subcategory_id))
        product = cur.fetchone()
        if product:
            return product[0]
        else:
            return None
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def create_product(name, description, company, price, units, subcategory_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "INSERT INTO product (name, description, company, price, units, subcategory_id) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (name, description, company, price, units, subcategory_id))
        conn.commit()
        product_id = cur.lastrowid
        return product_id
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()

def update_product(name, description, company, price, units, product_id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE product SET name = %s, description = %s, company = %s, price = %s, units = %s WHERE product_id = %s"
        cur.execute(query, (name, description, company, price, units, product_id))
        conn.commit()
        updated_rows = cur.rowcount
        return updated_rows
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
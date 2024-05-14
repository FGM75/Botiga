## Botiga - API de gestión de productos
Este proyecto es una API REST desarrollada con FastAPI que permite la gestión de productos en una tienda online.

### Características
Crear, leer, actualizar y eliminar productos
Consultar información detallada de todos los productos
Cargar productos desde un archivo CSV
Gestión de categorías y subcategorías de productos

### Endpoints
Método	Ruta	Descripción
- GET	/	Ruta raíz
- GET	/products	Obtener todos los productos
- GET	/product/{product_id}	Obtener un producto por ID
- POST	/product	Crear un nuevo producto
- PUT	/updateProductUnits/{product_id}	Actualizar las unidades de un producto
- DELETE	/product/{product_id}	Eliminar un producto
- GET	/productAll	Obtener información detallada de todos los productos
- POST	/loadProducts

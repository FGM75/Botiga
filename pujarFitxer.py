import requests

file_path = "llista_productes.csv"

with open(file_path, "rb") as file:
    files = {"file": file}
    
    response = requests.post("http://127.0.0.1:8000/loadProducts", files=files)

print(response.json())

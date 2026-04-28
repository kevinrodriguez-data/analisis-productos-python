
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def valor_total(self):
        return self.precio * self.stock

    def es_caro(self):
        return self.precio > 500
    

productos = [
    Producto("Laptop", 1000, 5),
    Producto("Mouse", 50, 20),
    Producto("Teclado", 80, 10),
    Producto("Monitor", 300, 3)
] 

resultado = [
    {"nombre": p.nombre, 
    "valor_total": p.valor_total()} 
    for p in productos]


ordenado = sorted(resultado, key=lambda x: x["valor_total"], reverse=True)

print(ordenado)
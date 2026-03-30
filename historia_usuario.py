# Programa de inventario
# Este programa solicita el nombre, precio y cantidad de un producto,
# valida los datos ingresados, calcula el costo total y muestra el resultado.

# ---------------------------
# Solicitar nombre del producto
# ---------------------------
nombre = input("Ingrese el nombre del producto: ")

# ---------------------------
# Solicitar y validar precio
# ---------------------------
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: el precio no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Error: debe ingresar un número válido.")

# ---------------------------
# Solicitar y validar cantidad
# ---------------------------
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Error: debe ingresar un número entero válido.")

# ---------------------------
# Calcular costo total
# ---------------------------
costo_total = precio * cantidad

# ---------------------------
# Mostrar resultados
# ---------------------------
print("\n--- Resultado ---")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# ---------------------------
# Comentario final del programa
# ---------------------------
# Este programa permite registrar un producto en un inventario solicitando
# nombre, precio y cantidad. Valida que los datos numéricos sean correctos,
# calcula el costo total y muestra toda la información de forma clara.



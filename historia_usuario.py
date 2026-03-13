#Programa de registro de producto en inventario
# Este programa solicita el nombre del producto, su precio y la cantidad.
# Luego calcula el costo total y muestra la información en pantalla.

# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio del producto y validar que sea un número
while :
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# Solicitar la cantidad y validar que sea un número entero
while :
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

# Calcular el costo total
costo_total = precio * cantidad

# Mostrar los resultados en consola
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

# Este programa permite registrar un producto en el inventario,
# validar los datos ingresados por el usuario, calcular el costo total
# (precio por cantidad) y mostrar toda la información de forma clara.


#acomodar el while
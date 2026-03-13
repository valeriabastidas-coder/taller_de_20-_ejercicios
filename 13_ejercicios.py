total_dia = 0

while True:
    producto = input("Producto (cafe, capuchino, pastel) o salir: ")
    if producto == "salir":
        break

    cantidad = int(input("Cantidad: "))

    if producto == "cafe":
        precio = 4000
    elif producto == "capuchino":
        precio = 7000
    elif producto == "pastel":
        precio = 6000

    total = precio * cantidad

    if total > 20000:
        total *= 0.9

    print("Total cliente:", total)
    total_dia += total

print("Total del día:", total_dia)


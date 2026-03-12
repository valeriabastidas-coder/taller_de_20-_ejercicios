caros = 0

for i in range(6):
    precio = int(input("Precio: "))
    if precio > 100000:
        caros += 1

print("Productos caros:", caros)


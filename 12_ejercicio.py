 bajo = medio = alto = 0

for i in range(5):
    nombre = input("Nombre: ")
    dias = int(input("Dias asistidos: "))

    if dias < 3:
        bajo += 1
    elif dias <= 4:
        medio += 1
    else:
        alto += 1

print("Bajo:", bajo)
print("Medio:", medio)
print("Alto:", alto)

capacidad = int(input("Capacidad sala: "))

niños = adultos = mayores = 0

for i in range(capacidad):
    edad = int(input("Edad: "))

    if edad < 18:
        niños += 1
    elif edad < 60:
        adultos += 1
    else:
        mayores += 1

print("Niños:", niños)
print("Adultos:", adultos)
print("Adultos mayores:", mayores)

edad = int(input("ingrese su edad" ))

if 13 >= edad <= 17:
    print("clase juvenil")
elif 18 >= edad <= 59:
    print("clase general")
elif 60 >= edad:
    print("clase senior")
else:
    print ("si eres menor de 13 no puede entrar")
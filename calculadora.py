'''''''''''''''''''''''''''''''''''
numero = 0
opcion = 0
opcion = input("calcular")
base = int(input("ingresa la base: "))
altura = int(input("ingrese la altura: "))
radio = int(input("ingrese el radio"))
π = int(input )


    print("\nMENU:\n1.rectangulo\n2.circulo\n3.trapecio\n4.paralelogramo\n5.cono\n6.cilindro\n7.esfera\n8prisma rectangular\n9.triángulo rectángulo\n10.Salir.")
    numero = int(input("ingresa el numero: "))
    if numero == 1:
        print("que quiere pedir?\1.area:\n2.perimetro:")
        if opcion == 1:
            area = base * altura 
        elif opcion == 2:
            perimetro =  2** (base + altura)
        else: 
            print("opcion invalida")

    elif numero == 2:
        print("que quiere pedir?\n1.area\n2.perimetro (circunferencia)")
        if opcion == 1:
            area = radio 


    elif numero == 3:
        pass
    elif numero == 4:
        pass
    elif numero == 5:
        pass
    elif numero == 6:
        pass
    elif numero == 7:
        pass
    elif numero == 8:
        pass
    elif numero == 9:
        pass
    elif numero == 10:
        print("saliste del programa")
    else:
        print("opcion invalida vuelva a intentarlo")
'''''''''''''''''''''''''''''''''''

pi = 3.1416

opcion = -1

while opcion != 0:
    print("\nCALCULADORA GEOMÉTRICA")
    print("1. Figuras 2D")
    print("2. Figuras 3D")
    print("3. Triángulo rectángulo")
    print("0. Salir")
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("error")
        continue

    # FIGURAS 2D
    if opcion == 1:
        print("\nFiguras 2D")
        print("1. Rectángulo")
        print("2. Círculo")
        print("3. Triángulo")
        print("4. Trapecio")

        figura = int(input("Elige una figura: "))

        if figura == 1:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = base * altura
            print("Área del rectángulo:", area)

        elif figura == 2:
            radio = float(input("Ingrese el radio: "))
            area = pi * radio ** 2
            print("Área del círculo:", area)

        elif figura == 3:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = (base * altura) / 2
            print("Área del triángulo:", area)

        elif figura == 4:
            base_mayor = float(input("Ingrese la base mayor: "))
            base_menor = float(input("Ingrese la base menor: "))
            altura = float(input("Ingrese la altura: "))
            area = ((base_mayor + base_menor) * altura) / 2
            print("Área del trapecio:", area)

    # FIGURAS 3D
    elif opcion == 2:
        print("\nFiguras 3D")
        print("1. Esfera")
        print("2. Cilindro")
        print("3. Cono")
        print("4. Prisma rectangular")

        figura = int(input("Elige una figura: "))

        if figura == 1:
            radio = float(input("Ingrese el radio: "))
            volumen = (4/3) * pi * radio ** 3
            print("Volumen de la esfera:", volumen)

        elif figura == 2:
            radio = float(input("Ingrese el radio: "))
            altura = float(input("Ingrese la altura: "))
            volumen = pi * radio ** 2 * altura
            print("Volumen del cilindro:", volumen)

        elif figura == 3:
            radio = float(input("Ingrese el radio: "))
            altura = float(input("Ingrese la altura: "))
            volumen = (pi * radio ** 2 * altura) / 3
            print("Volumen del cono:", volumen)

        elif figura == 4:
            largo = float(input("Ingrese el largo: "))
            ancho = float(input("Ingrese el ancho: "))
            altura = float(input("Ingrese la altura: "))
            volumen = largo * ancho * altura
            print("Volumen del prisma rectangular:", volumen)

    # TRIÁNGULO RECTÁNGULO
    elif opcion == 3:
        print("\nTriángulo Rectángulo")

        cateto1 = float(input("Ingrese el primer cateto: "))
        cateto2 = float(input("Ingrese el segundo cateto: "))

        hipotenusa = pi.sqrt(cateto1**2 + cateto2**2)

        print("La hipotenusa es:", hipotenusa)

    elif opcion == 0:
        print("Programa finalizado")

    else:
        print("Opción inválida")



compromiso_bajo = 0
compromiso_medio = 0
compromiso_alto = 0

for i in range (0,5,1):
    nombre = input("pedir nombre")
    dias = int(input("numero de dias"))
    minutos = int(input("minutos por dias"))    

    if 3 <= dias <= 4:
    
        print("compriso medio")
        compromiso_medio +=1
    elif dias >= 5:
        print("compromiso alto")
        compromiso_alto +=1
    else:
        print("menos de tres dias compromiso bajo")
        compromiso_bajo +=1
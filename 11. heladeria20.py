contador_cono = 0
contador_vaso = 0
contador_banana_split = 0

act = True
cadena = " "
cliente = 0

while(act):
    p = int(input("cono\nvaso\nbanana split"))
if p == "cono":
    contador_cono += 1
    cliente += 1
elif p == "vaso":
    contador_vaso += 1
    cliente += 1
elif p == "banana":
    contador_banana_split += 1
    cliente += 1
    
    agregar = int(input("desea agregar otro cliente"))
if agregar == 1:
    ventas = contador_cono * 3000 + contador_vaso * 4000 + contador_banana_split * 9000

cadenas = f"el cliente nro {cliente} paga {ventas} pesos"

contador_cono = 0
contador_vaso = 0
contador_banana_split = 0
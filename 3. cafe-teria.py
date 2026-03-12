
cafe = 4000
te = 3500
jugo = 5000

bebida = input("pida su bebida: \n ")
unidades = int(input ("cuantas unidades desea comprar: \n"))
if (bebida == "cafe"):
    total = unidades*cafe
elif (bebida == "te"):
    total = unidades*te
elif (bebida == "jugo"):
    total = unidades*jugo

print("el precio de su compra es", total)


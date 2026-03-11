
cafe = 4000
te = 3500
jugo = 5000

bebida = input("pida su bebida")
unidades = int(input ("cuantas unidades desea comprar"))
if (bebida == "cafe"):
    total = unidades*cafe
elif (bebida == "te"):
    total = unidades*te
elif (bebida == "jugo"):
    total = unidades*jugo

print("el precio de su compra es", total)

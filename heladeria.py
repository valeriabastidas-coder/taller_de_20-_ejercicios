v = 0 #("vainilla")
f = 0 #("fresa")
ch = 0 #("chocolte")

for i in range (0,5,1):
    sabores = input ("elige un salor entre, \nvainilla, \nchocolate  \nfresa")
    if (sabores == "v"):
        v += 1
    elif (sabores == "f"):
        f += 1
    elif (sabores == "ch"):
        ch += 1

print("cantidad de vainilla", v, "cantidad de fresa", f, "cantidad de chocolate", ch)

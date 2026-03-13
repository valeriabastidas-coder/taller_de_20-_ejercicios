total = 0
carros = motos = 0
max_pago = 0

for i in range(8):
    placa = input("Placa: ")
    tipo = input("Tipo (carro/moto): ")
    horas = int(input("Horas: "))

    if tipo == "carro":
        pago = horas * 4000
        carros += 1
    else:
        pago = horas * 2000
        motos += 1

    if pago > max_pago:
        max_pago = pago

    total += pago

print("Total recaudado:", total)
print("Carros:", carros)
print("Motos:", motos)
print("Pago mayor:", max_pago)


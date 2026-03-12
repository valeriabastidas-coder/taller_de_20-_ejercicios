primera_hora = 5000
cada_hora_adicional = 3000

n = int(input('Ingrese cuantas horas lleva:'))
x = 0

if n == 1:
    print('Total horas: ', n, '\nTotal a pagar: ', primera_hora)
else:
    x = primera_hora + (cada_hora_adicional * n)
    print('Total horas: ', n, '\nTotal a pagar: ', x)
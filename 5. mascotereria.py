'''
tipo_de_mascota = input("que tipo de mascota tiene?\n")
perro = input("purina")
gato = input("el pescado")
conejo = input("las zanahorias")
if perro == tipo_de_mascota:
    print("el alimento para su perro es el arroz con carne")
elif gato == tipo_de_mascota:
    print("el alimento para su gato es el pescado")
elif conejo == tipo_de_mascota:
    print("el alimento para su conejo es las zanaorias")
else:
    print
    
'''    
rec = ['purina', 'croquetas para gat','zanahoria']
ani = ['Perro', 'Gato', 'Conejo']
a = input('Ingrese su mascota: ')

if a == ani[0]:
    print(rec[0])
elif a == ani[1]:
    print(rec[1])
elif a == ani[2]:
    print(rec[2])

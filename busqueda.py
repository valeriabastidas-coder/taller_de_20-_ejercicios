lista_creada = [2, 3, 5, 8, 21, 52, 63, 85]





def mostrar_encontrado(pos, valor):
    print(f"Numero encontrado en la posicion {pos} -> {valor}")
    return True


def buscar_numero(numero:int, lista):
    encontrado = False
    pi = 0
    pd = len(lista) - 1
    encontrado = False
    if numero == lista[pi]:
             encontrado = mostrar_encontrado(pi, lista[pi])
             return encontrado
    if numero == lista[pd]:
            encontrado = mostrar_encontrado(pd, lista[pd])
            return encontrado
      
    while pi <= pd and not encontrado:
            pm = (pi + pd) // 2

            if numero == lista[pm]:
                encontrado = mostrar_encontrado(pm, lista[pm])

            elif numero > lista[pm]:
                pi = pm + 1
            else:
                pd = pm - 1
    return encontrado

def main():
    op = ""
    while op != "salir":
        op = input("Deseas buscar un numero (si/salir)")
        if op  == "si":
            numero = int(input("Ingresa el numero a buscar: "))
            encontrado = buscar_numero(numero, lista_creada)
            if not encontrado:
                print("Numero no encontrando")

main()      
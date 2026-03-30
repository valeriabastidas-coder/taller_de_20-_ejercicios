#Sistema de Gestion de Estudiantes conpersistencia de datos
#listas, Diccionario, Tuplas
import csv
import os
ARCHIVO = 'usuarios.csv'
estudiantes = [
    "id",
    "nombre",
    "edad",
    "curso o programa",
    "estado"] 

def ingrese_estudiantes():
    ingresar =[
    "id",
    "nombre",
    "edad",
    "curso o programa",
    "estado"
]
    float(input(Ingrese = 
        ["id",
        "nombre",
        "edad",
        "curso o programa",
        "estado"]))

def ingresar_estudiantes():
    """Crea el archivo con encabezados si no existe."""
    if not os.path.exists(estudiantes):
        with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=estudiantes)
            writer.writeheader()

def crear_registro(datos):
    """Crea (Añade) un nuevo registro al final del archivo."""
    ingresar_estudiantes()
    with open(ARCHIVO, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=estudiantes)
        writer.writerow(datos)

def leer_registros():
    """Lee y retorna todos los registros como una lista de diccionarios."""
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, mode='r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def actualizar_registro(id_buscado, nuevos_datos):
    """Busca por ID y reemplaza la fila correspondiente."""
    filas = leer_registros()
    actualizado = False
    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=estudiantes)
        writer.writeheader()
        for fila in filas:
            if fila['id'] == str(id_buscado):
                writer.writerow(nuevos_datos)
                actualizado = True
            else:
                writer.writerow(fila)
    return actualizado

def eliminar_registro(id_buscado):
    """Elimina una fila filtrando por ID."""
    filas = leer_registros()
    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=estudiantes)
        writer.writeheader()
        for fila in filas:
            if fila['id'] != str(id_buscado):
                writer.writerow(fila)

i = -1

while i != 0:
    print(["hola admi",
        "quieres ingresar a un estudiantes?"])
    print("1. yes")
    print("0. not")
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("error")
        continue
    
    if opcion == 1:
        mi_lista = [
            "id",
            "nombre"
            ,"edad",
            "curso o programa",
            "estado",
            ]
        print(mi_lista)
        try:
            datos = int(input("escriba los datos: "))
        except ValueError:
                print ("error")
                continue

    if ingresar_estudiantes :
        float(input("datos: "))
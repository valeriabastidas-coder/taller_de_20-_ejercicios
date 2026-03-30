import csv
import os

# Configuración básica
ARCHIVO = 'usuarios.csv'
CAMPOS = ['id', 'nombre', 'email']

def inicializar_archivo():
    """Crea el archivo con encabezados si no existe."""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()

def crear_registro(datos):
    """Crea (Añade) un nuevo registro al final del archivo."""
    inicializar_archivo()
    with open(ARCHIVO, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
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
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
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
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        for fila in filas:
            if fila['id'] != str(id_buscado):
                writer.writerow(fila)

# --- Ejemplo de Uso ---
crear_registro({'id': '1', 'nombre': 'Ana', 'email': 'ana@example.com'})
crear_registro({'id': '2', 'nombre': 'Luis', 'email': 'luis@example.com'})

print("Registros actuales:", leer_registros())

actualizar_registro('1', {'id': '1', 'nombre': 'Ana Maria', 'email': 'anam@example.com'})
eliminar_registro('2')

print("Registros finales:", leer_registros())
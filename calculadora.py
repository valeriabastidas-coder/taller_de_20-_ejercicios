def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("⚠️ No se puede dividir por cero")
        return None
    return a / b

def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1️⃣  Sumar")
    print("2️⃣  Restar")
    print("3️⃣  Multiplicar")
    print("4️⃣  Dividir")
    print("5️⃣  Salir")
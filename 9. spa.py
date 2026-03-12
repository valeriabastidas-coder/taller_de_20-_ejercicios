servicio = input("Servicio (masaje, facial, manicure): ")

if servicio in ["masaje","facial", "manicure"]:
    print("Servicio disponible")
else:
    print("Servicio no existe")
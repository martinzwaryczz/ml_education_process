# Determinar si una cadena es vacía (función esVacia)
# Es interesante porque si la cadena solo contiene espacios la longitud será mayor a 0 y la tomará como no vacia, para esto usarémos la función .strip()

def es_vacia(cadena) -> str:
    return f"La cadena es vacia" if len(cadena.strip()) == 0 else f"La cadena {cadena} no es vacia"

cadena_vacia = " "
print(es_vacia(cadena_vacia))
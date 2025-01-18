# Dada una lista de nombres, utiliza una función lambda para crear un diccionario donde cada nombre sea una clave y su longitud sea el valor.

lista_nombres = ["Martin", "Diego", "Alejandro", "Daniel", "Juan"]

diccionario_nombres_long = dict(map(lambda nombre: (nombre, len(nombre)), lista_nombres))

print(diccionario_nombres_long)
# Crea una lista de palabras y utiliza map() junto con una función lambda para crear una nueva lista que contenga la longitud de cada palabra.

lista_palabras = ["palabra","otra","python","machine","cabeza"]

lista_longitud_palabras = list(map(lambda x: len(x), lista_palabras))

print(lista_longitud_palabras) # 7, 4, 6, 7, 6
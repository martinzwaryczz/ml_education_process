# Crea una lista de tuplas donde cada tupla contenga un nombre y una edad. Utiliza una función lambda como clave para ordenar la lista por edad.

lista_nom_edad = [("Martin", 21),("Benjamin", 25),("Carlos", 18)]

orden = lambda lista : sorted(lista, key=lambda x: x[1])

lista_ordenada = orden(lista_nom_edad)

print(lista_ordenada)
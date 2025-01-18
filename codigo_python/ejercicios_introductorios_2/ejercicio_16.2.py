# Dada una lista de palabras, utiliza filter() con una función lambda para crear una nueva lista que contenga solo las palabras que tienen más de 4 letras.

lista_palabras = ["palabra","pala","sueño","tren","dinero","pobreza","oso","octagono"]

lista_mas_cuatro = list(filter(lambda x: len(x) > 4, lista_palabras))

print(lista_mas_cuatro) # ['palabra', 'sueño', 'dinero', 'pobreza', 'octagono']

# Dada una lista, crea una nueva lista que contenga los mismos elementos pero en orden inverso.
# Ojo, orden inverso literalmente, es decir: el primer elemento será el último y así
# Preferiblemente hacerla por comprensión

lista_valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_inversa = [lista_valores[i] for i in range(len(lista_valores) -1, -1, -1)]

print(lista_inversa)
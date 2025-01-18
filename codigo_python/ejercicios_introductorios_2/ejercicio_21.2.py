# Dada la lista numeros, crea una nueva lista llamada pares que contenga solo los números pares.
# Por comprensión

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = [numero_par for numero_par in lista_numeros if numero_par%2 == 0]
print(lista_pares)
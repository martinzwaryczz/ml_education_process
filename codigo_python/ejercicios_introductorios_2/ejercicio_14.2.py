# Dada una lista de números, utiliza map() y una función lambda para crear una nueva lista que contenga el doble de cada número.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

doble_numero = list(map(lambda x: x * 2, numeros))

print(doble_numero)
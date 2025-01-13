# Escribir una función que reciba dos arreglos a1 y a2, de enteros ordenados de menor a mayor e intercale los elementos de los arreglos que recibe en un nuevo arreglo, tal que el arreglo resultante también esté ordenado. Por ejemplo:
# a1 = [-5, 0, 0, 1, 5]
# a2 = [-10, 0, 7]
# resultado = [-10, -5, 0, 0, 0, 1, 5, 7]

def arreglos_ordenados(a1, a2):
    return sorted(a1 + a2)

a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]

print(f"{arreglos_ordenados(a1, a2)}")
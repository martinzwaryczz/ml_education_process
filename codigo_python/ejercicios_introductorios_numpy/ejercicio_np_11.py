# Hacer una función que nos permita verificar si dos matrices pueden multiplicarse
# No controlaré si entran matrices, solo usaré los valores del shape correspondientes y listo

import numpy as np

def es_multiplicable(matriz_uno, matriz_dos) -> bool: # Se puede hacer str y bla bla bla pero no es lo que estoy evaluando ahora
    return matriz_uno.shape[1] == matriz_dos.shape[0] 

# Variante de igual manera

def es_multiplicable_bonito(matriz_uno, matriz_dos) -> str:
    return "Es multiplicable" if matriz_uno.shape[1] == matriz_dos.shape[0] else "No es multiplicable"

# Set de datos de prueba:

matriz1 = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
matriz2 = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2
matriz3 = np.array([[1, 2], [3, 4]])  # 2x2

print(es_multiplicable(matriz1, matriz2)) # True
print(es_multiplicable(matriz2, matriz1)) # True
print(es_multiplicable(matriz1, matriz3)) # False
print(es_multiplicable(matriz3, matriz2)) # False

print(es_multiplicable_bonito(matriz1, matriz2)) # True bonito
print(es_multiplicable_bonito(matriz2, matriz1)) # True bonito
print(es_multiplicable_bonito(matriz1, matriz3)) # False bonito



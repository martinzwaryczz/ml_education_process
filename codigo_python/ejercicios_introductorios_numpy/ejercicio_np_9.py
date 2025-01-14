# Hacer una función que nos permita saber si dos matrices pueden sumarse

import numpy as np

def pueden_sumarse(matriz_uno, matriz_dos) -> bool:
    return matriz_uno.shape == matriz_dos.shape

matriz_uno = np.array([[1, 2, 3],[4, 5, 6]])
matriz_dos= np.array([[7, 8, 9], [10, 11, 12]])
matriz_tres = np.array([8,9])

print(pueden_sumarse(matriz_uno, matriz_dos)) # True
print(pueden_sumarse(matriz_uno, matriz_tres)) # False

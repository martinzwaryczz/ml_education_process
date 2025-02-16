# Dada una matriz retornar el cuadrado de esta.

import numpy as np

def matriz_cuadrada(matriz):
    if matriz.shape[0] != matriz.shape[1]:
        raise ValueError("No se puede realizar el cuadrado de una matriz no cuadrada")
    
    return np.dot(matriz, matriz)

matriz = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

print(matriz_cuadrada(matriz))
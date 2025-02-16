# Dada una matriz indicar su determinante.

import numpy as np

def determinante_matriz(matriz):
    return np.linalg.det(matriz)

matriz = np.array([[10, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(round(determinante_matriz(matriz)))
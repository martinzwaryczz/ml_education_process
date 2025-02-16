# Dada una matriz retornar su traspuesta.

import numpy as np

def matriz_traspuesta(matriz):
    return matriz.T

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matriz_traspuesta(matriz))
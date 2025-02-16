# Dada una matriz pasada por parametro a la función orden_matricial(matriz) indicar el order de la matriz en cuestión.

import numpy as np

def rango_matriz(matriz) -> str:
    return f"La matriz es de orden {matriz.shape[0]} x {matriz.shape[1]}"


matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

matriz2 = np.array([[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]])

print(rango_matriz(matriz))
print(rango_matriz(matriz2))
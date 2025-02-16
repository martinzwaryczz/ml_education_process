# Dada una matriz y la función exponente_matricial(matriz, exponente) elevar la función al exponente.

import numpy as np

def exponente_matricial(matriz, exponente):
    if matriz.shape[0] != matriz.shape[1]:
        raise ValueError("No se puede aplicar potencia a una matriz no cuadrada")
    elif exponente < 0:
        raise ValueError("El exponente debe ser mayor a 0")
    
    return np.linalg.matrix_power(matriz, exponente)

matriz = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

print(exponente_matricial(matriz, 3))
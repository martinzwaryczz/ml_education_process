# Dada una matriz retornar su inversa.

import numpy as np

def matriz_inversa(matriz):

    # Para poder realizar una inversa podrémos valernos también de numpy, pero debemos saber que la matriz si o si deberá ser cuadrada y su determinante debe ser diferente de 0
    if matriz.shape[0] != matriz.shape[1]:
        raise ValueError("Si la matriz no es cuadrada no tendrá inversa.")
    elif np.linalg.det(matriz) == 0:
        raise ValueError("La matriz tiene como determinante 0, no tiene inversa")
    else:
        return np.linalg.inv(matriz)
    
matriz = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

print(matriz_inversa(matriz))
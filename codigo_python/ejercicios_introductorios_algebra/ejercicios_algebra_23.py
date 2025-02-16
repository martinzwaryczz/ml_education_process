# Dada una función auto_valores_y_auto_vec(matriz) calcular los autovalores y autovectores de la matriz pasada como parametro.

import numpy as np

def autovalores_y_autovec(matriz):
    return np.linalg.eig(matriz)

matriz = np.array([[-2, -2],
                   [-5, 1]])

print(autovalores_y_autovec(matriz)) # Ver cómo puedo imprimir mejor esto, quedo horrible
# Utilizando la función anterior establecer si la matriz es o no diagonalizable, en caso de que lo sea diagonalizar y mostrar la misma por consola.

import numpy as np

def autovalores_y_autovec(matriz):
    autovalores, autovectores = np.linalg.eig(matriz)
    return autovalores, autovectores

# Una matriz es diagonalizable si el número de autovalores es igual a la dimensión de la matriz, EL NÚMERO DE VALORES, es decir: SIN REPETICIÓN

def es_diagonalizable(matriz):
    autovalores, autovectores = autovalores_y_autovec(matriz)

    num_unicos = len(set(autovalores))
    dim_matriz = matriz.shape[0]

    if num_unicos == dim_matriz:
        
        matriz_diagonal = np.diag(autovalores)
        return f"Matriz diagonal {matriz_diagonal}, \n autovalores {autovalores}"
    else:
        return f"No es diagonalizable"
    

matriz = np.array([[-2, -2],
                   [-5, 1]])

matriz2 = np.array([[2, 1],
                   [1, 2]])

print(es_diagonalizable(matriz))

print(es_diagonalizable(matriz2))


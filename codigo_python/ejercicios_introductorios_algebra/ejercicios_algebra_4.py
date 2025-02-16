# Dadas dos matrices retornar el producto de estas, recordar que el producto matricial no es conmutativo, 
# confimar si es posible realizar dicho producto, de ser necesario utilizar implemetaciones de código anteriormente hechas.

import numpy as np

def multiplicacion_de_matrices(matriz_A, matriz_B):
    
    # Recordemos que para que una matriz sea multiplicable por otra la matriz la matriz A debe tener la misma cantidad de filas que B en columnas, retornando así una matriz de A columnas por B filas 
    # siendo la operación a seguir AxB=C

    cant_filas_A = matriz_A.shape[0]
    cant_cols_B = matriz_B.shape[1]

    if cant_filas_A != cant_cols_B:
        raise ValueError("Las filas deben ser iguales a las columnas")
    
    return np.dot(matriz_A, matriz_B) # No podrémos usar return matriz_A * matriz_B, nos dará error. 

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 9, 0]])

matriz2 = np.array([[2, 3, 8, 10],
                  [1, 2, 3, 11],
                  [4, 1, 0, 5]])

print(multiplicacion_de_matrices(matriz, matriz2))
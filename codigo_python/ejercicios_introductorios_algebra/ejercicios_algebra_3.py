# Dadas dos matrices retornar la suma de estas.
import numpy as np

def suma_matrices(matriz_uno, matriz_dos):
    return matriz_uno + matriz_dos

matriz_a = np.array([[1, 2, 3],
                     [4, 5, 6]])

matriz_b = np.array([[7, 8, 9],
                     [1, 2, 3]])

print(suma_matrices(matriz_a, matriz_b))
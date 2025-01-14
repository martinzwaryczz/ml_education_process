# Crear dos matrices de 3x3 y 3x2 y multiplicarlas.
import numpy as np

matriz_uno = np.random.randint(1, 11, size=(3,3))
matriz_dos = np.random.randint(1, 11, size=(3,2))

def mul_matrices(matriz_uno, matriz_dos):
    return np.dot(matriz_uno, matriz_dos)

print(f"La multiplicación de las matrices {matriz_uno} y la {matriz_dos} es {mul_matrices(matriz_uno, matriz_dos)}")
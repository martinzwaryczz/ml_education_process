# Encontrar los autovalores de una matriz.
import numpy as np

matriz = np.array([[4, -2, 1],
                   [40, 5, 1],
                   [8, 10, 0]])

auto_valores, auto_vectores = np.linalg.eig(matriz)

print(f"Los autovalores de la matriz son {auto_valores} y los autovectores son {auto_vectores}")
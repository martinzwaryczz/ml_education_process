# Multiplicar un escalar por una matriz.
import numpy as np

escalar = 10
matriz = np.array([[1,2,3],
                   [6,7,8],
                   [0, 1, 2]])

producto = escalar * matriz # Recordar que no es conmutativa, lo mismo pasa con el vector

print(f"El producto de {escalar} por la matriz en cuestión es de: {producto}")
# Crear una matriz 3x3 con valores de 0 a 8
import numpy as np

valores = np.arange(9)

matriz = valores.reshape(3, 3)

print(matriz)
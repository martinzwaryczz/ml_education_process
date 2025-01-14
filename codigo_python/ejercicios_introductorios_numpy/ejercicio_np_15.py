# Crear una matriz de 3x3, acceder a los índices marcados por la función acceder_a(matriz, i, j).
import numpy as np

def acceder_a(matriz, i, j):
    return matriz[i-1][j-1] # Ojo que en las matrices también el índice empieza con 0, es curioso

matriz = [[1, 2],
          [2, 3]]

print(f"El indice matriz sub 11 es: {acceder_a(matriz, 1, 1)}")
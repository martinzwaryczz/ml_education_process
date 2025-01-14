# Crear una matriz de 3x3, calcular su traspuesta, determinante e inversa
import numpy as np

matriz_tresxtres = np.array([[1,2,3],
                            [4,2,1],
                            [5,6,7]])

# Traspuesta:

traspuesta = matriz_tresxtres.T
print(f"La traspuesta es: {traspuesta}")

# Determinante

determinante = np.linalg.det(matriz_tresxtres)
print(f"El determinante es: {round(determinante)}")

# Inversa

if determinante !=0:
    inversa = np.linalg.inv(matriz_tresxtres)

print(f"La inversa es: {inversa}")
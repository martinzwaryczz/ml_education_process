# Crear dos matrices de 3x3 y sumar estas
import numpy as np

matriz_uno = np.random.randint(1, 11, size=(3,3))
matriz_dos = np.random.randint(1, 11, size=(3,3))

matriz_sumada = matriz_uno + matriz_dos

print(f"La suma de las matrices {matriz_uno} y {matriz_dos} es {matriz_sumada}")

# Llevandolo a una función:
# El problema que encuentro cuando llevo las matrices a una función es la falta de control sobre si se pasan como parametros matrices o cualquier
# otra cosa :(



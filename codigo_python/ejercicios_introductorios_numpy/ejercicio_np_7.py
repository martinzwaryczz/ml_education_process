# Crear una matriz con valores aleatorios de 3x3x3
# Esto es lo más parecido a un tensor visto hasta el momento

import numpy as np

matriz_tres_por_tres_por_tres = np.random.randint(1, 11, size=(3, 3, 3))

print(f"La matriz de 3x3x3 es: \n: {matriz_tres_por_tres_por_tres}")
# Dado un sistema de ecuación pasado por función junto a un conjunto de soluciones indicar cuáles son y cuáles no,
#  estos últimos podrán ser indefinidos, es decir: solucion_de(sistema, soluciones*).

import numpy as np

def solucion_de(sistema, *soluciones) -> None:
    A = sistema[:, :-1]
    B = sistema[:, -1]
    
    for sol in soluciones:
        if np.allclose(np.dot(A, sol), B):
            print(f"Solución: {sol}, Estado: Es solución")
        else:
            print(f"Solución: {sol}, Estado: No es solución")

# Nuevo sistema de ejemplo
sistema = np.array([[1, 2, 3, 14],
                    [2, 4, 6, 28],
                    [1, -1, 0, -1]])

# Llamada a la función con soluciones indefinidas
solucion_de(sistema,
            np.array([1, 2, 3]),  # Debería ser solución
            np.array([0, 0, 0]),  # No es solución
            np.array([1, 1, 1]),  # No es solución
            np.array([3, 0, 0]))  # Puede ser solución o no

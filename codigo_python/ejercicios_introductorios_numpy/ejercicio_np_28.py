# Hacer una función que lance un dado lanzar_dado.
import numpy as np

def lanzar_dado() -> str:
    return f"Lanzo un dado {np.random.randint(1, 7)}"

print(lanzar_dado())


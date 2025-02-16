# Calcular el versor asociado a un vector pasado por la función versor_asociado_a(vector).

import numpy as np

def  vector_asociado_a(vector):
    vector_np = np.array(vector)

    modulo = np.linalg.norm(vector_np)

    versor = vector_np / modulo

    return versor

print(vector_asociado_a([3, 4]))
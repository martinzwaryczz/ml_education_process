# Crear un vector con numpy y devolver otro con los elementos pares de este.
import numpy as np

mi_vector =np.array([0,1, 2, 3, 4, 5, 60, 6, 7, 8, 9, 90, 100])

mi_vector_par = mi_vector[mi_vector % 2 == 0]

print(f"El vector original es el siguiente: {mi_vector}, el filtrado solo con numeros pares es {mi_vector_par}")
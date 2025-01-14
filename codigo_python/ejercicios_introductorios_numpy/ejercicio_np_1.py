# En Python no existen los array como tal, existen las listas
# Sin embargo, numpy nos proporciona la posibilidad de crear vectores

# Crear un vector con numpy y mostrar:
#             - Como sumar vectores
#             - Como restar vectores
#             - Como multiplicar vectores
#             - Como dividir vectores
#             - Como acceder a su modulo, es decir: la raíz cuadrada de la sumatoria de sus elementos al cuadrado

import numpy as np

mi_array = np.array([1, 2, 3])
mi_array2 = np.array([4, 5, 6])
print(f"Nuestro array 1 es {mi_array} y nuestro array 2 es {mi_array2}")

# Operaciones básicas con vectores
# Suma
suma_vectores = mi_array + mi_array2
print(f"La suma de los elementos de igual cantidad de elementos es de {suma_vectores}")

# Resta
resta_vectores = mi_array - mi_array2
print(f"La resta de los vectores es {resta_vectores}")

# Multiplicación
multiplicacion_vectores = mi_array * mi_array2
print(f"La multiplicación de dos vectores es {multiplicacion_vectores}")

# Division
division_vectores = mi_array / mi_array2
print(f"La división de dos vectores es {division_vectores}")

# Si queremos hacer otro vector pero este con una cantidad de elementos diferente tendrémos un ValueError

# Si queremos multiplicar un escalar por un vector - cosa que solo es posible en ese orden - podrémos:
producto_punto = np.dot(2, mi_array2)
print(f"Producto escalar de 2 y {mi_array2}")
print(f"Producto escalar {producto_punto}")

# Magnitud de un vector, raiz cuadrada de la suma de sus elementos al cuadrado

norma = np.linalg.norm(mi_array2)
print(f"Norma del vector {mi_array2}: ", norma)
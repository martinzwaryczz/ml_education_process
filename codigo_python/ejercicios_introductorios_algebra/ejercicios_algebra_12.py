# Clasificar un sistema de ecuaciones por función con clasificar_sistema(sistema) con el teorema de Rouché-Fröbenius.

# Si el rango de nuestra matriz de coeficientes es igual al de la matriz de coeficientes con su vector de soluciones 
# y a la cantidad de incognitas el sistema será compatible determinado

# Si el rango de nuestra matriz de coeficientes es igual al de la matriz de coeficientes con su vector de soluciones 
# y la cantidad de incognitas es mayor será compatible indepeterminado

# Sí el rango de nuestra matriz de coeficientes es diferente al de la matriz de coeficientes con su vector de soluciones es incompatible. 

import numpy as np

def clasificar_sistema(sistema):
    A = sistema[:, :-1]
    B = sistema

    rango_A = np.linalg.matrix_rank(A)
    rango_B = np.linalg.matrix_rank(B) # En realidad esto esta mal, debemos utilizar colum stack si verdaderamente estamos evaluando la matriz con su correspondiente vector
    # rango_B = np.linalg.matrix_rank(np.column_stack((A, B)))

    if rango_A == rango_B and rango_A == A.shape[1]:
        print("El sistema es compatible determinado")
    elif rango_A == rango_B and rango_A < A.shape[1]:
        print("El sistema es compatible indeterminado")
    else:
        print("El sistema es incompatible")

# Sistemas de ejemplo
sistema1 = np.array([[1, 2, 1, 6],
                      [2, 3, 1, 8],
                      [3, 1, 2, 11]])

sistema2 = np.array([[1, 2, 1, 6],
                      [2, 4, 2, 12],
                      [3, 6, 3, 18]])

sistema3 = np.array([[1, 2, 1, 6],
                      [2, 4, 2, 12],
                      [1, 2, 1, 8]])

# Clasificación de los sistemas
print("Sistema 1:")
clasificar_sistema(sistema1)

print("\nSistema 2:")
clasificar_sistema(sistema2)

print("\nSistema 3:")
clasificar_sistema(sistema3)
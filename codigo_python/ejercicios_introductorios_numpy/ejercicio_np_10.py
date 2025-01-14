# Hacer una función para sumar matrices que controle que se sumen matrices, mas no otra estructura
# Se tendrá en cuenta que las matrices son del mismo orden, aún así podrémos usar la misma función del ejercicio 9 para controlar esto
import numpy as np

def sumar_matrices(matriz_uno, matriz_dos) -> bool:
    if not isinstance(matriz_uno, np.ndarray) or not isinstance(matriz_dos, np.ndarray):
        raise ValueError("Se deben ingresar matrices, no otro valor")
    if not pueden_sumarse(matriz_uno, matriz_dos): # Ojo con asignar False siempre
        raise ValueError("Las matrices deben tener el mismo orden")
    else:
        return matriz_uno + matriz_dos


def pueden_sumarse(matriz_uno, matriz_dos) -> bool:
    return matriz_uno.shape == matriz_dos.shape    



matriz_uno = np.array([[1, 2, 3],[4, 5, 6]])
matriz_dos= np.array([[7, 8, 9],[10, 11, 12]])



print(f"La suma de las matrices {matriz_uno} y {matriz_dos} es: \n\n {sumar_matrices(matriz_uno, matriz_dos)}")
# print(pueden_sumarse(matriz_uno, matriz_dos))
# Dada una matriz de orden nxm indicar por parametro en la función elemento_matricial(matriz, elemento), siendo el elemento el índice de esta, en caso de que no exista lanzar un ValueError().
import numpy as np

def elemento_matriz(matriz, elemento) -> str:
    if elemento <= 0 or len(str(elemento)) != 2:
        raise ValueError("Índice incorrecto.")
    
    fila = (elemento // 10) - 1
    columna = (elemento % 10) - 1

    max_fila = matriz.shape[0]
    max_col = matriz.shape[1] 

    # print(max_fila, max_col)

    if fila > max_fila or columna > max_col or fila <= 0 or columna <= 0:
        raise ValueError(f"Indices fuera de rango") 



    return f"El elemento {elemento} tiene como valor {matriz[fila, columna]}"


matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(elemento_matriz(matriz, 11)) # 1
print(elemento_matriz(matriz, 32)) # 2

print(elemento_matriz(matriz, 33)) # 9
# print(elemento_matriz(matriz, 44)) # Índice fuera de rango

print(elemento_matriz(matriz, 31)) # 9
print(elemento_matriz(30))
# Escribir una función que reciba dos matrices de NxN y devuelva la suma de las mismas. Podemos considerar que las matrices se representan como un arreglo bidimensional
# Con numpy no tenemos que hacer nada de este laburo super infumable, pero bueno no esta demás para ejercitar la lógica

def suma_matrices(m1, m2):
    filas = len(m1)
    columna = len(m1[0])
    matriz_suma = [[0 for _ in range(columna)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columna):
            matriz_suma[i][j] = m1[i][j] + m2[i][j]
    
    return matriz_suma

matriz_uno = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_dos = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(f"La suma de las matrices es f{suma_matrices(matriz_uno, matriz_dos)}")

# Hacer coincidir los índices, sumar elemento por elemento y esto llevarlo a una nueva matriz es infumable, aguante numpy
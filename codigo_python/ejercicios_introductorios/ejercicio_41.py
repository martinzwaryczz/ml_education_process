# Implementar la función: **busquedaSecuencial(int [] arreglo, int valorBuscado)** que recibe un arreglo de enteros y un valor a buscar,
#  y devuelve la posición del valor buscado, o -1 si el valor no se encuentra

def busqueda_secuencial(arreglo, valor_buscado):
    for i in range(len(arreglo)):
        if arreglo[i] == valor_buscado:
            return i
        else:
            return -1

arreglo = [1,2,3,4]
print(busqueda_secuencial(arreglo, 1))
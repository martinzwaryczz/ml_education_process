# Escribir una función que reciba un arreglo de enteros y devuelva true si el arreglo está ordenado de mayor a menor y false si está desordenado

def arreglo_ordenado(arreglo):
    return f"El arreglo {arreglo} esta ordenado de mayor a menor" if sorted(arreglo, reverse=True) == arreglo else "el arreglo no esta ordenado de mayor a menor"

arreglo1 = [3, 2, 1]
arreglo0 = [6, 1, 12000, 10]

print(arreglo_ordenado(arreglo1))
print(arreglo_ordenado(arreglo0))
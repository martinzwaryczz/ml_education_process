# Escribir una función que imprima por compresión todos los valores impares del 0 al 100.

def valores_impares_por_compresion() -> list:
    return [i for i in range(0, 101) if i%2 != 0]

print(valores_impares_por_compresion())
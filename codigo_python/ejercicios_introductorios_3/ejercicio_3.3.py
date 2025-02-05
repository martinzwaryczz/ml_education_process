# Escriba una función que escriba los números de la secuencia de fibanacci desde 0 a un atributo pasado como parametro.

def fibonacci(n) -> list:
    sec_fibonacci = []
    a, b = 0, 1

    for _ in range(n):
        sec_fibonacci.append(a)
        a, b = b, a + b
    
    return sec_fibonacci

print(fibonacci(10))
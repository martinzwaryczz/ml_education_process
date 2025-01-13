# Se ingresa un valor numérico por consola, determinar e informar si se trata de un número primo o no
# Los números primos son aquellos que sólo son divisibles por uno y por sí mismos
# El código fue sacado del ellibrodepython.com, no lo hice yo :P

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
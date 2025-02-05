# Escribir una función que calcule el factorial de un número.

def factorial(n):
    if n < 0:
        raise ValueError("Los numeros negativos no tienen factorial")
    elif n==0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(0)) # 1
print(factorial(2)) # 2
print(factorial(4)) # 24
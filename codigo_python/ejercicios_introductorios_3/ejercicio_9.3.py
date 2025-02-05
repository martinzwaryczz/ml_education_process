# Escribir una función que reciba un número y diga si el mismo es palindromo, tener en cuenta el signo.

def numero_palindromo(numero) -> bool:
    numero = str(numero)
    numero_inverso = numero[::-1]
    return numero == numero_inverso

print(numero_palindromo(121))
print(numero_palindromo(-121))
print(numero_palindromo(12321))
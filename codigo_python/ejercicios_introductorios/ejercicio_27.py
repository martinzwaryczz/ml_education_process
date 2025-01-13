# Escribir una función que reciba un string y lo devuelva invertido. Por ejemplo: invertirCadena("Hola"),retorna "aloH".
#  Reutilice la función implementada para decir si una palabra es o no, un palíndromo. **esPalindromo("neuquen")** devuelve true

def invertir(a):
    b = ""
    for i in range(0, len(a), 1): # range(start, stop, step)
        b = a[i] + b
    return b

def es_palindromo(a):
    return a == invertir(a)

print(es_palindromo("neuquen")) # True
print(es_palindromo("no es")) # False
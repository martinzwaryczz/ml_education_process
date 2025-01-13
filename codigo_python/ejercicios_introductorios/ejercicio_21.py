# Determinar si un carácter es una letra mayúscula o minúscula (**función esMayuscula(char c) y esMinuscula(char c)**)

def es_mayuscula(c):
    return c.isupper()

def es_minuscula(c):
    return c.islower()

caracter_mayus = 'B'
caracter_min = 'b'

print(es_mayuscula(caracter_mayus)) # True
print(es_minuscula(caracter_min)) # True

# Determinar si un carácter es un dígito numérico (**función esDigito(char c)**)

def es_digito(c):
    return c.isdigit()

caracter = '5'
caracterFalso = 'tu vieja'

if es_digito(caracter):
    print(f"{caracter} es digito.")
else:
    print(f"{caracter} no es digito.")

print(es_digito(caracterFalso)) # False, no tengo ganas de hacer el if
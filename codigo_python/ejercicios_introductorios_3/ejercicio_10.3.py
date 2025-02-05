# Escribir una función que reciba una frase y devuelva la longitud de la ultima palabra.

def longitud_ultima_palabra(cadena) -> int:
    cadena = cadena.strip()
    cadena = cadena.split(" ")
    return len(cadena[-1])

print(longitud_ultima_palabra("Hola mundo")) # 5
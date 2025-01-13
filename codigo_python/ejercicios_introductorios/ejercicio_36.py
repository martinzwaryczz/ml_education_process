# Escribir una función consonantes que recibe una cadena de caracteres y devuelve la cadena que resulta 
# de eliminar todas las vocales de la cadena recibida. Por ejemplo: **consonantes("hola como estas");** // devuelve "hl cm sts"

def eliminar_vocales(cadena):
    vocales = ("a", "e", "i", "o", "u")
    cadena_sin_vocales = ""
    cadena = str(cadena)
    for caracter in cadena:
        if caracter not in vocales:
            cadena_sin_vocales += caracter
    
    return cadena_sin_vocales

print(eliminar_vocales("hola como estas"))
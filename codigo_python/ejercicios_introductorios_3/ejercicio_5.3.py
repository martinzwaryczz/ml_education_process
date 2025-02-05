# Escribir una función que tenga reciba dos cadenas y diga si la primera esta contenida en la segunda sin usar una función que lo haga directamente.

def cadena_en(cadena1, cadena2) -> bool:
    longitud_uno = len(cadena1)
    longitud_dos = len(cadena2)

    if longitud_uno > longitud_dos:
        return False
    
    for i in range(longitud_dos - longitud_uno + 1):
        for j in range(longitud_uno):
            if cadena2[i + j] != cadena1[j]:
                break
        else:
            return True  

    return False  

print(cadena_en("Hola", "Hola como estas")) # True
print(cadena_en("asdad", "Palabra")) # False


# Escribir una función que reciba como parametro dos palabras y retorne o no si son anagramas.

def son_anagramas(cadena1, cadena2) -> str:
    if len(cadena1) != len(cadena2):
        return "Las longitudes de las palabras son diferentes, es imposible que sean anagramas"
    else:
        if set(cadena1.lower()) == set(cadena2.lower()):
            return "Las palabras son anagramas"
        else:
            return "Las palabras no son anagramas"

print(son_anagramas("roma", "amor"))
print(son_anagramas("roma", "aaaa"))
print(son_anagramas("Valora", "Alvaro"))
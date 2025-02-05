# El mismo ejercicio se puede simplificar una bararidad haciendolo por compresión

def cuantasVocales(palabra) -> str:
    vocales = ("a", "e", "i", "o", "u")
    contador_vocales = sum(1 for c in palabra if c in vocales)

    return f"La palabra {palabra} tiene {contador_vocales} vocales."

print(cuantasVocales("casa")) # 2
print(cuantasVocales("palabra")) # 3
print(cuantasVocales("aeiou")) # 5

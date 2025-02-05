# Escriba una función que cuente cuantas palabras hay en una palabra o frase.

def cuantasVocales(palabra) -> str:
    vocales = ("a", "e", "i", "o", "u")
    contador_vocales = 0
    for c in palabra:
        if c in vocales:
            contador_vocales+=1
    
    return f"En la palabra {palabra} hay {contador_vocales} vocales."

print(cuantasVocales("casa")) # 2
print(cuantasVocales("palabra")) # 3
print(cuantasVocales("aeiou")) # 5


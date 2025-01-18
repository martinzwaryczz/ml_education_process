# Crea un diccionario que cuente la frecuencia de las letras en la palabra "programacion". Imprime el diccionario resultante.

palabra = "programacion"

dic_frecuencias = {}

for letra in palabra:
    if letra in dic_frecuencias:
        dic_frecuencias[letra] += 1
    else:
        dic_frecuencias[letra] = 1 # Ya agrega automaticamente la clave letra y le asigna un valor


print(dic_frecuencias)

# Variante: función que reciba una string y retorne la frecuencia de las letras en esta

def frecuencias_en_string(string) -> str: # El str es opcional
    dic_func_frecuencias = {}
    for letra in string:
        if letra in dic_func_frecuencias:
            dic_func_frecuencias[letra] +=1
        else:
            dic_func_frecuencias[letra] = 1
    
    return f"La frencuencia de letras en {string} es de {dic_func_frecuencias}"

print(frecuencias_en_string("oso")) # {o:2, s:1}
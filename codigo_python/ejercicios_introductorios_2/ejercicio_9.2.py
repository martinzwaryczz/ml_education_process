# Crea un diccionario que represente una biblioteca, donde cada clave sea un género y el valor sea otro diccionario con títulos de libros y sus autores.

dic_biblioteca = {
    "terror": {
        "titulo":"IT",
        "autor":"Stephen King"
    },
    "ficcion":{
        "titulo":"Cien años de soledad",
        "autor":"Garcia Marquez"
    },
    "divulgacion cientifica":{
        "titulo": "De animales a dioses",
        "autor": "Yuan Noah Harari"}
}

print(dic_biblioteca)

# Extra: función que imprime en formato str dicho diccionario

def imprimir_genero_bien(diccionario) -> str:
    generos = ""
    cont_genero = 0
    for genero in diccionario.keys():
        if cont_genero == 0:
             generos += (" " + genero)
             cont_genero += 1
        elif cont_genero == len(diccionario.keys()) -1:
            generos += " y " + genero
        else:
            generos += (", " + genero)
            cont_genero += 1
    return generos # Estaria bueno investigar como escribirlos por color en consola pero no es lo que estoy queriendo mejorar o aprender ahora

def imprimir_dic(diccionario) -> str:
    return f"La biblitoca tiene los generos{imprimir_genero_bien(diccionario)}." # Queda pendiente: imprimir BIEN en formato str los subdiccionarios, de momento no pude

print(imprimir_dic(dic_biblioteca))



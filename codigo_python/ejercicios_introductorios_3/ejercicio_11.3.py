# Escribir una función que reciba una lista y encuentre el prefijo más grande en sus elementos si es que existen.

def prefijo_comun(lista_valores) -> str:
    if not lista_valores:
        return "" # Si la lista esta vacia
    
    prefijo = lista_valores[0]

    for i in lista_valores[1:]:

        while i[:len(prefijo)] != prefijo:

            prefijo = prefijo[:-1]

            if not prefijo:
                return ""
            
    return prefijo

lista1 = ["perro", "perrito", "perrera"]
lista2 = ["pajaro", "pajarito", "pajarera"]
lista3 = ["gato", "gatito", "gatería"]

lista4 = ["elefante", "jirafa", "tigre"]
lista5 = ["rojo", "verde", "azul"]

print(prefijo_comun(lista1))
print(prefijo_comun(lista2))
print(prefijo_comun(lista3))
print(prefijo_comun(lista4))
print(prefijo_comun(lista5))
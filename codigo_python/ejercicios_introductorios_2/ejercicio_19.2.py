# Crea una lista de diccionarios donde cada diccionario represente una persona con claves nombre y edad. Usa sorted() junto con una función lambda para ordenar la lista por edad.
# Este se lo re tire a chatgtp, hice la lista de diccionarios nomas 

lista_diccionarios = [{"nombre":"Fulanito", "edad":80},
                      {"nombre":"Martin", "edad":21},
                      {"nombre":"Carlos", "edad":20},
                      {"nombre": "Alejo", "edad":30}]

lista_ordenada = sorted(lista_diccionarios, key=lambda x: x["edad"])

print(f"La lista ordenada por edad es {lista_ordenada}.")


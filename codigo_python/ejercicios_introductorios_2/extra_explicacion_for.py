# Extra con for y sus variantes
# Listas
nombres_lista = ["Juan", "Carlos", "Fulano"]
for nombre in nombres_lista:
    print(nombre)

# Tupla
nombres_tupla = ("Juan", "Carlos", "Fulano")
for nombre in nombres_tupla:
    print(nombre)

# Set
nombres_set = {"Juan", "Ana", "Elena"}
for nombre in nombres_set:
    print(nombre)

# Diccionario
nombres_diccionario = {"Juan": 1, "Ana": 2, "Elena": 3}
for nombre in nombres_diccionario:
    print(nombre)

# Range
for i in range(0, 11):
    print(i)

# En una cadena
for x in "cadena":
    print(x)

# Inversa
cadena = "cadena"
for i in range(len(cadena) - 1, -1, -1):
    print(i)

# Compresión
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = [numero_par for numero_par in lista_numeros if numero_par%2 == 0]
print(lista_pares)

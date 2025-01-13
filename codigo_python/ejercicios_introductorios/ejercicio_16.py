# Determinar el menor valor de un conjunto de números e indicar también su posición relativa dentro del mismo. El ingreso de datos finaliza con la llegada de un cero
# Al hablar de un conjunto de números podemos hablar de valores no repetidos.
# Este primer código esta mal, los conjuntos no tienen un indice como tal, son solo valores. 

# numeros = set()

# while True:
#     num = int(input("Ingrese un numero: "))
#     if num == 0:
#         break
#     numeros.add(num)

# print(f"El menor numero ingresado es: {min(numeros)}")
# print(f"El conjunto es {numeros}")

# Como no entiendo actualmente como se ordenan los valores en un conjunto usaré una lista que no pueda contener valores duplicados.

lista_numeros = []

while True:
    val = int(input("Ingrese un numero: "))
    if val == 0:
        break
    elif lista_numeros.__contains__(val):
        pass
    else:
        lista_numeros.append(val)

print(f"La lista es: {lista_numeros}")
print(f"El número más chico es {min(lista_numeros)} y su posición relativa dentro del mismo es {lista_numeros.index(min(lista_numeros))}") # Dice una menos porque contempla el 0

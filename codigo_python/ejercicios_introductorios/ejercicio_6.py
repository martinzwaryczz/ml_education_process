#  Leer tres valores numéricos enteros, indicar cual es el mayor, cuál es el del medio y cuál el menor. 
# Considerar que los tres valores son diferentes, no agregaré un control para saber si esto ocurre o no, no es lo que busco aprender ahora

val1 = int(input("Ingrese un valor: "))
val2 = int(input("Ingrese otro valor: "))
val3 = int(input("Ingrese un ultimo valor: "))
print("\n")

# Variante 1: la más infumable, hacer todas las comparaciones posibles n^2 posibles comparaciones, no la voy a hacer no saco nada haciendo tantos elif

# Variante 2:

listaVal = [val1, val2, val3]
listaVal = sorted(listaVal, reverse=True)
print(f"El valor más grande es {val1}, el del medio es {val2}, el más chico es {val3}")

# Variante 3: lo mismo pero en una función, el vector ya esta ordenado de mayor a menor, igual no hace falta revertirlo=true, de utlima se cambian los índices, es más
# una cuestión de prolijidad que otra cosa

def numMayorMedioChicoPorLista(listaVal) -> str:
    return f"El valor más grande es {val1}, el del medio es {val2}, el más chico es {val3} por función"

print(numMayorMedioChicoPorLista(listaVal))
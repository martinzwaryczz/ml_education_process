#  Leer dos valores numéricos enteros e indicar cual es el mayor y cual es el menor. Considerar que ambos valores son diferentes

val1 = int(input("Ingrese un numero: "))
val2 = int(input("Ingrese otro numero: "))

# Variante 1:

if val1 < val2:
    print(f"El numero {val1} es menor que el numero {val2}")
else:
    print(f"El numero {val1} es mayor que el numero {val2}")

# Variante 2:
def numMayor(val1, val2):
    return f"El numero {val1} es menor que el numero {val2} por funcion" if val1 < val2 else f"El numero {val1} es mayor que el numero {val2} por funcion"

print(numMayor(val1, val2))

# Variante 3:

lista_val = [val1, val2]

def numMayorPorLista(lista_val):
    lista_val = sorted(lista_val) # Ordena de menor a mayot
    return f"El numero {val1} es menor que el numero {val2} por sorted"

print(numMayorPorLista(lista_val))
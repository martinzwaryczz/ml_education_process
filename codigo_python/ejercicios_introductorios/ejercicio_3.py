# Dado un valor numérico entero, informar si es par o impar

val = int(input("Ingrese un número, se informará si es par o impar: "))

# Variante 1:

if val%2 == 0:
    print("Es par sin funcion")
else:
    print("Es impar sin funcion")

# Variante 2:

def esPar(val):
    if val%2 == 0:
        print("Es par por funcion")
    else:
        print("Es impar por funcion") # Esta variante es buena si requerimos en multiples ocasiones saber si el número es par o impar, pero hay una versión mucho mejor
    

# Variante 3:

def esParV2(val):
    return f"El valor {val} es par V3" if val%2==0 else f"El valor {val} es impar" # Recordar que el return devuelve un valor pero no lo muestra, usar print

esPar(val)
print(esParV2(val))

# Dado un conjunto de valores numéricos indicar cuál es el mayor. El ingreso de datos finaliza con la llegada de un cero

# Variante 1:
valMayor = int(input("Ingrese un número inicial: "))
val = int(input("Ingrese otro valor: "))

while val != 0:
    if val > valMayor:
        valMayor = val
    val = int(input("Ingrese un número: "))  # Debe estar dentro del bucle

print(f"\nEl valor mayor es {valMayor}")

# Variante 2:

valor = int(input("Ingrese un valor"))
lista_valor = [valor]
while valor != 0:
    lista_valor.append(valor)

print(f"El valor más grande es el {lista_valor[-1]}") # También podemos usar lista_valor sort


   


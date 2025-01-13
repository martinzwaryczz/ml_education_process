# Leer dos valores enteros e informar la suma y su cociente

# Variante 1:

val1 = int(input("Ingrese un valor: "))
val2 = int(input("Ingrese otro valor: "))

sum = val1 + val2
cociente = val1 * val2
print(f"La suma de los valores es: {sum}.")
print(f"El cociente es: {cociente}.\n")

# Variante 2:

print(f"La suma calculada en el print es: {val1 + val2}")
print(f"El cociente calculador en el print es: {val1 * val2}")

# Variante 3:

def suma(val1, val2):
    return val1 + val2 # Se puede también guardar la suma en una variable y retornar esta como otra variante, pero a estas alturas ya quedo claro

def cociente(val1, val2):
    return val1 * val2 # Se puede también guardar el cociente en una variable y retornar esta como otra variante, pero a estas alturas ya quedo claro

print(f"La suma por función es: {suma(val1, val2)}.")
print(f"El cociente por función es: {cociente(val1, val2)}.")
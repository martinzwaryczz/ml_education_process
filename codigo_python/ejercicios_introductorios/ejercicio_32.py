# Implementar una función que reciba como parámetro un arreglo de enteros 
# y muestre por pantalla cuántas veces se repite cada uno. 
# El arreglo no está ordenado. Se garantiza que a los sumo habrá 100 números diferentes

# Para generar un vector que genere mas de 100 numeros al azar le pregunte a chatgtp, despues lo pensé yo : )
import random

n = 150
lista_random = []

for i in range(n):
    valor = random.choice(range(1, 21))
    lista_random.append(valor)

def contar_repeticiones(lista_random):
    conteo = {}

    # Contar las repeticiones de cada número
    for numero in lista_random:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1
    
    # Mostrar el resultado
    for numero, cantidad in conteo.items(): # Este for es un dolor de huevos, revisar bien porque funciona de milagro
        print(f"El número {numero} se repite {cantidad} {'veces' if cantidad > 1 else 'vez'}.")

print(contar_repeticiones(lista_random))

# Desarrollar un algoritmo que muestre los primeros n números primos siendo n un valor que debe ingresar el usuarios
# NO ANDA


def es_primo(a):
    i = 2
    while(a > i and i <= a % i != 0):
        i += 1 
    
    return a == 1

def primeros_n_primos(n):
    n = int(input("Ingrese la cantidad n de primos: "))
    contador_de_primos = 0
    i = 2
    while contador_de_primos < n:
        if es_primo(i):
            contador_de_primos += 1
            print(i)
            i+=1

print(primeros_n_primos(10))


    
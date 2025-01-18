# Dada una lista de números, utiliza una función lambda junto con filter() para crear una nueva lista que contenga solo los números pares.

#def filter(lista) -> list:
#    return [num for num in lista if num % 2 == 0] # Tener super presente esto, esta tecnica optimiza una bararidad de código y es super eficiente

#lista_par = lambda lista : filter(lista)

#lista_de_prueba = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lista_lamda = lista_par(lista_de_prueba)

# print(f"La lista filtrada con filter() y lambda es: {lista_lamda}.")

##### En realidad entendi re mal la consigna, lo previo no es que este mal pero es al pedo hacer la función lambda si ya filta filter(), esta es la resolución correcta: #####

# Lista de números:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar filter con una función lambda para obtener los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros)) # Es curioso ver como evitas una funcion practicamente por usar una lambda

# Imprimir la lista de números pares
print(pares)  # Salida: [2, 4, 6, 8, 10]
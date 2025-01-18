# Crea una lista de números y utiliza map() y filter() en combinación con funciones lambda para obtener una lista de los cuadrados de los números impares.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1000, 1001]

# Incialmente salio mal, list hay que usarlo si o si, a fin de cuentas vamos a crear una lista
# list_cuad_imp = filter(map(lambda x: x%2 != 0, lista_numeros**2))

list_cuad_imp = list(map(lambda x: x ** 2, filter(lambda x: x%2 != 0, lista_numeros)))

print(f"La lista es {lista_numeros} y la lista con sus elementos impares al cuadrado es {list_cuad_imp}")


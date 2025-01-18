# Utiliza una comprensión de listas para crear una nueva lista llamada cuadrados que contenga el cuadrado de cada número en la lista numeros.
# El concepto de comprensión es muy interesante

lista_normal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_con_comprension = [numero ** 2 for numero in lista_normal]

print(lista_con_comprension)
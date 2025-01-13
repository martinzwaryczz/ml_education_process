# Dado un conjunto de número enteros mayores o iguales a 0 y menores que 100 determinar e informar cuántas veces aparece cada uno.
#  El conjunto finaliza con la llegada de un valor negativo
# Para esto usaré un diccionario que tendrá como clave el número en cuestión y como valor se sumará 1 a medida que aparezca otra clave igual

# Cargamos la lista
lista_numeros = []

num = int(input("Ingrese un valor: "))
while True:
    if num < 0:
        break
    elif num >= 100:
        raise ValueError("El numero debe ser menor a 100") # No me carga valores mayores o iguales a 100 pero tampoco lanza el error :P
    lista_numeros.append(num)
    num = int(input("Ingrese otro valor: "))

# Creamos el diccionario, acá es mucho más fácil que en Java, aunque suele ser algo confunso:
# Usaré una función por comodidad
def conteo_numeros(lista_numeros):
    mapa_conteo = {}
    for num in lista_numeros:
        if num in mapa_conteo:
            mapa_conteo[num] += 1
        else:
            mapa_conteo[num] = 1
    
    return mapa_conteo

# Imprimir un diccionario en python no es tan fácil igual:
conteo = conteo_numeros(lista_numeros)

for num, cantidad in conteo.items():
    print(f"El numero {num} aparece {cantidad} veces")
        





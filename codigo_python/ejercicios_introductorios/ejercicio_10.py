# Desarrollar una función que muestre por pantalla los primeros n números
#  naturales considerando al 0 (cero) como primer número natural, siendo n un valor que se pasa por parámetro

# Variante 1:

def primeros_n_numeros(n):
    for i in range(0, n+1): # Recordar que excluye el valor dado, por eso si queremos incluir a este debemos sumar un valor
        print(i)  

primeros_n_numeros(100)

# Se debe poder hacer de otra manera con una lista pero no viene al caso

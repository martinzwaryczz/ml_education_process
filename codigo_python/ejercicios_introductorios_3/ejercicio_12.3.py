# Dado una lista con [0, n] elementos del 0 a n siendo estos la susesión de números de 1 en 1 positivos imprimir por pantalla cual es el número faltante, en caso de no haber imprimir -1

def elemento_faltante(num_list):
    # Determino el número máximo en la lista, no el tamaño dado que falta un valor
    n = max(num_list)

    elementos_totales = set(range(n + 1))  
    num_list_set = set(num_list)
    
    elemento_faltante = elementos_totales.difference(num_list_set)

    if elemento_faltante:
        return elemento_faltante  
    else:
        return -1 


print(elemento_faltante([0, 1, 3]))  
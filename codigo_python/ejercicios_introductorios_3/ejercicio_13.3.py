# Dado una lista con valores de cualquier tipo remover los elementos duplicados y devuelver una lista, tratar de no usar set().

def remover_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if lista_sin_duplicados.__contains__(elemento):
            pass
        else:
            lista_sin_duplicados.append(elemento)
    
    return lista_sin_duplicados

print(remover_duplicados([1, 1, 0, 0, 2, 2])) # 1, 0, 2

# Con el set ya que estamos

def remover_duplicados(lista):
    return list(set(lista))

print(remover_duplicados([1, 1, 2, 2, 3, 3, 0])) # 0, 1, 2, 3
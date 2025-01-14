# Crear un vector y mostrar sus funciones de agregación
import numpy as np

mi_array = np.array([1, 2, 3, 4])

# sum()
# Manualmente, un re quilomno:
suma_array = 0
for i in mi_array-1:
    suma_array += mi_array[i]
print(f"La suma de los elementos de mi array es de {suma_array}")

# Con numpy :)
print(f"La suma de los elementos con numpy es de {np.sum(mi_array)}")

# mean()
# Manualmente, reutilizarémos el for anterior:
print(f"El promedio manualmente reutilizando codigo es de {suma_array / len(mi_array)}") # Si bien parece fácil es horrible, encima ni siquiera 
                                                                                         # use una función, tiré el for así nomás, horrible
# Con numpy :)
print(f"El promedio con numpy es de {np.mean(mi_array)}")
                                                                                     
# max()
# Manualmente: no tiene sentido hacerlo, ya lo hice antes y no es lo que estoy buscando aprender ahora
# Con numpy :)
print(f"El maximo valor del array es: {max(mi_array)}")

# min()
# Manualmente: =]
# Con numpy :))
print(f"El minimo valor es {min(mi_array)}")
import numpy as np
import matplotlib.pyplot as plt

def graficar_vector_r2(vector):
    
    # Creamos la gráfica
    fig, ax = plt.subplots()

    # Creamos el vector en R2 con un color random
    color_random = np.random.rand(3,)
    ax.quiver(0,0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color_random)

    # Los ejes "principales" serán más oscuros

    ax.axhline(0, color='black', linewidth=4, ls='-', zorder=0)  # Eje X
    ax.axvline(0, color='black', linewidth=4, ls='-', zorder=0)  # Eje Y

    # Definimos los límites, como será un producto este será de 10 pero el proximo será un poco más grande

    ax.set_xlim(-10, 10) # Lím. eje X
    ax.set_ylim(-10, 10) # Lím. eje Y

    # Ajustar los ticks de los ejes para que vayan de 1 en 1
    plt.xticks(np.arange(-10, 11, 1)) # 11 queda excluido, va de -10 a 10
    plt.yticks(np.arange(-10, 11, 1))

    plt.title('Gráfica de los Vectores en R2')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()
    plt.show()


# Busquemos ahora la forma de hacer un producto escalar * vector

def producto_escalar_r2(escalar, vector):
    vector = np.array(vector)
    nuevo_vector = escalar * vector
    return nuevo_vector

def producto_vector_por_vector(vector, vector2):
    vector = np.array(vector)
    vector2 = np.array(vector2)
    return vector * vector2


# Datos de prueba
vector = [4, 3]
vector2 = [2, 2]

graficar_vector_r2(vector)
vector_por_escalar = producto_escalar_r2(2, vector)
graficar_vector_r2(vector_por_escalar)
vector_por_vector = producto_vector_por_vector(vector, vector2)
graficar_vector_r2(vector_por_vector)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def graficar_vectores(*vectores): # * recibe multiples parametros, no lo tome en cuenta en los ejercicios básicos


    # Crear la gráfica
    fig, ax = plt.subplots()

    # Graficar cada vector con un color aleatorio

    for vector in vectores:
        color = np.random.rand(3,)  # Generar un color aleatorio
        ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color) # Ver quiver en la documentación de matplotlib, es el mejor tipo de gráfico para gráficar vectores

    # Configurar los ejes

    ax.axhline(0, color='black', linewidth=4, ls='-', zorder=0)  # Eje X
    ax.axvline(0, color='black', linewidth=4, ls='-', zorder=0)  # Eje Y



    ax.set_xlim(-10, 10) # Lím. eje X
    ax.set_ylim(-10, 10) # Lím. eje Y
    
    # Ajustar los ticks de los ejes para que vayan de 1 en 1
    plt.xticks(np.arange(-10, 11, 1)) # 11 queda excluido, va de -10 a 10
    plt.yticks(np.arange(-10, 11, 1))

    # Titulo y labels

    plt.title('Gráfica de los Vectores en R2')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()
    plt.show()

    # Datos y pruebas

vector = [4, 3]
vector2 = [-4, 3]
vector3 = [0, 3]

graficar_vectores(vector, vector2, vector3)

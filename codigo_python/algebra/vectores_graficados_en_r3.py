import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # De esto ni idea


def graficar_vectores_3d(*vectores):
    # Creamos el gráfico
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Creamos los vectores:
    for vector in vectores:
        color_vector_random = np.random.rand(3,)
        ax.quiver(0,0,0, vector[0], vector[1], vector[2], color=color_vector_random)

    # Límites de los ejes:
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    # Marcamos los ejes a gusto
    ax.axhline(0, color='black', linewidth=2, ls='-')  # Eje X
    ax.axvline(0, color='black', linewidth=2, ls='-')  # Eje Y
    ax.zaxis.set_tick_params(width=2)  # Eje Z

    # Etiquetas y título
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Gráfica de los Vectores en R3')

    plt.show()

# Datos y pruebas:

vector1 = [4, 3, 2]
vector2 = [-4, 3, 5]
vector3 = [0, 3, -2]
vector4 = [10, 10, 10]

graficar_vectores_3d(vector1, vector2, vector3, vector4)
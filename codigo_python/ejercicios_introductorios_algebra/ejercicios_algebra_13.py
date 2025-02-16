# Calcular las componentes y módulo de un vector pasado por una función componente_y_modulo(origen, extremo), 
# se podrán pasar como maximo 3 valores, gráficar estos e incluir en la leyenda del gráfico las componentes y el módulo.

import numpy as np
import matplotlib.pyplot as plt

def componente_y_modulo(origen, extremo):

    componente = np.array(extremo) - np.array(origen) # Componente

    modulo = np.linalg.norm(componente) # Modulo

    # return f"El componente del vector ({origen};{extremo}) es {componente} y su modulo es {round(modulo, 2)}"
    return componente, round(modulo, 2)


origen = (-2,5)
extremo = (-3, 1)

print(componente_y_modulo(origen, extremo))

def graficar_vector(origen, extremo):
    # Calcular componentes y módulo
    vector, modulo = componente_y_modulo(origen, extremo)
    
    # Graficar el vector
    plt.quiver(origen[0], origen[1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue')

    # Añadir leyenda fuera del gráfico
    plt.text(10, 8, f'V: {vector}\n|V|: {modulo:.2f}', # Esto se lo tire a chatgtp, hay formas de escribir matemáticamente todo de manera más prolija pero bueno no es lo que busco ahora
             fontsize=10, ha='left', color='red')

    # Configurar los ejes
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    # Configurar los ejes en el centro
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    
    plt.grid()
    plt.title('Vector en 2D')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Ajustar la posición de los ticks
    plt.xticks(np.arange(-10, 11, 2))
    plt.yticks(np.arange(-10, 11, 2))
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Ejemplo de uso
origen = (-2,5)
extremo = (-3, 1)

graficar_vector(origen, extremo)

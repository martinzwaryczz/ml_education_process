# Crear la función gráficar_funcion(funcion), debe tener gráficada la función y las correspondientes asíntotas con una línea separada por renglones. (- - -)

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def posee_asintotas(funcion):
    x = sp.symbols('x')
    f = sp.sympify(funcion)

    # Asíntotas verticales
    asintotas_verticales = sp.solve(sp.denom(f), x)

    # Asíntotas horizontales
    limite_infinito = sp.limit(f, x, sp.oo)
    limite_menos_infinito = sp.limit(f, x, -sp.oo)

    asintotas_horizontales = []
    if limite_infinito.is_real:
        asintotas_horizontales.append(limite_infinito)
    if limite_menos_infinito.is_real:
        asintotas_horizontales.append(limite_menos_infinito)

    # Asíntotas oblicuas
    grado_funcion = sp.degree(sp.numer(f))
    grado_denominador = sp.degree(sp.denom(f))

    asintotas_oblicuas = []
    if grado_funcion == grado_denominador + 1:
        m = sp.limit(sp.diff(f, x), x, sp.oo)
        b = limite_infinito - m * sp.oo
        asintotas_oblicuas.append((m, b))

    return {
        'asintotas_verticales': asintotas_verticales,
        'asintotas_horizontales': asintotas_horizontales,
        'asintotas_oblicuas': asintotas_oblicuas
    }

def graficar_funcion(funcion):
    x = np.linspace(-10, 10, 400)
    f = eval(funcion.replace('x', 'x'))  # Evaluar la función

    plt.figure(figsize=(10, 6))
    plt.plot(x, f, label=f'f(x) = {funcion}', color='blue')

    # Obtener asíntotas
    resultados = posee_asintotas(funcion)

    # Graficar asíntotas verticales
    for av in resultados['asintotas_verticales']:
        plt.axvline(x=float(av), color='red', linestyle='--', label=f'Asíntota Vertical: x = {av}')

    # Graficar asíntotas horizontales
    for ah in resultados['asintotas_horizontales']:
        plt.axhline(y=float(ah), color='green', linestyle='--', label=f'Asíntota Horizontal: y = {ah}')

    # Graficar asíntotas oblicuas
    for ao in resultados['asintotas_oblicuas']:
        m, b = ao
        x_vals = np.linspace(-10, 10, 400)
        plt.plot(x_vals, m*x_vals + b, color='orange', linestyle='--', label=f'Asíntota Oblicua: y = {m}x + {b}')

    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.title('Gráfica de la Función y sus Asíntotas')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black',linewidth=2, ls='--', zorder=2)
    plt.axvline(0, color='black',linewidth=2, ls='--', zorder=2)
    plt.grid(zorder=1)
    plt.legend()
    plt.show()

# Ejemplo de uso:
funcion = '1/(x-1)'  # Cambia esta función por la que desees analizar
graficar_funcion(funcion)
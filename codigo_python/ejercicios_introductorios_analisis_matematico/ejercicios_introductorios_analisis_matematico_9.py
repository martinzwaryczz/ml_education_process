import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def teorema_de_lagrange(funcion, intervalo):
    x = sp.symbols('x')
    f = sp.sympify(funcion)

    a, b = intervalo

    # Calculamos los valores de la función en los extremos del intervalo
    fa = f.subs(x, a)
    fb = f.subs(x, b)

    # Calculamos la pendiente de la secante
    pendiente_secante = (fb - fa) / (b - a)

    # Derivamos la función
    f_derivada = sp.diff(f, x)

    # Buscamos el punto c donde la derivada es igual a la pendiente secante
    c = sp.solve(f_derivada - pendiente_secante, x)
    c = [float(val) for val in c if a < float(val) < b]  # Filtramos los valores en el intervalo

    # Generamos los valores de x en el intervalo [a, b]
    x_vals = np.linspace(a, b, 400)
    
    # Calculamos los valores de la función
    f_vals = []
    for val in x_vals:
        try:
            f_vals.append(float(f.evalf(subs={x: val})))
        except Exception as e:
            print(f"Error evaluando f en x = {val}: {e}")
            return

    # Filtramos valores no finitos
    f_vals = [val for val in f_vals if np.isfinite(val)]

    if not f_vals:
        print("Error: Todos los valores en f_vals son no finitos.")
        return

    # Calculamos límites del eje y
    min_val = min(f_vals) - 1
    max_val = max(f_vals) + 1
    
    # Aseguramos que los límites son válidos
    if np.isfinite(min_val) and np.isfinite(max_val):
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, f_vals, label=f'f(x) = {funcion}', color='blue')

        # Graficamos los puntos (a, f(a)) y (b, f(b))
        plt.scatter([a, b], [fa, fb], color='red')
        plt.plot([a, b], [fa, fb], color='orange', linestyle='--', label='Secante')

        # Graficamos el punto c y la recta tangente
        for val in c:
            y_c = f.evalf(subs={x: val})  # f(c)
            pendiente_tangente = f_derivada.evalf(subs={x: val})  # f'(c)

            # Ecuación de la recta tangente
            y_tangente = pendiente_tangente * (x_vals - val) + y_c

            # Graficar la recta tangente solo en el intervalo [a, b]
            plt.plot(x_vals, y_tangente, color='purple', linestyle=':', label='Recta Tangente en c')

            plt.scatter(val, y_c, color='green', label=f'c = {val:.2f}')

        plt.title('Teorema de Lagrange con Recta Tangente')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.xlim(a, b)  # Limitar el eje x al intervalo [a, b]
        
        # Ajustar el rango del eje y
        plt.ylim(min_val, max_val)

        plt.legend()
        plt.show()
    else:
        print("Error: Los límites del eje y no son válidos.")

    return c if c else "No se encontró un punto c en el intervalo."

# Ejemplo:
funcion = 'x**3 - 3*x + 2' 
intervalo = (0, 2)         
resultado = teorema_de_lagrange(funcion, intervalo)
print(f"Puntos c en el intervalo: {resultado}")
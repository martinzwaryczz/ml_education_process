# Calcular las raíces de un polinomio de grado 2, se pueden usar funciones de numpy y/o propias.
# Reutilizar la función del ejercicio anterior para retornar el polinomio y sus raices en un texto por consola

import numpy as np

# Calcular raíces
def calcular_raices(pol) -> str:
    return f"Las raices de {escribir_polinomio(pol)} son {np.roots(pol)}"

# Función del ejercicio anterior

def escribir_polinomio(coeffs):
    grado = len(coeffs) - 1
    polinomio = ""

    for i, coef in enumerate(coeffs):
        exp = grado - i
        if coef != 0:
            # Formatear el término
            if exp == 0:
                termino = f"{coef}"
            elif exp == 1:
                termino = f"{coef}x"
            else:
                termino = f"{coef}x^{exp}"

            # Concatenar el término al polinomio
            if polinomio:
                # Manejar el signo
                if coef > 0:
                    polinomio += " + " + termino
                else:
                    polinomio += " - " + termino.lstrip('-')
            else:
                polinomio += termino

    return polinomio if polinomio else "0"


# Probamos:

pol_p = [1, -4, 3]

print(calcular_raices(pol_p))
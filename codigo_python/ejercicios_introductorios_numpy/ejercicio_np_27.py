# Calcula 2.sin⁡(x)+cos⁡(2x)** en x=π3.
# Se puede mejorar, me imprime el polinomio medio mal pero bueno
import numpy as np

# Reutilizamos la función anterior
def evaluar_polinomios(polinomio, x) ->str:
    return f"El polinomio {escribir_polinomio(polinomio)} evaluado con {x} tiene el valor {round(np.polyval(polinomio, x))}"

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

x = np.pi * 3
pol = [2*np.sin(x), np.cos(2*x)]

print(evaluar_polinomios(pol, x))
# Evalúa el polinomio p(x) = x^3 - 4x + 1 en x=2
import numpy as np

def evaluar_polinomios(polinomio, x) ->str:
    return f"El polinomio {polinomio} evaluado con {x} tiene el valor {np.polyval(polinomio, x)}"

pol_p = [1, 0, -4, 1]
print(evaluar_polinomios(pol_p, 2))


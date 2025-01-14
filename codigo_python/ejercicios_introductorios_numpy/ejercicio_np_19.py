# Resta el polinomio q(x)= 4x^2 - 2x + 1 del polinomio p(x)= x^3 + 2x^2 + 5.
# Es curioso este ejemplo porque acá gracias a numpy podemos tratar como polinomios a las listas y utilizarlas a gusto, independientemente de su orden

import numpy as np

pol_q = [4, -3, 2]
pol_p = [2, 3, 0, 5]

resta_pol = np.polysub(pol_q, pol_p)
print(f"La resta de los polinomios q(x)= 4x^2 - 2x + 1 del polinomio p(x)= x^3 + 2x^2 + 5 es {resta_pol}")
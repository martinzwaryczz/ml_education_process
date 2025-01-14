# Divide el polinomio p(x) = 3x^4 - x^3 + 2x - 5 entre q(x) = x^2 + 1
import numpy as np

pol_p = [3, -1, 0, 2, -5]
pol_q = [1, 1]

div_pol, resudio = np.polydiv(pol_p, pol_q)

print(f"La división de los polinomios p(x) = 3x^4 - x^3 + 2x - 5 entre q(x) = x^2 + 1 es {div_pol} y tiene un resudio de {resudio}")
# Multiplica los polinomios p(x)=x + 2 y q(x) = 2x^2 - 3x + 1
import numpy as np

pol_p = [1, 2]
pol_q = [2, -3, 1]

mul_pol = np.polymul(pol_p, pol_q)
print(f"La multiplicación de los polinomios p(x)=x + 2 y q(x) = 2x^2 - 3x + 1 es {mul_pol}")

#  Suma los polinomios:
#  p(x) = 2x^3 + 3x^2 - 4
#  q(x) = x^2 - 5x + 6

# Para sumar estos polinomios cargaremos los mismos en una lista, si nuestro polinomio no tiene cierto grado pondrémos 0 pero no es el caso
import numpy as np

pol_p = [2,3,0,-4]
pol_q = [1,-5,6]

suma_pol = np.polyadd(pol_p, pol_q)
print(f"La suma de los polinomios es: {suma_pol}") # Tengo que investigar sobre como escribir bien el polinomio, imprime otra lista y no me gusta

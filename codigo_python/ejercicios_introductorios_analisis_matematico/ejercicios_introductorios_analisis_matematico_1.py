# Crear la función limite_de(limite, variable, valor) y devolver el límite.

import numpy as np
import sympy as sp

def limite_de(limite, variable, valor):
    return sp.limit(limite, variable, valor)

# Ejemplos de límites:

x = sp.symbols('x')
f = (sp.sin(x) - x) / (x**3)

print(limite_de(f, x, 0)) # -1/6, comprobar con GeoGebra o manualmente incluso
# Crear una función que confirme si una integral fue correctamente realizada derivando la misma.

import sympy as sp

def derivada_de(funcion):
    x = sp.symbols('x')

    f = sp.sympify(funcion)

    derivada = sp.diff(f, x)
    return derivada

def integral_de(funcion):
    x = sp.symbols('x')
    f = sp.sympify(funcion)

    integral = sp.integrate(f, x)
    return integral


funcion = '2*x + 3'  
resultado_integral = integral_de(funcion)

funcion = 'x**2 + 3*x + 2'  
resultado_derivada = derivada_de(funcion)

def esta_bien_integrado(resultado_integral, resultado_derivada) -> bool:
    return True if sp.sympify(resultado_integral - resultado_derivada) == 0 else False

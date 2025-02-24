import sympy as sp

def derivada_de(funcion):
    x = sp.symbols('x')

    f = sp.sympify(funcion)

    derivada = sp.diff(f, x)
    return derivada

funcion = 'x**2 + 3*x + 2'  
resultado_derivada = derivada_de(funcion)
print(f"La derivada de {funcion} es: {resultado_derivada}")
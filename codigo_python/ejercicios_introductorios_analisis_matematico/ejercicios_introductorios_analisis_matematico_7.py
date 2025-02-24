import sympy as sp

def integral_de(funcion):
    x = sp.symbols('x')
    f = sp.sympify(funcion)

    integral = sp.integrate(f, x)
    return integral

funcion = '2*x + 3'  
resultado_integral = integral_de(funcion)
print(f"La integral de {funcion} es: {resultado_integral} + C")
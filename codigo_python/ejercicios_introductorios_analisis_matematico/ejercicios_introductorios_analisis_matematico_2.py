# Crear la función es_continua(función, intervalo) y retornar si es continua o no.

# Para determinar si una función es o no continua debemos calcular sus limites en el intervalo dado, debe existir una imagen en estos y deberá ser igual a los límites.

import sympy as sp

def es_continua(funcion, intervalo):
    x = sp.symbols('x')
    a, b = intervalo

    limite_izquierdo = sp.limit(funcion, x, a, dir='-')
    limite_derecho = sp.limit(funcion, x, a, dir='+')

    valor_en_a = funcion.subs(x, a) if a != 0 else limite_izquierdo

    limite_izquierdo_b = sp.limit(funcion, x, b, dir='-')
    limite_derecho_b = sp.limit(funcion, x, b, dir='+')
    valor_en_b = funcion.subs(x, b)

    # Comprobar continuidad, valores boleanos
    continua_a = (limite_izquierdo == limite_derecho) and (limite_derecho == valor_en_a)
    continua_b = (limite_izquierdo_b == limite_derecho_b) and (limite_derecho_b == valor_en_b)

    return continua_a and continua_b # Es un and, si uno es falso la función no será continua en el intervalo y retornará False.

# Ejemplo de uso
x = sp.symbols('x')
f = (sp.sin(x) - x) / (x**3)  # Función a verificar
intervalo = (0, 1)  # Intervalo a comprobar

resultado = es_continua(f, intervalo)
print("La función es continua en el intervalo:", resultado)
# Crear la función posee_asintotas, en caso de que tenga asíntotas decir cuáles tiene y que formula o valor toman.

# Para saber si una función posee asíntotas debemos empezar por ver que valores quedan excluidos del dominio, estos serán candidatos a AV en caso de que el lim x-> {valores excluidos del dominio} sea igual a infinito, en caso contrario no tendrá asintota ahí
# Para saber si tiene asíntota horizontal con pendiente 0 debemos hacer el lim x-> infinito, si esto nos da un valor tendrá AH con b=0, caso contrario podrá tener AV con cierta b

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def posee_asintotas(funcion):
    x = sp.symbols('x')
    f = sp.sympify(funcion)
    
    asintotas_verticales = sp.solve(sp.denom(f), x) # AV

    limite_infinito = sp.limit(f, x, sp.oo) # oo = infinito
    limite_menos_infinito = sp.limit(f, x, -sp.oo)

    asintotas_horizontales = []

    if limite_infinito.is_real:
        asintotas_horizontales.append(limite_infinito)
    if limite_menos_infinito.is_real:
        asintotas_horizontales.append(limite_menos_infinito)


    grado_funcion = sp.degree(sp.numer(f))
    grado_denominador = sp.degree(sp.denom(f))

    asintotas_oblicuas = []
    if grado_funcion == grado_denominador + 1:
       m = sp.limit(sp.diff(f, x), x, sp.oo)
       b = limite_infinito - m * sp.oo
       asintotas_oblicuas.append((m, b))
    
    return {
        'asintotas_verticales': asintotas_verticales,
        'asintotas_horizontales': asintotas_horizontales,
        'asintotas_oblicuas': asintotas_oblicuas
    }
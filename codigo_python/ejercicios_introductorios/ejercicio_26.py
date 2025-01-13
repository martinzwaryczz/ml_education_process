# Invertir un string, sin usar la biblioteca que lo haga automáticamente
# Se puede mejorar, si la cadena tiene acentos y/o espacios da varios problemas pero bueno

def invertir(a):
    b = ""
    for i in range(0, len(a), 1): # range(start, stop, step)
        b = a[i] + b
    return b

print(invertir("cadena"))
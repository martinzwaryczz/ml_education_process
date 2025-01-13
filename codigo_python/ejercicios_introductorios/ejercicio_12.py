# Dado un conjunto de valores numéricos que se ingresan por teclado determinar el valor promedio. El fin de datos se indicará ingresando un valor igual a cero

def promedio():
    val = int(input("Ingrese un conjunto de valores, terminará la carga cuando sea igual a 0: "))
    sum_val = 0
    cont_val = 0
    while val != 0:
        sum_val += val
        cont_val += 1
        val = int(input("Ingrese otro valor: "))
    return f"El promedio es de: {sum_val / cont_val}"

print(promedio())
# Realizar una función que tome como parámetro un polinomio de una variable en forma de lista y retorne este en formato String escrito con su variables y grados.
def escribir_polinomio(coeffs):
    grado = len(coeffs) - 1
    polinomio = ""

    for i, coef in enumerate(coeffs):
        exp = grado - i
        if coef != 0:
            # Formatear el término
            if exp == 0:
                termino = f"{coef}"
            elif exp == 1:
                termino = f"{coef}x"
            else:
                termino = f"{coef}x^{exp}"

            # Concatenar el término al polinomio
            if polinomio:
                # Manejar el signo
                if coef > 0:
                    polinomio += " + " + termino
                else:
                    polinomio += " - " + termino.lstrip('-')
            else:
                polinomio += termino

    return polinomio if polinomio else "0"

# Cargar polinomios:
p_coeff = [1, 0, -4, 1]  # x^3 - 4x + 1
polinomio_str = escribir_polinomio(p_coeff)
print(f"Polinomio: {polinomio_str}")
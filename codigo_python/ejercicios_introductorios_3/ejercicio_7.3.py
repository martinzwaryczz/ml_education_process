# Escribir una función que reciba una cadena que números romanos y retorne su valor en digitos del 0 al 9.

def romano_a_entero(num_romano):
    dicc_romano = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    longitud = len(num_romano)

    for i in range(longitud):
        if i + 1 < longitud and dicc_romano[num_romano[i]] < dicc_romano[num_romano[i + 1]]:
            total -= dicc_romano[num_romano[i]]
        else:
            total += dicc_romano[num_romano[i]]

    return total

# print(romano_a_entero("III"))  
# print(romano_a_entero("IV"))    
print(romano_a_entero("IX"))    
# print(romano_a_entero("LVIII")) 
# print(romano_a_entero("MCMXCIV")) 
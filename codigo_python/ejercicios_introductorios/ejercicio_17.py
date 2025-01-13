# Se ingresa por consola un número entero que representa un sueldo que se debe pagar. Considerando que existen billetes de las denominaciones que se indican más abajo;
#  informar, que cantidad de billetes de cada denominación se deberá utilizar, dando prioridad a los de valor nominal más alto. Denominaciones ($) = {100, 50, 20, 10, 5, 2, 1}

def cantidada_billetes(sueldo):
    billetes = (100, 50, 20, 10, 5, 2, 1) # Uso una tupla ya que los billetes "a mano" son esos, pero es lo mismo usar una lista salvo que se requiera un método o función, ojo ahí
    for billete in billetes:
        contador_billetes = sueldo // billete
        sueldo = sueldo % billete
        if contador_billetes > 0:
            print(f"Se necesitan {contador_billetes} billetes de {billete}.")
    
sueldo = int(input("Indique el importe a abonar: "))
cantidada_billetes(sueldo)
# Implementar una función que recibe dos enteros de 8 dígitos con el formato aaaammdd,
#  informar cuál de las dos es la anterior y cuál la posterior. Usar lo aplicado en ejercicio anterior

# Las variantes no las voy a hacer, pero serian como en el ejercico 4: acceder al año, mes y día de diferente manera y aplicar la lógica para saber que fecha es posterior y anterior
# Se puede mejorar el código diciendo que la fecha, en caso de ser lo contrario a posterior, sea anterior, puse todo anterior, no esta mal pero se puede mejorar

def comparar_fechas(fecha_uno, fecha_dos):

    # Accedemos a los datos, para usar la tecnica que estamos usando los pasamos a str:

    fecha_uno = str(fecha_uno)
    fecha_dos = str(fecha_dos)


    anio_fecha_uno = fecha_uno[:4]
    mes_fecha_uno = fecha_uno[4:6]
    dia_fecha_uno = fecha_uno[6:8]

    anio_fecha_dos = fecha_dos[:4]
    mes_fecha_dos = fecha_dos[4:6]
    dia_fecha_dos = fecha_dos[6:8]

    # Comparamos fechas con un if, elif eterno...

    if anio_fecha_uno < anio_fecha_dos:
        return f"La fecha {escribir_fecha(fecha_uno)} es anterior a la fecha {escribir_fecha(fecha_dos)}"
    elif anio_fecha_uno > anio_fecha_dos:
        return f"La fecha {escribir_fecha(fecha_dos)} es anterior a la fecha {escribir_fecha(fecha_uno)}"
    elif anio_fecha_dos == anio_fecha_dos:
        if mes_fecha_uno < mes_fecha_dos:
            return f"La {escribir_fecha(fecha_uno)} es anterior a la fecha {escribir_fecha(fecha_dos)}"
        elif mes_fecha_uno > mes_fecha_dos:
            return f"La {escribir_fecha(fecha_dos)} es anterior a la fecha {escribir_fecha(fecha_uno)}"
        elif mes_fecha_uno == mes_fecha_dos:
            if dia_fecha_uno < dia_fecha_dos:
                return f"La {escribir_fecha(fecha_uno)} es anterior a la {escribir_fecha(fecha_dos)}"
            elif dia_fecha_dos > dia_fecha_dos:
                return f"La {escribir_fecha(fecha_dos)} es anterior a la {escribir_fecha(fecha_uno)}"
            elif dia_fecha_dos == dia_fecha_uno:
                return f"Las {escribir_fecha(fecha_uno)} es igual a la {escribir_fecha(fecha_dos)}"
            
def escribir_fecha(fecha) -> str:
    fecha = str(fecha)
    return f"{fecha[:4]}/{fecha[4:6]}/{fecha[6:8]}"


print(comparar_fechas(20030418, 20030418)) # Igual
print(comparar_fechas(20030401, 20030404)) # Anterior
print(comparar_fechas(20200301, 20200401)) # Anterior
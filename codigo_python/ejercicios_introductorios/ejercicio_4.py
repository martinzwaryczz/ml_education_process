# Se ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato aaaammdd. 
# Se pide informar por separado el día, el mes y el año de la fecha ingresada

date = int(input("Ingrese un numero con formaeto AAAAMMDD, se dirá que año, mes y día corresponde a este: "))

# Variante 1:

anio = date // 10000 # El operador // corresponde a la división entera
mes = date // 100 % 100
dia = date % 100

print(f"La fecha ingresada sin fue: {date}")
print(f"El año correspondiente a la fecha calculado manualmente es: {anio}.")
print(f"El mes correspondiente a la fecha calculado manualmente es {mes}.")
print(f"El día correspondiente a la fecha calculado manualmente es {dia}.\n\n")

# Variante 2:

date_str = str(date)

print(f"La fecha string es {date_str}")
print(f"El año correspondiente a la fecha accediendo a este como si fuera un string es: {date_str[:4]}")
print(f"El mes correspondiente a la fecha accediendo a este como si fuera un string es: {date_str[4:6]}")
print(f"El día correspondiente a la fecha accediendo a este como si fuera un string es: {date_str[6:8]}")

# Anexo: con estos datos podrémos incluso hacer una función que retorne la fecha en formato AAAA / MM / DD

def fecha_con_formato(anio, mes, dia) -> str:
    return f"{anio}/{mes}/{dia}"

print(f"La funcion fecha con formato retorna entonces: {fecha_con_formato(anio, mes, dia)}")

# También podrémos realizar funciones especificas que calculen el año, mes y día retornando estos valores y permitiendo ser reutilizados muchas veces sin problema
# Esto nos permitirá comparar fechas, tal como se pedirá en proximos ejercicios
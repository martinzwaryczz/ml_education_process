# Leer un valor numérico que representa un día de la semana. 
# Se pide mostrar por pantalla el nombre del día considerando que el lunes es el día 1, el martes es el día 2 y así, sucesivamente

# Variante 1: hacer 8 ifs, no existe el switch case en python, no voy a hacerlo así, no tiene sentido ya se hacer un if

# Variante 2: usar una tupla, estas son inmutables, una vez hechas no pueden ser alteradas, pero si pueden ser accedidas mediante índices

dias_de_la_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
dias_numericos = (1, 2, 3, 4, 5, 6, 7)

def fun_dia(dia):
    if dia not in dias_numericos:
        raise ValueError(f"El número {dia} no corresponde a un día de la semana.")
    else:
         print(f"El día correspondiente al número {dia} es el {dias_de_la_semana[dia-1]}") # Como el índice arranca en 0 ponemos el día-1

fun_dia(1)
fun_dia(2)
fun_dia(3)
fun_dia(4)
fun_dia(5)
fun_dia(6)
fun_dia(7)

# Acá tira el error
fun_dia(10)
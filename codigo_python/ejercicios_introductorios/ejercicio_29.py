# ESTE NO LO HICE YO LO HIZO SAN CHATGTP

# 29. Se tiene una tabla o planilla con los resultados de la última llamada a examen de una materia, con la siguiente información:
#    - Matricula (valor numérico entero de 8 dígitos)
#    - Nota (valor numérico entero de 2 dígitos entre 1 y 10)
#    - Nombre (valor alfanumérico de 10 caracteres)
#    - Se pide informar:
#        1. Cantidad de alumnos que se presentaron a rendir examen
#        2. Nota promedio
#        3. Nombre y nota del alumno que obtuvo el mejor resultado (será único)
#    - Para indicar el fin del ingreso de datos el operador ingresará un registro nulo con matrícula =0, nota=0 y nombre=""

# Inicialización de variables
alumnos = []
total_notas = 0

while True:
    # Ingreso de datos
    matricula = int(input("Ingrese la matrícula (0 para terminar): "))
    if matricula == 0:
        break
    nota = int(input("Ingrese la nota (0 para terminar): "))
    if nota == 0:
        break
    nombre = input("Ingrese el nombre (10 caracteres): ")
    
    # Validación de nombre
    if len(nombre) != 10:
        print("El nombre debe tener exactamente 10 caracteres.")
        continue
    
    # Guardar los datos del alumno
    alumnos.append((matricula, nota, nombre))
    total_notas += nota

# Cálculos requeridos
cantidad_alumnos = len(alumnos)
nota_promedio = total_notas / cantidad_alumnos if cantidad_alumnos > 0 else 0

# Encontrar el alumno con la mejor nota
mejor_alumno = max(alumnos, key=lambda x: x[1]) if alumnos else None

# Resultados
print(f"\nCantidad de alumnos que se presentaron: {cantidad_alumnos}")
print(f"Nota promedio: {nota_promedio:.2f}")
if mejor_alumno:
    matricula_mejor, nota_mejor, nombre_mejor = mejor_alumno
    print(f"Mejor alumno: {nombre_mejor} con nota {nota_mejor}")
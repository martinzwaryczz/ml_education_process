# Se ingresa por teclado un conjunto de valores numéricos enteros positivos, 
# se pide informar, por cada uno, si el valor ingresado es par o impar. Para indicar el final se ingresará un valor cero o negativo

print("Ingrese valores positivos, se dirá si son pares o impares, la carga finalizará cuando el valor ingresado sea negativo o cero.")

val_inicial = int(input("Ingrese un valor: "))
lista_val = []

while val_inicial > 0:
    lista_val.append(val_inicial)
    val_inicial = int(input("Ingrese un valor: "))

for i in lista_val:
    if i%2 == 0:
        print(f"El valor {i} es par.")
    else:
        print(f"El valor {i} es impar.")
# FizzBuzz: Imprimir por pantalla los números del 1 al 100 pero considerando lo siguiente: a) Si el número es divisible por 3 se debe imprimir "Fizz".
#  b) Si el número es divisible por 5 se debe imprimir "Buzz". c) Si el número es divisible por 3 y por 5 se debe imprimir "FizzBuzz"


# Es importante saber que se puede simplificar una bararidad de codigo si entendemos como usar los operadores en Python

def fizzbuzz():
    for i in range(1, 101):
        print("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)
        
print(fizzbuzz())
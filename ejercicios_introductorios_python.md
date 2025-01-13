1. Informar "Hola mundo"
2. Leer dos valores enteros e informar la suma y su cociente
3. Dado un valor numérico entero, informar si es par o impar
4. Se ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato aaaammdd. Se pide informar por separado el día, el mes y el año de la fecha ingresada
5. Leer dos valores numéricos enteros e indicar cual es el mayor y cual es el menor. Considerar que ambos valores son diferentes
6. Leer tres valores numéricos enteros, indicar cual es el mayor, cuál es el del medio y cuál el menor. Considerar que los tres valores son diferentes
7. Leer un valor numérico que representa un día de la semana. Se pide mostrar por pantalla el nombre del día considerando que el lunes es el día 1, el martes es el día 2 y así, sucesivamente
8. Se ingresa por teclado un conjunto de valores numéricos enteros positivos, se pide informar, por cada uno, si el valor ingresado es par o impar. Para indicar el final se ingresará un valor cero o negativo
9. Sumados: Sumar los 1000 primeros números naturales (1 + 2 + 3 + 4 + … + 1000), imprimiendo por cada suma el resultado parcial obtenido
10. Desarrollar una función que muestre por pantalla los primeros n números naturales considerando al 0 (cero) como primer número natural, siendo n un valor que se pasa por parámetro
11. Escribir una función que calcule la suma de los múltiplos de 3 o 5, mayores o iguales que 0 y menores que un parámetro n. Por ejemplo la llamada:
    - sumaMultiplos(10); // devuelve 23 (3+5+6+9)
    - sumaMultiplos(16); // devuelve 60 (3+5+6+9+10+12+15)
12. Dado un conjunto de valores numéricos que se ingresan por teclado determinar el valor promedio. El fin de datos se indicará ingresando un valor igual a cero
13. Se ingresa un valor numérico por consola, determinar e informar si se trata de un número primo o no
14. Desarrollar un algoritmo que muestre los primeros n números primos siendo n un valor que debe ingresar el usuario
15. Dado un conjunto de valores numéricos indicar cuál es el mayor. El ingreso de datos finaliza con la llegada de un cero
16. Determinar el menor valor de un conjunto de números e indicar también su posición relativa dentro del mismo. El ingreso de datos finaliza con la llegada de un cero
17. Se ingresa por consola un número entero que representa un sueldo que se debe pagar. Considerando que existen billetes de las denominaciones que se indican más abajo; informar, que cantidad de billetes de cada denominación se deberá utilizar, dando prioridad a los de valor nominal más alto. Denominaciones ($) = {100, 50, 20, 10, 5, 2, 1}
18. Implementar una función que recibe dos enteros de 8 dígitos con el formato aaaammdd, informar cuál de las dos es la anterior y cuál la posterior. Usar lo aplicado en ejercicio anterior
19. Determinar si un carácter es un dígito numérico (**función esDigito(char c)**)
20. Determinar si un carácter es una letra (**función esLetra(char c)**)
21. Determinar si un carácter es una letra mayúscula o minúscula (**función esMayuscula(char c) y esMinuscula(char c)**)
22. Determinar la longitud de una cadena (función longitud)
23. Determinar si una cadena es vacía (función esVacia)
24. Concatenar dos cadenas (función concatenarCadena)
25. Comparar cadenas (función comparaCadenas)
26. Invertir un string, sin usar la biblioteca que lo haga automáticamente
27. Escribir una función que reciba un string y lo devuelva invertido. Por ejemplo: invertirCadena("Hola"),retorna "aloH". Reutilice la función implementada para decir si una palabra es o no, un palíndromo. **esPalindromo("neuquen")** devuelve true
28. FizzBuzz: Imprimir por pantalla los números del 1 al 100 pero considerando lo siguiente: a) Si el número es divisible por 3 se debe imprimir "Fizz". b) Si el número es divisible por 5 se debe imprimir "Buzz". c) Si el número es divisible por 3 y por 5 se debe imprimir "FizzBuzz"
29. Se tiene una tabla o planilla con los resultados de la última llamada a examen de una materia, con la siguiente información:
    - Matricula (valor numérico entero de 8 dígitos)
    - Nota (valor numérico entero de 2 dígitos entre 1 y 10)
    - Nombre (valor alfanumérico de 10 caracteres)
    - Se pide informar:
        1. Cantidad de alumnos que se presentaron a rendir examen
        2. Nota promedio
        3. Nombre y nota del alumno que obtuvo el mejor resultado (será único)
    - Para indicar el fin del ingreso de datos el operador ingresará un registro nulo con matrícula =0, nota=0 y nombre=""
30. Escribir una función que reciba un arreglo de enteros y devuelva true si el arreglo está ordenado de mayor a menor y false si está desordenado
31. Escribir una función que reciba un arreglo de enteros y devuelva la suma de los elementos que se encuentran en posiciones pares (incluido el elemento de la posición 0). Por ejemplo: Dado el arreglo [1, 2, 13 ,4, 8, 6] => devuelve 22 (1+13+8)
32. Implementar una función que reciba como parámetro un arreglo de enteros y muestre por pantalla cuántas veces se repite cada uno. El arreglo no está ordenado. Se garantiza que a los sumo habrá 100 números diferentes
33. Escribir una función que reciba dos matrices de NxN y devuelva la suma de las mismas. Podemos considerar que las matrices se representan como un arreglo bidimensional
34. Escribir una función que reciba dos arreglos a1 y a2, de enteros ordenados de menor a mayor e intercale los elementos de los arreglos que recibe en un nuevo arreglo, tal que el arreglo resultante también esté ordenado. Por ejemplo:
    
    - a1 = [-5, 0, 0, 1, 5]
    - a2 = [-10, 0, 7]
    - resultado = [-10, -5, 0, 0, 0, 1, 5, 7]
35. Encriptar un mensaje usando el método de "la cifra del césar", que consiste en correr cada letra -considerando la posición de cada una en el alfabeto- una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra "HOLA" se transforma en "JQNC". Si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra "a"
36. Escribir una función consonantes que recibe una cadena de caracteres y devuelve la cadena que resulta de eliminar todas las vocales de la cadena recibida. Por ejemplo: **consonantes("hola como estas");** // devuelve "hl cm sts"
37. **Escribir una función que reciba una cadena de caracteres muestre por pantalla la frecuencia de aparición de cada letra. Por ejemplo: frecuencias("hola como estas..."); // debe mostrar por pantalla:    ```**
      **a: 2**
      **c: 1**
      **e: 1**
      **h: 1**
      **l: 1**
      **m: 1**
      **o: 3**
      **s: 2**
      **t: 1**
    ```
38. Desarrollar un programa que le permita al usuario ingresar un conjunto de 10 valores enteros. Luego se debe imprimir el conjunto que el usuario ingresó, primero en el orden original y luego en el inverso. Por ejemplo, si el usuario ingresa: 12, 43, 5, 26, 7, 98, 1, 32, 18, 9 la salida del programa debe ser la siguiente:
    - Orden original: 12 43 5 26 7 98 1 32 18 9
    - Orden inverso: 9 18 32 1 98 7 26 5 43 12
    
39. Dado una lista de número enteros mayores o iguales a 0 y menores que 100 determinar e informar cuántas veces aparece cada uno. El conjunto finaliza con la llegada de un valor negativo
40. **Se ingresa un conjunto de ternas de valores que representan el año, el grado y la cantidad de alumnos que se inscribieron en un colegio durante ese año y para ese grado en particular. Solo se ingresará la información comprendida entre los años 2000 y 2009. En el colegio, los alumnos cursan desde el primer grado hasta el séptimo. Los datos se ingresan sin ningún tipo de orden. Se pide:**
    1. **Emitir un listado ordenado por año detallando para cada año la cantidad de inscriptos por grado**
    2. **Emitir un listado ordenado por grado detallando para cada grado la cantidad de inscriptos por año**
41. Implementar la función: **busquedaSecuencial(int [] arreglo, int valorBuscado)** que recibe un arreglo de enteros y un valor a buscar, y devuelve la posición del valor buscado, o -1 si el valor no se encuentra
Hasta acá fueron todos ejercicios sacados del siguiente repostorio: https://github.com/ppandomail/poo/blob/main/doc/02-intro-loo-ejercicios.md.
Los ejercicios marcados en negrita de momento no fueron realizados.


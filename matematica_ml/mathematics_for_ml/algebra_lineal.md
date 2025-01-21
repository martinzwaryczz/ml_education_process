# Algebra lineal

> Previo a cualquier apunte quiero aclarar que, a mi criterio según el orden que inicialmente aprendí los temas, el libro esta algo desordenado en lo que temas amerita, por lo que volcaré los conceptos en el orden que consideré que me sea claro.

Cuando hablamos del algebra lineal nos referimos al estudio de vectores y - en palabras del libro - ciertas reglas para manipularlos.

Cuando queremos formalizar de manera intuitiva ciertos conceptos es una buena estrategia hablar con cierto vocabulario y usar ciertos simbolos para hablar de los diferentes objetos que componen el tema de estudio.

Siendo las matemáticas el *lenguaje de dios* debemos casi obligatoriamente formalizar estos conceptos.

Los vectores existen en la programación, física, matemática y quizas en otras areas del conocimiento que desconozco.

En el caso del algebra nos referiremos a los vectores como letras con una flecha arriba llamados ***"vectores geométricos"***.
                                              ![image](https://github.com/user-attachments/assets/1f130eaa-c69f-43e5-900b-ff677b661685)
                                              
Estos pueden tener un ***R*** dimensión, por ejemplo:                               
                                               ![image](https://github.com/user-attachments/assets/b2da0754-194b-4d64-b373-0115968be6a4)
                                               
Si un vector es del mismo ***R*** se pueden sumar, restar, multiplicar cada elemento por un escalar *(pero no al revés)* y otras operaciones más que no se contemplan de momento. ***Si luego se ven modificaré con ejemplos***


Considero que ya se hacer estas operaciones, de hecho cualquier persona de manera mecánica las puede hacer, no es el objetivo contemplar el como se hacen estas operaciones sino entender su vista e interpretación geométrica.

> **¿Qué es, cartesiana y geometricamente, un vector?**

Así sea más programador que matemático, usarémos el vector en el contexto matemático.
En el contexto matemático un vector es un objeto que tiene magnitud y una dirección, tal como se ve en la imagen de arriba.
Geometricamente hablando en R2 podemos decir que se ve de la siguiente manera:
![image](https://github.com/user-attachments/assets/9580d583-c7a7-4f8c-8cb6-6105fe87e5cc)

Al ser un espacio bidimensional debemos tener un punto de anclaje de donde saldrá nuestro vector, el primero nos dirá que tanto nos tenemos que mover a lo largo del eje X, el segundo del Y, y hacia ahí irá el vector, siendo su distancia su modulo,
siendo su modulo la raíz cuadrada de la sumatoria de sus elementos, cada uno de estos estando al cuadrado.

Veniamos hablando de R2, cuando pasamos a R3 tendrémos que agregar el eje Z, cuando pasamos de R dimensión > 3 no podrémos representarlos de ninguna manera posible en este universo.
Cuando hablamos de R3 cada vector esta asociado a una tripleta de números.
El primero nos dirá cuando debemos movernos en el eje X, el segundo en el eje Y y por último, el tercero, en el eje Z:
![image](https://github.com/user-attachments/assets/73af29b2-d5b3-45e7-a3bb-3272ce6d97f9)

Cada vector tiene su único par de números y cada par de números a su vez su único vector, así como cada vector tiene su modulo.
Podrémos sumar vectores y multiplicarlos por un escalar, **aunque esta ultima no es conmutativa**, mucho cuidado:

![image](https://github.com/user-attachments/assets/a0b9fcd3-6a13-45d5-a49f-e6fa575447c1)

En terminos genericos:

![image](https://github.com/user-attachments/assets/e2a11154-646e-414a-abaa-915c840be48a)

Cuando hablamos de un escalar:

![image](https://github.com/user-attachments/assets/fcf68d71-4f7a-4efc-aa10-4b295cdbd293)

Según el autor o fuente el algebra gira entorno a la suma de vectores y multiplicación de un escalar por vectores. 

Al los vectores genericos que apuntan al eje x, y, z respetivamente se les llama, *i,j y k*. Se podría decir que apuntan 1 unidad y se mueven (Xn, Yn, Zn) valores en el espacio Rn en cuestión, se les llama *"base"*.





Falta mucho, independientemente de esto, complementaré mi lectura con el siguiente canal de YouTube: https://www.youtube.com/watch?v=0Ndnzx6AyaA&list=PLIb_io8a5NB2DddFf-PwvZDCOUNT1GZoA

                                      

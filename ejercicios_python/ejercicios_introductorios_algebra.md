### Matrices
1. Dada una matriz pasada por parametro a la función orden_matricial(matriz) indicar el order de la matriz en cuestión.
2. Dada una matriz de orden *nxm* indicar por parametro en la función elemento_matricial(matriz, elemento), siendo el elemento el índice de esta, en caso de que no exista lanzar un ValueError().
3. Dadas dos matrices retornar la suma de estas.
4. Dadas dos matrices retornar el producto de estas, recordar que el producto matricial no es conmutativo, confimar si es posible realizar dicho producto, de ser necesario utilizar implemetaciones de código anteriormente hechas.
5. Dada una matriz retornar su traspuesta.
6. Dada una matriz retornar su inversa.
7. Dada una matriz retornar el cuadrado de esta.
8. Dada una matriz y la función exponente_matricial(matriz, exponente) elevar la función al exponente.
9. Dada una matriz de cualquier orden posible de visiualizar gráficar esta, en caso de que no sea posible devolver una imagen.
### Determinantes:
10. Dada una matriz indicar su determinante.
### Sistemas de ecuaciones:
11. Dado un sistema de ecuación pasado por función junto a un conjunto de soluciones indicar cuáles son y cuáles no, estos últimos podrán ser indefinidos, es decir: solucion_de(sistema, soluciones*).
12. Clasificar un sistema de ecuaciones por función con clasificar_sistema(sistema) con el teorema de Rouché-Fröbenius.
### Vectores algebráicos: 
13. Calcular las componentes y módulo de un vector pasado por una función componente_y_modulo(origen, extremo), se podrán pasar como maximo 3 valores, gráficar estos e incluir en la leyenda del gráfico las componentes y el módulo.
14. Calcular diferentes operaciones matemáticas con vectores, en caso de que sea imposible calcular la misma (un vector por un escalar, una resta o suma de un vector y un escalar) lanzar un ValueError().
15. Calcular el versor asociado a un vector pasado por la función versor_asociado_a(vector).
16. Dado un vector u y otro v hallar los valores de los escalares faltantes para que se de lugar al vector correspondiente, siendo este un sistema de ecuaciones.
17. Indicar si dos vectores son paralelos con la función son_paralelos.
18. Indicar si dos vectores son equipolentes.
### Espacios vectoriales:
19. Determinar si un vector dado es combinación líneal de otros dos pasados por parametro, útilizar ejemplo del libro Matemathics for ML.
20. Determinar la dimensión de un espacio vectorial generado por vectores pasados a través de una función espacio_generado_por(vector1, vector2, vector3).
21. Utilizar la función anterior para gráficar el espacio generado con la función graficar_espacio(vector1, vector2, vector3). 
### Autovalores y autovectores:
23. Dada una función auto_valores_y_auto_vec(matriz) calcular los autovalores y autovectores de la matriz pasada como parametro.
24. Utilizando la función anterior establecer si la matriz es o no diagonalizable, en caso de que lo sea diagonalizar y mostrar la misma por consola.

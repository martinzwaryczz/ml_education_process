Hablamos de *matrices* cuando tenemos una disposición bidimensional de números reales a los que llamaremos **"elementos"** con sus correspondientes índices *i* que indicarán las filas y *j* que indicarán las columnas.
Estos números reales constituyen vectores, pero es tema de más adelante en el caso del orden de estos apuntes.

#### Orden de matrices:
El orden de una matriz será la cantidad de filas y columnas que tenga, es decir.
Si denotamos nuestras matrices con una letra mayúscula y su orden podemos decir que son de orden $A_{mn}$, siendo *n* la última columna y *m* la última fila. 
Un ejemplo de una matriz sería: 
$$
A = \begin{pmatrix}
3 & 7 & 1 \\
5 & 2 & 9 \\
4 & 6 & 8
\end{pmatrix}
$$
En este caso el orden es de 3x3.

#### Equidad de matrices:
Para que dos matrices <span style="color: #005700;">sean iguales </span>deben tener el mismo orden y los elementos deben ser iguales, es decir, los elementos accedidos a través de su subíndice deberán ser iguales.

#### Matrices cuadradas:
Se dice que una matriz es cuadrada cuando las mismas tienen un orden *n=m*, estas a su vez contienen lo que llamamos <span style="color: #A52A2A;"> una traza </span>, esta es la sumatoria de los elementos de la diagonal principal.
Un ejemplo de la traza de una matriz seria:
$$
A = \begin{pmatrix}
1 & 3 & 5 \\
2 & 4 & 6 \\
1 & 1 & 10
\end{pmatrix}
$$
                             $Tr(A)= 1 + 4 + 10 = 15$
Las  <span style="color: #A52A2A;">propiedades de una traza</span> son:
$$
\begin{aligned}
- & \text{ Tr} (a \cdot A) = a \cdot \text{Tr} (A) \\
- & \text{ Tr} (A + B) = \text{Tr} (A) + \text{Tr} (B)
\end{aligned}
$$
Siendo $a$ un valor real.
#### Operaciones con matrices:
###### Matriz traspuesta:

Podemos realizar operaciones con matrices, una de ellas es la <span style="color: #A52A2A;">matriz traspuesta</span>.
Esta consiste en cambiar las filas por columnas, esta, genéricamente, se denota de la siguiente manera:
$$
A = \begin{pmatrix}
a_{11} & \cdots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{m1} & \cdots & a_{mn}
\end{pmatrix} \Rightarrow A^T = \begin{pmatrix}
a_{11} & \cdots & a_{m1} \\
\vdots & \ddots & \vdots \\
a_{1n} & \cdots & a_{mn}
\end{pmatrix}
$$
Una <span style="color: #A52A2A;">matriz es simétrica</span> cuando su traspuesta es igual.
Una <span style="color: #A52A2A;">matriz es anti simétrica</span> que es un igual la opuesta de su traspuesta, es decir: los elementos cambian de signo. En este caso los elementos de la diagonal son 0.

###### Suma de matrices *(o Addition):
Para <span style="color: #A52A2A;">sumar dos o más matrices</span> debemos tener en cuenta que el orden debe ser el mismo, sumando elemento por elemento obtendremos una nueva matriz resultante de la suma de estás.
$$
\begin{aligned}
\text{Sea } & A = (a_{ij}), B = (b_{ij}) \in \mathbb{R}^{m \times n}: A + B = C \\ 
\text{Siendo } & C = (c_{ij}) \in \mathbb{R}^{m \times n} \, | \, c_{ij} = a_{ij} + b_{ij}
\end{aligned}
$$

$$
A + B = (a_{ij}) + (b_{ij}) =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34}
\end{pmatrix}
+
\begin{pmatrix}
b_{11} & b_{12} & b_{13} & b_{14} \\
b_{21} & b_{22} & b_{23} & b_{24} \\
b_{31} & b_{32} & b_{33} & b_{34}
\end{pmatrix}
=
\begin{pmatrix}
(a_{11} + b_{11}) & (a_{12} + b_{12}) & (a_{13} + b_{13}) & (a_{14} + b_{14}) \\
(a_{21} + b_{21}) & (a_{22} + b_{22}) & (a_{23} + b_{23}) & (a_{24} + b_{24}) \\
(a_{31} + b_{31}) & (a_{32} + b_{32}) & (a_{33} + b_{33}) & (a_{34} + b_{34})
\end{pmatrix}
=
C
$$
La suma de dos matrices de mismo orden dará como resultado otra matriz con el mismo orden.
###### Producto de un número por una matriz *(o Multiplication by a Scalar)*:
Podremos multiplicar un número real por una matriz, pero no al revés.
$$
k \cdot A = k \cdot (a_{ij}) = k \cdot 
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
=
\begin{pmatrix}
k a_{11} & k a_{12} & k a_{13} \\
k a_{21} & k a_{22} & k a_{23} \\
k a_{31} & k a_{32} & k a_{33}
\end{pmatrix}
=
(k a_{ij})
$$
Tal cómo se ve en el ejemplo de arriba, esta consta de multiplicar cada valor *k* por cada elemento de la matriz, dado como resultado una matriz de igual orden a la que le aplicamos el producto.
###### Multiplicación de matrices
<span style="color: #A52A2A;">Podremos multiplicar matrices si y solo si la cantidad de columnas de la primera matriz es igual a la cantidad de filas de la segunda matriz. </span>
**La multiplicación de matrices no es conmutativa**.
En caso de ser posible nos dará como resultado una matriz con el orden de las filas de la primer matriz y las columnas de la segunda.
$$
A = 
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}_{2 \times 3}, \quad
B = 
\begin{pmatrix}
7 & 8 \\
9 & 10 \\
11 & 12
\end{pmatrix}_{3 \times 2}
$$

$$
C = A \cdot B = 
\begin{pmatrix}
1\cdot 7 + 2\cdot 9 + 3\cdot 11 & 1\cdot 8 + 2\cdot 10 + 3\cdot 12 \\
4\cdot 7 + 5\cdot 9 + 6\cdot 11 & 4\cdot 8 + 5\cdot 10 + 6\cdot 12
\end{pmatrix} 
$$

$$
C = 
\begin{pmatrix}
58 & 64 \\
139 & 154
\end{pmatrix}_{2 \times 2}
$$
Cada elemento será el resultado de la *<span style="color: #7FFFD4;">fila</span> x <span style="color: #7FFFD4;">columna</span>*.
###### Potencia de una matriz
La potencia de una matriz es n veces dicha matriz multiplicada por si misma:
$$
A^n = A \cdot A \cdot \ldots \cdot A \quad \text{(n veces)}
$$


#### Características y comportamientos de las matrices:
##### Rango de una matriz:
El rango de una matriz es un número que representa el número de <span style="color: #7FFFD4;">dimensiones </span>en la imagen, es por esto que es la cantidad de vectores canónicos que puedan formarse mediante diferentes métodos que se verán luego.
Por ejemplo:
$$
A = 
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}, \quad
B = 
\begin{pmatrix}
1 & 1 & 0 \\
0 & 0 & 0 \\
0 & 0 & 1
\end{pmatrix}, \quad
C = 
\begin{pmatrix}
1 & 0 & -3 \\
0 & 1 & 2 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
$$

$$
\rho(A) = 3, \quad \rho(B) = 2, \quad \rho(C) = 2
$$
Aclaración: en el [libro](https://mml-book.github.io/book/mml-book.pdf) se habla del rango de una matriz como: $$ rk(A)$$
Usa el método de eliminación Gaussiana, sin embargo yo usaré *la regla del triangulo*, hacen lo mismo de otra manera.
Si es necesario programarlo se puede programar, pero ya librerías como *numPy* hacen ese trabajo tan tedioso. 
Entonces podemos decir que para calcular el rango de una matriz debemos aplicar la regla del triangulo, los pasos son los siguientes:
1) Se elige un pivote *(elemento distinto de 0, preferiblemente 1 en el primer elemento)*.
2) La fila del pivote se divide por este, si es 1 se omite este paso.
3) Los elementos de la columna del pivote se hacen 0, menos el pivote que se hace 1.
4) Los demás elementos de la matriz se transforman, ahora sí, por *la regla del rectángulo*, repitiendo esto con todos los elementos.
La regla del rectángulo consta de:
1) Multiplicar el valor elegido por n diagonal, sumarlo al m diagonal al costado y dividirlo por el pivote


##### Matriz identidad:
La matriz identidad es aquella que es cuadrada y los elementos de su diagonal son 1 y el resto son 0: $$
I = 
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$


##### Matriz inversa:
Se dice que una matriz admite inversa si existe una matriz simbolizada por: $$
A^{-1}
$$
que multiplicada a derecha y a izquierda por la matriz dada A da como resultado la matriz identidad: $$
A \in \mathbb{R}^{m \times n}, \exists A^{-1} \in \mathbb{R}^{n \times m} \text{ tal que } A A^{-1} = A^{-1} A = I
$$
Si la matriz inversa existe, es única, y la condición para que exista es que el rango de dicha matriz nxn sea n.
Calcular esta manualmente es super tedioso, insoportable si por cada vez que nuestros modelos de ML lo necesitarían, sin embargo acá va una breve explicación:
$$
\begin{pmatrix}
A & I \\
\hline
I & A^{-1}
\end{pmatrix}
$$
Por limitaciones del programa no puedo poner otra línea vertical, pero la idea sería aplicar la regla del rectángulo y de esa manera llegar a la inversa.  

##### Propiedades de suma y multiplicación de matrices: 
- **Asociativa:** $$ A + (B + C) = (A + B) + C $$ - **Conmutativa:** $$ A + B = B + A $$ - **Elemento neutro:** $$ A + N = N + A = A $$
  Siento N una matriz compuesta solo por 0 y el mismo orden de A.
- **Elemento opuesto:** $$ A + (-A) = (-A) + A = N $$
##### Propiedades de las matrices traspuestas: 
$$
\begin{align*}
AA^{-1} & = I = A^{-1}A \\
(AB)^{-1} & = B^{-1}A^{-1} \\
(A + B)^{-1} & \neq A^{-1} + B^{-1} \\
(A^T)^T & = A \\
(AB)^T & = B^TA^T \\
(A + B)^T & = A^T + B^T
\end{align*}
$$

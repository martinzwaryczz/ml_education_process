# Enfoque del libro en el capitulo 1: 


![[Pasted image 20250121120918.png]]

Por mi parte empezaré con matrices, trataré de respetar las técnicas y orden en el cual los temas son presentados.
Por ejemplo: los determinantes no son tema de este capitulo, por lo que no los tocaré. 
Sin embargo las matrices, vectores y sistemas de ecuaciones sí, por lo que trataré de ser lo más respetuoso posible con la forma de escribir de los autores, dado que probablemente otras fuentes también de habla inglesa utilicen los mimos términos. 

Debemos saber es que es una *ecuación lineal*.
Para saber que es una ecuación lineal debemos saber, en el contexto de las matemáticas, que es una **relación**.
##### ¿Qué es una relación en matemática...?
En matemáticas, una **relación** en un [conjunto](https://es.wikipedia.org/wiki/Conjunto "Conjunto") es alguna clase de vínculo que puede darse o puede no darse (sin posibilidad de estados intermedios) entre dos miembros de un conjunto determinado.
##### ¿Qué es una ecuación lineal...?:
Una **ecuación lineal** es una expresión matemática que representa una relación lineal entre dos o más variables, podemos representarlo de la siguiente manera:$$
a_1 x_1 + a_2 x_2 + \ldots + a_n x_n = b
$$
##### ¿Qué es un grupo en el contexto del libro...?
#### En inglés:
Un grupo es un conjunto de elementos y operaciones definidos sobre estos elementos que mantiene intacta la estructura del mismo.

> [!NOTE] Página 35
> [...] Now, we are ready to formalize this, and we will start by introducing the concept of a group, which is a set of elements and an operation defined on these elements that keeps some structure of the set intact.

Los grupos son más que importantes, según este libro al menos, en la computación.
Nos proveen una estructura para operar sobre conjuntos y se utilizan en muchas ramas de esta.
Acá tendré bastante cuidado con mi traducción, la definición del libro puede o no ser tan literal, es por esto que pondré nuevamente los axiomas a tener en cuenta en ingles, luego los traduciré y por último los explicaré:

> [!NOTE] Página 36 2.4.1
> **Definition 2.7** (Group). Consider a set G and an operation ⊗ : G ×G → G group defined on G. Then G := (G, ⊗) is called a group if the following hold: 
> 1. *Closure of G* under ⊗: ∀x, y ∈ G : x ⊗ y ∈ G
> 2. *Associativity:* ∀x, y, z ∈ G : (x ⊗ y) ⊗ z = x ⊗ (y ⊗ z)
> 3. *Neutral element:* ∃e ∈ G ∀x ∈ G : x ⊗ e = x and e ⊗ x = x
> 4. *Inverse element*: ∀x ∈ G ∃y ∈ G : x ⊗ y = e and y ⊗ x = e, where e is the neutral element. We often write x^−1 to denote the inverse element of x.

> [!NOTE] Página 36 2.4.1 - Aclaración:
> *Remark*. The inverse element is defined with respect to the operation ⊗ and does not necessarily mean 1/x . 


> [!NOTE] Página 36 2.4.1 - Grupo abeliano
> If additionally ∀x, y ∈ G : x ⊗ y = y ⊗ x, then G = (G, ⊗) is an *Abelian group (commutative)*.

#### En español: 
La definición de grupos, en el contexto de la teoría de grupos *(Me queda pendiente ver si es igual a la teoría de conjuntos)* menciona los grupos como conjuntos:

> [!NOTE] ChatGTP y lo que entendí
> Se menciona un conjunto *G* y una operación ∗:*G×G→G*  que se define sobre este conjunto. Esto significa que la operación toma dos elementos del conjunto *G* y produce otro elemento en *G*.

Para que esto se cumpla deben cumplirse las siguientes propiedades:

> [!NOTE] Chat GTP y lo que entendí Página 36 2.4.1
> 1. Cierre: Para todo *a,b∈ G* , el resultado de *a∗ba* también debe estar en *G*.
> 2. Asociatividad: Para todo *a,b,c ∈ G* también debe:$$
e(a \cdot b) \cdot c = a \cdot (b \cdot c).
$$  3. Elemento neutro: Debe existir un elemento *e ∈ G* tal que todo x ∈ G: $$
x \in G, \quad x * e = e * x = x.
$$4. Inverso: Para cada elemento  x ∈ G debe existir un elemento *y* ∈ G tal que: $$
x * y = y * x = e
$$ Donde *e* es el elemento neutro, se denota el inverso de x como x elevado a -1.

Grupo abeliano o conmutativo:

> [!NOTE] ChatGTP y lo que entendí grupo abeliano o conmutativo:
> Un grupo se llama **abeliano** o **conmutativo** si la operación entre sus elementos satisface la propiedad conmutativa, es decir, el orden de los elementos no afecta el resultado de la operación:
> $$
x * y = y * x \quad \text{para todo } x, y \in G
$$

En el caso de la explicación de que son los espacios vectoriales hablamos de axiomas que la bibliografía denota como grupos que deben cumplir ciertas condiciones, aunque es bastante tedioso de leer y en la universidad me lo explicaron de una mejor manera no esta demás saber esta explicación.

Transformaciones líneales:

> [!NOTE] 2.7 Linear Mappings
> In the following, we will study mappings on vector spaces that preserve their structure, which will allow us to define the concept of a coordinate. In the beginning of the chapter, we said that vectors are objects that can be added together and multiplied by a scalar, and the resulting object is still a vector. We wish to preserve this property when applying the mapping: Consider two real vector spaces V, W. A mapping Φ : V → W preserves the structure of the vector space if [condiciones]

Inicialmente mal interprete este concepto, volví con la duda y mi intuición no fallo: linear mappings no hace referencia a "mapear linealmente" o "graficar" sino a las transformaciones línales, ojo con traducir literalmente. 
Cuando hablamos de vectores hablamos de un par ordenados de puntos según el R en donde, por ejemplo, en caso de R2 (A,B) A es el origen y B el extremo.
Los vectores se representan por medio de un segmento orientado.
![[Pasted image 20250121123446.png]]
Los vectores pueden ser fijos o libres, es decir: su punto de aplicación no puede variar o si.
Para el análisis de datos usaremos vectores libres.
Los vectores componen matrices, espacios vectoriales, subespacios, y tienen a su vez operaciones.
Estas operaciones son:
                     - Producto de un escalar por un vector
                     -  Producto de un vector por otro
Omitiré ejercicios de productos y su explicación: considero que a estas alturas no puedo sacar nada de detenme en eso.
##### Espacio vectorial
Definiremos **espacio vectorial** como un, irónicamente, **espacio** en donde un conjunto de vectores existe. 
La definición del libro es la siguiente:

> [!NOTE] 2.4.2 Vector Spaces
> **Definition 2.9** (Vector Space). A real-valued vector space V = (V, +, ·) a set V with two operations:
>                                + : V × V → V 
>                                ·   : R × V → V
> where [...] habla de axiomas

La definición que nos proporciona el libro es valida pero super técnica al punto de no ser valida y clara para realizar un apunte tal como este que estoy haciendo, es por esto que daré a continuación la definición de un espacio vectorial:
Un espacio vectorial es un *conjunto* de vectores que pueden sumarse entre sí y multiplicarse por escalares, dichas operaciones son:
                      ![[Pasted image 20250122223235.png]]
  Y las propiedades son:
                       ![[Pasted image 20250122223318.png]]
                       
##### Subespacios vectoriales: 



> [!NOTE] Página 39 - 2.4.3 Vector Subspaces:
> Intuitively, they are sets contained in the original vector space with the property that when we perform vector space operations on elements within this subspace, we will never leave it. In this sense, they are “closed". Vector subspaces are a key idea in machine learning. For example, Chapter 10 demonstrates how to use vector subspaces for dimensionality reduction.
> 

Lo que nos quiere decir el libro es que un subespacio vectorial es un ***subconjunto*** de un espacio vectorial determinado que también cumple con las condiciones de un espacio vectorial.
Para verificar que dicho subconjunto es un espacio vectorial debemos realizar los axiomas mencionados anteriormente, para confirmar que es un subespacio de un tal espacio vectorial debemos:
![[Pasted image 20250122223821.png]]
Hay ejercicios realizados en el GitHub.

##### Independencia lineal de vectores y combinación lineal: 
Es increíble lo simple pero complejo que es a veces este concepto dado que se nombra o muy rápido o en el aire, pero la independencia lineal de los vectores va de lo siguiente:

> [!NOTE] 2.5 Linear Independence
> In the following, we will have a close look at what we can do with vectors (elements of the vector space). In particular, we can add vectors together and multiply them with scalars. The closure property guarantees that we end up with another vector in the same vector space. It is possible to find a set of vectors with which we can represent every vector in the vector space by adding them together and scaling them. This set of vectors is a basis, and we will discuss them in Section 2.6.1. Before we get there, we will need to introduce the concepts of linear combinations and linear independence.

Lo que el libro nos quiere decir es que gracias a la gracias a las propiedades que deben seguir los subespacios es posible encontrar todos los vectores que componen dicho espacio, pudiendo hablar así de una combinación lineal, esta maravilla es la combinación lineal. 
Entonces, ya sabiendo esto, podemos hablar de *vectores linealmente independientes* cuando la única combinación lineal que da 0 es la trivial, es decir: en la que todos los coeficientes son 0 decimemos si los ***linealmente independientes***.
En caso contrario, si existe ese o más son ***linealmente dependientes***.
##### Base de un espacio vectorial
La base de un espacio vectorial es el conjunto de vectores que puede generar el espacio completo a través de combinaciones lineales. 
##### Conjunto generador y base
Un conjunto de vectores *A* es un **conjunto generador** para el espacio vectorial *V* si cualquier vector *v en V* puede ser expresado como una combinación lineal de los vectores en *A*. Esto significa que *A* tiene la capacidad de *"generar"* todo el espacio.
En esta parte ya si que es interesante no abstraerse tanto con definiciones y ver ejercicios hechos.
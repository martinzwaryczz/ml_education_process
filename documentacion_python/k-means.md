El algoritmo de *k-means* es un modelo de clasificación NO supervisado, es decir: no tendremos etiquetas y sin la necesidad de estas podremos clasificar sin problema nuestros datos en *clusters* o grupos. 

Para esto tendremos en primer lugar nuestro set de datos correspondiente y su gráfico, esto puede darnos inicialmente una idea a simple vista de cuantos grupos podremos formar, aunque esto por supuesto que no es a ojo, pero vamos por partes.

Para este apunte usaré el ejemplo de código máquina, el gráfico normalizado es el siguiente:
                 ![[Pasted image 20250214215512.png]]
Teniendo este gráfico podríamos decir que hay 3 *clusters* y que de esta manera podremos clasificar los datos de la mejor manera posible, sin embargo esto no es así, luego veremos porque.

Sacando los genéricos pasos de importar las correspondientes librerías y cargar los dataset es importante saber que importaremos el modulo:  <span style="color: #569cd6;">from</span> <span style="color: #d69d85;">sklearn.cluster</span> <span style="color: #569cd6;">import</span> <span style="color: #d69d85;">KMeans</span>

Para crear nuestro objeto *k-means* debemos utilizar la siguiente sintaxis: 
              <span style="color: #d69d85;">kmeans</span> <span style="color: #569cd6;">=</span> <span style="color: #d69d85;">KMeans</span>(<span style="color: #569cd6;">n_clusters=9</span>).<span style="color: #d69d85;">fit</span>(<span style="color: #d69d85;">clientes.values</span>)
Durante el .fit se asignaran centroides aleatoriamente que se irán adaptando a nuestros grupos según que cantidad de clusters indiquemos, el como se hace esto no es tema para tomar en este apunte.

Luego de esto se crearán nuestros clusters indexados según los valores entrenados, es por esto que debemos agregar al DataFrame una columna con los grupos correspondientes llamados *kmeans.labels_*
Es por esto que nuestro DataFrame quedará de la siguiente manera:
                         ![[Pasted image 20250214220545.png]]
Para graficar los grupos ya creados podemos crear una lista de colores, recorrer la lista *kmeans.n_clusters* y por cada cluster asignar una nube de puntos con un determinado color al correspondiente cluster con su correspondiente centroide.    
                 ![[Pasted image 20250214220948.png]]
Ahora bien, ¿Cómo establecí que 9 es la cantidad más optima de grupos? La respuesta esta en que criterio utilicemos para determinar esto.
%% Acá haré un paréntesis, hay muchas maneras e iré actualizando a medida que las vaya aprendiendo, utilizando y entendiendo %%
### Método del codo:
El método del codo gráfica la suma de los errores cuadráticos (SSE) para diferentes valores de *n_clusters*.

Se llama así dado que donde se produce la disminución de errores cuadráticos la gráfica comenzará a ser menos pronunciada, por lo que se parecerá a un "codo".  
             ![[Pasted image 20250214221510.png]]
Tal como podemos ver en la sintaxis del código, crearemos una lista de *inercias* y bucle *for* que vaya de desde la cantidad mínima de clusters (2 dado que al menos tendremos que tener 2 grupos) a la máxima que es 10 dado que queda excluido, siendo en realidad 9, aunque aquí no hay limite, siempre y cuando la inercia no tome un valor exageradamente bajo, siendo este un *overfitting*.

Luego crearemos un objeto kmeans con el valor k correspondiente al for y lo entrenaremos con los valores del DF ya con los clusters.

Guardaremos en la lista de inercias el valor *kmeans.inertia__* y graficaremos estos valores en función al rango establecido previamente.  
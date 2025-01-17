Si bien para introducirme a Python, Pandas y Numpy no realicé ningún apunte, en este caso ya si que amerita realizar un apunte que sirva para revisar y tener cierta orientación en los temas a ver.
La librería seaborn nos permitirá graficar muchas cosas, particularmente son 3:
## Gráficos relacionales:
- Gráfico de dispersión o scatterplot
- Gráfico de líneas o lineplot
## Gráfico de distribuciones:
- Histograma o histplot
- Kdeplot
- Ecdfplot
- rugplot
## Gráficos categóricos: 
* stripplot
* swarmplot
* boxplot
* violinplot
* pointplot
* barplot

![[Pasted image 20250114212151.png]]
En español serían los siguientes:
![[Pasted image 20250114215317.png]]
Si queremos ver estás a detalle debemos acceder a la galería oficial de la librería: https://seaborn.pydata.org/examples/index.html
Seaborn es una especialización de matplotlib, es por esto que si bien este apunte esta orientado a seaborn se usará en ciertos casos matplotlib.
Dado que para graficar datos debemos tener estos ordenados acá ya si usaremos la librería pandas y, nuevamente, algún set de datos de Kaggle. 
# Proyectos básicos de aprendizaje automático con sklearn

## PCA (Análisis de Componentes Principales)
1. **Visualización 3D de datos de vino**
   - Usar PCA para reducir a 3 componentes principales y graficar en 3D.

2. **PCA con normalización previa**
   - Estandarizar datos y luego aplicar PCA en un conjunto de datos.

3. **Reconstrucción de datos después de PCA**
   - Reducir a 2 componentes y reconstruir datos para evaluar pérdida de información.

4. **Explicación de varianza acumulada**
   - Graficar la varianza explicada acumulada en datos de cáncer de mama.

5. **PCA en imágenes**
   - Aplicar PCA para comprimir imágenes y visualizarlas.

6. **Detección de anomalías con PCA**
   - Usar PCA para detectar anomalías en un conjunto de datos.
---

## Regresión Lineal
1. **Predecir precios de casas**
   - Entrenar un modelo para predecir precios basado en el tamaño y número de habitaciones.

2. **Relación entre horas de estudio y calificaciones**
   - Crear un modelo para analizar la correlación.

3. **Pronóstico de ventas**
   - Predecir ventas basándose en presupuesto publicitario.

4. **Regresión lineal múltiple**
   - Usar múltiples variables predictoras en datos de salud: nivel de actividad diario, calorias consumidas y peso como variable dependiente.

5. **Error cuadrático medio**
   - Calcular y analizar el error cuadrático medio en predicciones de cualquier modelo previamente hecho, escribir conclusiones.

6. **Gráfico de residuales**
   - Crear un gráfico de residuales para evaluar la calidad del modelo.

7. **Cross-validation en regresión lineal**
    - Evaluar el modelo del punto 3 con validación cruzada.

---

## Regresión Logística
1. **Clasificación de correos electrónicos (spam/no spam)**
   - Entrenar un modelo en un conjunto de datos de correos.

2. **Clasificación de imágenes en blanco y negro**
   - Usar regresión logística para clasificar imágenes simples.
---

## k-Vecinos más Cercanos (KNN) 

1. **Clasificación de flores (Iris)**
   - Entrenar un modelo KNN para clasificar especies de flores.

3. **KNN para regresión**
   - Predecir valores continuos con KNN en datos simples.

4. **Detección de outliers**
   - Usar KNN para identificar puntos atípicos.

5. **Clasificación de dígitos escritos a mano**
   - Usar KNN en un conjunto de datos de imágenes de dígitos. (es un ejercicio interesante, ver vídeos ya que a su vez es algo complejo)

6. **Distancia ponderada en KNN**
   - Implementar un modelo KNN con distancias ponderadas teniendo en cuenta: edad, prestamo, si pago o no.

7. **Validación cruzada en KNN**
   - Evaluar el rendimiento del modelo con validación cruzada.

---

## K-Means
1. **Agrupamiento de Clientes según su Comportamiento de Compra**
   
   Tienes un dataset de clientes de una tienda en línea con las siguientes características:
   
      - ID del Cliente 
      - Edad
      - Ingresos Anuales ($)
      - Gasto Promedio Mensual ($)
      - Número de Compras al Año
        
Aplica **K-Means** para segmentar a los clientes en grupos según su comportamiento de compra.

---

## Test de Hipótesis (De momento no vi que es el test de hipotesis y por paros aún no lo ví en la facultad)
1. **Comparación de medias (t-test)**
   - Evaluar si dos grupos tienen medias significativamente diferentes.

2. **Test de proporciones**
   - Analizar si las proporciones de dos grupos son diferentes.

3. **Chi-cuadrado**
   - Verificar la independencia entre dos variables categóricas.

4. **Análisis ANOVA**
   - Comparar medias de más de dos grupos.

5. **Test de Kolmogorov-Smirnov**
   - Comparar si dos distribuciones son iguales.

6. **Shapiro-Wilk para normalidad**
   - Evaluar si los datos siguen una distribución normal.

7. **Regresión lineal con prueba de hipótesis**
   - Evaluar la significancia de los coeficientes.

8. **Test de Mann-Whitney U**
   - Comparar distribuciones entre dos grupos.

9. **Prueba de Wilcoxon**
   - Evaluar diferencias en datos emparejados.

10. **Prueba de Friedman**
    - Comparar más de dos grupos emparejados.

---

## Support Vector Machines (SVM)
1. **Clasificación binaria con SVM**
   - Usar SVM para clasificar datos simples (Iris).

2. **SVM con kernel RBF**
   - Comparar el rendimiento con diferentes kernels.

3. **Clasificación de imágenes**
   - Usar SVM en un conjunto de datos de imágenes de dígitos.

4. **Visualización de fronteras de decisión**
   - Graficar la frontera de decisión de un modelo SVM.

5. **SVM con datos no lineales**
   - Crear un modelo con kernel no lineal en datos sintéticos.

6. **SVM para regresión**
   - Usar SVR (regresión con SVM) en datos continuos.

7. **Regularización en SVM**
   - Comparar modelos con diferentes valores de C.

8. **Clasificación multicategoría con SVM**
   - Extender SVM para clasificar más de dos clases.

9. **SVM con reducción de dimensionalidad**
   - Usar PCA antes de entrenar el modelo.

10. **Optimización de hiperparámetros en SVM**
    - Usar GridSearchCV para encontrar los mejores parámetros.

---

## Árboles de Decisión
1. **Clasificación de datos de flores (Iris)**
   - Entrenar un árbol de decisión para clasificar especies.

2. **Visualización de árbol**
   - Graficar el árbol de decisión.

3. **Pruning de árboles**
   - Implementar poda para reducir el sobreajuste, buscar otro ejemplo que no sea del de flores de Iris.

4. **Regresión con árboles**
   - Crear un modelo de regresión basado en árboles, buscar otro ejemplo que no sea del de flores de Iris y repasar árboles de matemática discreta.

5. **Clasificación de dígitos escritos a mano**
   - Usar árboles para clasificar imágenes de dígitos.

6. **Validación cruzada con árboles**
   - Evaluar el rendimiento del modelo anterior con validación cruzada.

7. **Optimización de hiperparámetros**
   - Usar GridSearchCV para optimizar la profundidad y el número mínimo de muestras.

8. **Árbol de decisión con datos ruidosos**
    - Entrenar un árbol en un conjunto de datos con ruido para evaluar su robustez.
  
---

## Bosques aleatorios


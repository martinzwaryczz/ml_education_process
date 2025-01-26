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
   - Usar múltiples variables predictoras en datos de salud, tales como nivel de actividad diario, calorias consumidas y peso como variable dependiente.

5. **Error cuadrático medio**
   - Calcular y analizar el error cuadrático medio en predicciones de cualquier modelo previamente hecho, escribir conclusiones.

6. **Gráfico de residuales**
   - Crear un gráfico de residuales para evaluar la calidad del modelo.

7. **Impacto de características normalizadas**
   - Analizar cómo afecta la normalizadas a la regresión lineal.

8. **Predecir consumo energético**
   - Modelo para predecir consumo basado en temperatura y hora del día.

9. **Cross-validation en regresión lineal**
    - Evaluar el modelo del punto 3 con validación cruzada.

---

## Regresión Logística
1. **Clasificación de correos electrónicos (spam/no spam)**
   - Entrenar un modelo en un conjunto de datos de correos.

2. **Diagnóstico de diabetes**
   - Clasificar pacientes con o sin diabetes basado en características médicas.

3. **Clasificación de imágenes en blanco y negro**
   - Usar regresión logística para clasificar imágenes simples.

4. **Predicción de aprobación de préstamos**
   - Determinar si un préstamo será aprobado.

5. **Evaluación de métricas (precision, recall, F1)**
   - Calcular métricas clave para evaluar el modelo.

6. **Curva ROC**
   - Graficar y analizar la curva ROC, dar en el archivo adjunto una definición de qué es una curva ROC.

7. **Clasificación de flores con datos de iris**
   - Crear un modelo basado en características del conjunto de datos, investigar sobre dicho dataset.

9. **Predicción de resultados deportivos**
    - Usar datos históricos para predecir el resultado de juegos. **desarrollar más este punto, la consigna**

---

## k-Vecinos más Cercanos (KNN) - De este punto en adelante son ejercicios que no puedo decir nada, no llegue aún a estos modelos por lo que dejo lo que según chatgtp es valido como ejercicios básicos

1. **Clasificación de flores (Iris)**
   - Entrenar un modelo KNN para clasificar especies de flores.

2. **Elección del mejor valor de K**
   - Graficar la precisión del modelo en función del valor de K.

3. **KNN para regresión**
   - Predecir valores continuos con KNN en datos simples.

4. **Detección de outliers**
   - Usar KNN para identificar puntos atípicos.

5. **Comparación con otros clasificadores**
   - Comparar KNN con regresión logística en precisión.

6. **Clasificación de dígitos escritos a mano**
   - Usar KNN en un conjunto de datos de imágenes de dígitos.

7. **Predicción de aprobación de préstamos**
   - Modelo basado en características del cliente.

8. **Distancia ponderada en KNN**
   - Implementar un modelo KNN con distancias ponderadas.

9. **Validación cruzada en KNN**
   - Evaluar el rendimiento del modelo con validación cruzada.

10. **Clusterización después de KNN**
    - Aplicar KNN después de agrupar datos con k-means.

---

## K-Means
1. **Clusterización de clientes**
   - Agrupar clientes basado en su comportamiento de compra.

2. **Clusterización de especies de flores (Iris)**
   - Usar k-means para agrupar flores y compararlo con las etiquetas reales.

3. **Elección del número de clusters**
   - Graficar la inercia para determinar el mejor número de clusters.

4. **Clusterización en datos 3D**
   - Visualizar clusters en tres dimensiones.

5. **Agrupación de datos de salud**
   - Dividir pacientes en grupos basado en características médicas.

6. **Clusterización en imágenes**
   - Usar k-means para segmentar imágenes en diferentes regiones.

7. **K-means con inicialización aleatoria**
   - Comparar resultados de diferentes inicializaciones.

8. **Evaluación con índice de Silhouette**
   - Calcular y analizar el índice de Silhouette para evaluar los clusters.

9. **Clusterización de transacciones**
   - Agrupar transacciones bancarias para identificar patrones.

10. **Clusterización y reducción de dimensionalidad**
    - Combinar PCA con k-means para agrupar datos.

---

## Teste de Hipótesis
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
   - Implementar poda para reducir el sobreajuste.

4. **Regresión con árboles**
   - Crear un modelo de regresión basado en árboles.

5. **Importancia de características**
   - Analizar las características más importantes del modelo.

6. **Clasificación de dígitos escritos a mano**
   - Usar árboles para clasificar imágenes de dígitos.

7. **Validación cruzada con árboles**
   - Evaluar el rendimiento del modelo con validación cruzada.

8. **Comparación con bosques aleatorios**
   - Comparar el rendimiento de un árbol con un bosque aleatorio.

9. **Optimización de hiperparámetros**
   - Usar GridSearchCV para optimizar la profundidad y el número mínimo de muestras.

10. **Árbol de decisión con datos ruidosos**
    - Entrenar un árbol en un conjunto de datos con ruido para evaluar su robustez.


# Calcula el valor de sin⁡(30°)+cos⁡(30°)\sin(30°) +cos(30°)sin(30°)+cos(30°)
# Recordar que las funciones en numpy utilizan radianes 
import numpy as np

angulo = np.radians(30)

resultado = ((np.sin(angulo) + np.cos(angulo)) / (np.sin(angulo)) + np.cos(30) * (np.sin(30) + np.cos(30)))
print(resultado)


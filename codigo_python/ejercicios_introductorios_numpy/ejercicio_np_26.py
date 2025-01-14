# Realizar tan⁡(60°)−tan⁡(45°) / tan(60°)
import numpy as np

angulo60 = np.radians(60)
angulo45 = np.radians(45)

resultado = np.tan(angulo60) - (np.tan(45) / np.tan(60))
print(f"El resultado de es tan⁡(60°)−tan⁡(45°)/tan(60°): {resultado}")

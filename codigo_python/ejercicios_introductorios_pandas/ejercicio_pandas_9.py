# Realizar un promedio de Daily_Calorie_Intake
import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

promedio_calorias_diarias = df["Daily_Calorie_Intake"].mean()
print(f"El promedio de las calorias por día es: {round(promedio_calorias_diarias)}")
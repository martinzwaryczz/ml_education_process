# Filtrar a las personas que tengan una dieta vegetariana y que tengan una dieta de menos de 2.000 calorías
# Averiguar como hacer que se muestren todos los log

import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

def filtrar_vegana_2000_cal(df):
    return df[(df["Diet_Type"] == "Vegetarian") & (df["Daily_Calorie_Intake"] < 2000)][[
        "Person_ID", "Age", "Gender", "Region", "Diet_Type", "Daily_Calorie_Intake"]]

print(filtrar_vegana_2000_cal(df))
# Filtrar a las personas que tengan una dieta vegetariana 
import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

def filtrar_dieta_vegana(df):
    return df[df["Diet_Type"] == "Vegetarian"] # Retornaremos un DataFrame donde nuestro DataFrame sea vegetariano

print(filtrar_dieta_vegana(df))
# Identificar que campos guarda el csv
import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

# print(df.columns)

def escribir_columnas(df):
    for columna in df.columns:
        print(columna)

print(escribir_columnas(df))
# Mostrar cuantas personas hay por atributo
import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

def cant_personas_por_atributo(atributo, df):
    dic_cant_por_atributo = {}

    if atributo in df.columns:
        conteo = df[atributo].value_counts()
        for valor, cantidad in conteo.items():
            dic_cant_por_atributo[valor] = cantidad
        return dic_cant_por_atributo
    else:
        raise ValueError("Atributo erróneo, no existe en el DataFrame asignado.")       

print(cant_personas_por_atributo("Region", df)) # Region
print(cant_personas_por_atributo("Gender", df)) # Genero

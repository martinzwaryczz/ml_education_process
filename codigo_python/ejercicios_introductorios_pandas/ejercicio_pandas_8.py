# Crear un DataFrame que contenga todos los campos del csv leído con cada dato de forma no repetida.
import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)


def valores_de(atributo, df):
    if atributo in df.columns:
        return df[atributo].unique().tolist()
    else:
        raise ValueError("Error, el atributo no existe en el DataFrame indicado. ")

print(valores_de("Gender", df))
print(valores_de("Diet_Type", df))
# Lo dejo comentado porque se va al carajo el log
# print(valores_de("Daily_Calorie_Intake", df)) 
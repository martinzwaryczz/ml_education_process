# Guardar el DataFrame anterior en un nuevo archivo.csv
import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

def personas_por_localidad_y_cal(df):
    nuevo_df = df.groupby('Region')['Daily_Calorie_Intake'].sum().reset_index()
    return nuevo_df

personas_por_localidad_y_cal(df).to_csv('./csv/region_y_calorias_15.csv', index=False)
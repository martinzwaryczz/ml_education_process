# Agregar al DataFrame una columna que tenga la fecha de nacimiento de las personas, 
# no debe estar hardcodeada, se debe poder acceder al año en el que se este ejecutando el programa

import pandas as pd

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

def personas_por_localidad_y_cal(df):
    return df.groupby('Region')['Daily_Calorie_Intake'].sum()

print(personas_por_localidad_y_cal(df))
# Agregar al DataFrame una columna que tenga la fecha de nacimiento de las personas,
# no debe estar hardcodeada, se debe poder acceder al año en el que se este ejecutando el programa.
import pandas as pd
from datetime import date

csv_patch = './csv/food_impact_india.csv'
df = pd.read_csv(csv_patch)

def agregar_fecha_nacimiento(df):
    df['Año_Nacimiento'] = date.today().year - df['Edad']

print(df['Age'],['Año_Nacimiento']) # Se imprime mal, revisar
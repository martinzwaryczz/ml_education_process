# Entrar al siguiente recurso de Kaggle: https://www.kaggle.com/datasets/harry5760/food-impact-on-indians?resource=download leer el csv y llevar el mismo a un gran DataFrame
import pandas as pd

csv_patch = './csv/food_impact_india.csv'

df = pd.read_csv(csv_patch)

print(df)

#  Con el mismo DataFrame buscar que persona tiene la edad máxima, retornar su nombre y apellido
import pandas as pd

data_generica = {
    'Nombre': ['Martín','Carlos','Julian','Gustavo','Laura'],
    'Apellido': ['Gonzales','Gutierrez','Jakboski','Vecchio','Polverini'],
    'Edad': [21, 30, 16, 25, 70],
    'Ciudad de residencia':['Buenos Aires','Catamarca','El Bolson','Tandil','Olavarria']
}
df = pd.DataFrame(data_generica)

def persona_mayor(df) -> str:
    indice_mayor_edad = df["Edad"].idxmax()
    nombre = df.loc[indice_mayor_edad, 'Nombre']
    apellido = df.loc[indice_mayor_edad, 'Apellido']
    return f"La persona con más edad tiene {df["Edad"].max()} años y se llama {nombre} {apellido}"

print(persona_mayor(df))



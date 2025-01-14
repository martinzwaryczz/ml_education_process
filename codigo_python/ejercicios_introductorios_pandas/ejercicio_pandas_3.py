# Con el mismo DataFrame buscar la persona que tiene la edad mínima, retornar su nombre y apellido
import pandas as pd

data_generica = {
    'Nombre': ['Martín','Carlos','Julian','Gustavo','Laura'],
    'Apellido': ['Gonzales','Gutierrez','Jakboski','Vecchio','Polverini'],
    'Edad': [21, 30, 16, 25, 70],
    'Ciudad de residencia':['Buenos Aires','Catamarca','El Bolson','Tandil','Olavarria']
}
df = pd.DataFrame(data_generica)

def persona_menor(df) -> str:
    indice_persona_menor = df["Edad"].idxmin()
    nombre = df.loc[indice_persona_menor, "Nombre"]
    apellido = df.loc[indice_persona_menor, "Apellido"]
    return f"La persona más joven tiene {df["Edad"].min()} y se llama {nombre} {apellido}"

print(persona_menor(df))
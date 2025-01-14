# Mostrar el promedio de edad con la función edad_promedio.
import pandas as pd

data_generica = {
    'Nombre': ['Martín','Carlos','Julian','Gustavo','Laura'],
    'Apellido': ['Gonzales','Gutierrez','Jakboski','Vecchio','Polverini'],
    'Edad': [21, 30, 16, 25, 70],
    'Ciudad de residencia':['Buenos Aires','Catamarca','El Bolson','Tandil','Olavarria']
}
df = pd.DataFrame(data_generica)

def edad_promedio(df) -> str:
    return f"La edad promedio es: {df["Edad"].mean()}"

print(edad_promedio(df))
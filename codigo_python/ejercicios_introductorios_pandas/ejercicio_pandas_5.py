# import pandas as pd
import pandas as pd

data_generica = {
    'Nombre': ['Martín','Carlos','Julian','Gustavo','Laura'],
    'Apellido': ['Gonzales','Gutierrez','Jakboski','Vecchio','Polverini'],
    'Edad': [21, 30, 16, 25, 70],
    'Ciudad de residencia':['Buenos Aires','Catamarca','El Bolson','Tandil','Olavarria']
}
df = pd.DataFrame(data_generica)

dimensiones = df.shape
print(f"Las dimensiones del data frame son {dimensiones}")

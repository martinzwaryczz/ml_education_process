# Crea un diccionario frutas donde las claves sean nombres de frutas y los valores sean sus colores. Recorre el diccionario e imprime cada fruta con su color.

frutas = {
    "manzana":"rojo",
    "banana":"amarillo",
    "durazno":"naranja",
    "kiwi":"verde"
}

for fruta, color in frutas.items():
    print(f"La {fruta} es de {color} color")


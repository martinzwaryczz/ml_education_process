# Crea dos diccionarios, estudiante1 y estudiante2, con claves como nombre, edad y curso. Luego, combina ambos diccionarios en uno solo llamado estudiantes

estudiante1 = {
    "nombre":"Dante",
    "edad":20,
    "curso":"abogacia"
}

estuidante2 = {
    "nombre":"Gonzalo",
    "edad":20,
    "curso":"medicina"
}

# Esto esta mal, crea un diccionario de diccionarios y no es lo pedido en la consigna, lo pedido es crear uno combinado:

estudiantes_mal = {
    "estudiante1": estudiante1,
    "estuidante2": estuidante2
}
print(f"Diccionario de diccioarnios: {estudiantes_mal}")

estudiantes_bien = [estudiante1, estuidante2]

print(f"Nuevo diccionario que combina ambos: {estudiantes_bien}") # Igual esta mal, junta ambos diccionarios pero retorna una lista y yo quiero un nuevo diccionario, quedará pendiente.

class Nota:

    # Constructor del objeto Nota
    def __init__(self, valor_inicial):
        if not self.es_nota_valida(valor_inicial):
            raise ValueError("Nota inválida")
        self.valor_nota = valor_inicial
    

    # Métodos pedidos en la consigna 
    def es_nota_valida(self, valor):
        return 0 <= valor <= 10
    
    def obtener_valor(self):
        return self.valor_nota
    
    def aprobado(self):
        return self.obtener_valor() >= 4
    
    def desaprobado(self):
        return not self.aprobado()
    
    def recuperar(self, nuevo_valor):
        if not self.es_nota_valida(nuevo_valor):
            raise ValueError("Nota inválida")
        if nuevo_valor > self.obtener_valor():
            self.valor_nota = nuevo_valor

# 

if __name__ == "__main__":
    try:
        parcial1 = Nota(8)
        parcial1.recuperar(6)
        print("Nota parcial 1:", parcial1.obtener_valor())
        print("Aprobado:", parcial1.aprobado())
        print("Desaprobado:", parcial1.desaprobado())
        
        parcial2 = Nota(2)
        print("Nota parcial 2:", parcial2.obtener_valor())
        print("¿Está aprobado?:", parcial2.aprobado())
        print("¿Está desaprobado?:", parcial2.desaprobado())
        
        parcial2.recuperar(7)
        print("Recupera")
        print("Nota parcial 2:", parcial2.obtener_valor())
        print("Aprobado:", parcial2.aprobado())
        print("Desaprobado:", parcial2.desaprobado())
        
        # Esto lanzará un error porque 11 no es una nota válida
        examen_final = Nota(11)
    except ValueError as e:
        print(e)
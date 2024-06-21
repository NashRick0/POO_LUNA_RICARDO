class Pajaro:
    def __init__(self, tipo, habitad):
        self.tipo = tipo
        self.habitad = habitad
    
    def volar(self):
        print("FUAA")
    
    def comer(self):
        print("Comiendo")
    
    def cantar(self):
        print("Cantando")

class Zoo:
    def __init__(self, tipo):
        self.tipo = tipo 
        self.pajaros = []
    
    def añadir_pajaro(self, pajaro):
        self.pajaros.append(pajaro)
        print(pajaro.tipo, "añadido al zoo", self.tipo)

    def lista_pajaros(self):
        print(self.tipo, "tiene estos tipos de pajaros: ")
        for pajaro in self.pajaros:
            print(pajaro.tipo)
    
pajaro1 = Pajaro("Canario", "Bosques")
pajaro2 = Pajaro("Avestruz", "Sabanas")

zoo = Zoo("El Oeste")

zoo.añadir_pajaro(pajaro1)
zoo.añadir_pajaro(pajaro2)

zoo.lista_pajaros()
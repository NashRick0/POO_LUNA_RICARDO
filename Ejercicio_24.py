#CLASE PAJARO
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

#CLASE ZOO
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

#CLASE CUIDADOR
class Cuidador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pajaros = []

    def asignar_pajaro(self, pajaro):
        self.pajaros.append(pajaro)
        print(pajaro.tipo, "asignado a", self.nombre)

    def lista_pajaros_cuidados(self):
        print(self.nombre, "cuida de estos pájaros: ")
        for pajaro in self.pajaros:
            print(pajaro.tipo)

    
#OBJETOS PAJAROS

pajaro1 = Pajaro("Canario", "Bosques")
pajaro2 = Pajaro("Avestruz", "Sabanas")

#METODOS ZOO

zoo = Zoo("El Oeste")
zoo.añadir_pajaro(pajaro1)
zoo.añadir_pajaro(pajaro2)
zoo.lista_pajaros()

#CLASE CUIDADOR

cuidador1 = Cuidador("Rick")
cuidador1.asignar_pajaro(pajaro1)
cuidador1.asignar_pajaro(pajaro2)
cuidador1.lista_pajaros_cuidados()
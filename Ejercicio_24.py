#CLASE PAJARO (Principal)
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

    def construir(self, nido):
        print(self.tipo, "esta construyendo un nido de", nido.material)

#CLASE ZOO (Asociacion)
class Zoo:
    def __init__(self, tipo):
        self.tipo = tipo 
        self.pajaros = []
        self.habitads = []
    
    def añadir_pajaro(self, pajaro):
        self.pajaros.append(pajaro)
        print(pajaro.tipo, "añadido al zoo", self.tipo)

    def lista_pajaros(self):
        print(self.tipo, "tiene estos tipos de pajaros: ")
        for pajaro in self.pajaros:
            print(pajaro.tipo)

    def añadir_habitad(self, habitad):
        self.habitads.append(habitad)
        print("Habitad", habitad.tipo, "añadido al zoo", self.tipo)

    def lista_habitads(self):
        print(self.tipo, "tiene estos habitads: ")
        for habitad in self.habitads:
            print(habitad.tipo)

#CLASE CUIDADOR (Agregacion)
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

#CLASE HABITAD (Composicion)
class Habitad:
    def __init__(self, tipo):
        self.tipo = tipo
        self.pajaros = []

    def añadir_pajaro(self, pajaro):
        self.pajaros.append(pajaro)
        print(pajaro.tipo, "añadido al habitad", self.tipo)
    
    def lista_pajaros(self):
        print(self.tipo, "tiene estos tipos de pajaros: ")
        for pajaro in self.pajaros:
            print(pajaro.tipo)

#CLASE PAJARO MENSAJERO (Herencia)

class PajaroMensajero(Pajaro):
    def __init__(self, tipo, habitad, tipo_mensaje):
        super().__init__(tipo, habitad)
        self.tipo_mensaje = tipo_mensaje

    def trabajar(self):
        print(self.tipo, "esta trabajando como pajaro de mensajeria de",
              self.tipo_mensaje)

#CLASE NIDO (Dependencia)

class Nido():
    def __init__(self, material):
        self.material = material

    def describir(self):
        print("El nido esta hecho de", self.material)

    
#METODO PAJARO

pajaro1 = Pajaro("Canario", "Bosques")  #Objeto
pajaro2 = Pajaro("Avestruz", "Sabanas") #Objeto
habitad = Habitad("Bosque")
habitad.añadir_pajaro(pajaro1)

#METODO ZOO

zoo = Zoo("El Oeste") #Objeto
zoo.añadir_pajaro(pajaro1)
zoo.añadir_pajaro(pajaro2)
zoo.lista_pajaros()

zoo.añadir_habitad(habitad)
zoo.lista_habitads()

#METODO CUIDADOR

cuidador1 = Cuidador("Rick") #Objeto
cuidador1.asignar_pajaro(pajaro1)
cuidador1.asignar_pajaro(pajaro2)
cuidador1.lista_pajaros_cuidados()

#METODO PAJARO_MENSAJERO

pajaro_mensaje = PajaroMensajero("Canario", "Bosque", "Cartas") #Objeto
pajaro_mensaje.trabajar()

#METODO NIDO

nido1 = Nido("Paja") #Objeto
pajaro1.construir(nido1)
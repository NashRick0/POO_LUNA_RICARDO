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
    
pajaro1 = Pajaro("Canario", "Bosques")
pajaro2 = Pajaro("Avestruz", "Sabanas")

print(pajaro1.tipo)
print(pajaro2.tipo, pajaro2.habitad)

pajaro1.cantar()
pajaro2.comer()
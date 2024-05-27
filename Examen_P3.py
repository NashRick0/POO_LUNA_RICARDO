edades = [45, 17, 8, 6, 24, 18, 32, 19, 22, 9, 15]

infancia = []
adoles = []
jovenes = []
adultos = []

for edad in edades:
    if edad >= 6 and edad <=11:
        infancia.append(edad)
    elif edad >=12 and edad <=17:
        adoles.append(edad)
    elif edad >=18 and edad <=26:
        jovenes.append(edad)
    elif edad >27:
        adultos.append(edad)

print(f"Infancia: {infancia}")
print(f"Adolescentes: {adoles}")
print(f"Jovenes: {jovenes}")
print(f"Adultos: {adultos}")
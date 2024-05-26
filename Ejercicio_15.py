edades = [12, 17, 24, 16, 35, 18, 22, 8, 22]

mayores = []
menores = []

for edad in edades:
    if edad >= 18:
        mayores.append(edad)
    else:
        menores.append(edad)

print(f"Mayores: {mayores}")
print(f"Menores: {menores}")
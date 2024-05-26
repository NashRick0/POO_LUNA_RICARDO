prom = float(input("Ingrese la 1ra califcacion: "))
prom1 = float(input("Ingrese la 2da califcacion: "))
prom2 = float(input("Ingrese la 3ra califcacion: "))

if prom > prom1 and prom > prom2:
    mayor = prom
elif prom1 > prom and prom1 > prom2:
    mayor = prom1
else:
    mayor = prom2

print(f"Mayor promedio: {mayor}")

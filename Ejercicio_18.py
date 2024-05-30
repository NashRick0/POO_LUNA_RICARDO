print("\nPRODUCTOS")

diccionario = {
    "Coca" : 20,
    "Jabon" : 40,
    "Arroz" : 30
}
des = .30

for prod, precio in diccionario.items():
    print(f"{prod}: {precio}")

print("\nDescuentos")

for prod, precio in diccionario.items():
    diccionario[prod] = diccionario[prod]*(1 - des)
    print(f"{prod}: {diccionario[prod]}")
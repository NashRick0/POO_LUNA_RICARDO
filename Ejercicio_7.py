print("ENVIOS")

peso = float(input("Ingrese el peso en KG de su envio: "))

if peso <= 1:
    print("Tienes que pagar: $50")
elif peso <= 5:
    print("Tienes que pagar: $100")
elif peso <= 10:
    print("Tienes que pagar: $200")
elif peso > 10:
    print("Tienes que pagar: $500")
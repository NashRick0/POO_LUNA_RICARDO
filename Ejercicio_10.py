while True:
    num1 = float(input("Ingrese su 1er número: "))
    num2 = float(input("Ingrese su 2do número: "))

    result = num1+num2
    print(f"La suma es: {result}")

    salir = input("¿Desea salir? (y/n): ")
    if salir == 'y':
        print("Hasta Pronto")
        break

print("AREAS")
print("")

while True:
    print("1.- Cuadrado")
    print("2.- Rectangulo")
    print("3.- Triangulo")
    print("4.- Salir")

    opcion = input("Ingrese la opción deseada (1, 2, 3 o 4): ")

    if opcion == "1":
        print("Seleccionado: CUADRADO")
        lado = float(input("Ingrese lado: "))
        resultC = lado*lado
        print(f"El area es igual a {resultC}")
    elif opcion == "2":
        print("Seleccionado: RECTANGULO")
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        resultR = base*altura
        print(f"El area es igual a {resultR}")
    elif opcion == "3":
        print("Seleccionado: TRIANGULO")
        baseT = float(input("Ingrese la base: "))
        alturaT = float(input("Ingrese la altura: "))
        resultT = (baseT*alturaT)/2
        print(f"El area es igual a {resultT}")
    elif opcion == "4":
        print("Saliendo")
        break
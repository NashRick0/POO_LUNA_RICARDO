while True:
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Salir")

    opcion = input("Ingrese la opción deseada (1, 2, o 3): ")

    if opcion == "1":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fah = (celsius * 9/5) + 32
        print(f"{celsius}°C es igual a {fah}°F")
    elif opcion == "2":
        fah = float(input("Ingrese la temperatura en Fahrenheit: "))
        celsius = (fah - 32) * 5/9
        print(f"{fah}°F es igual a {celsius}°C")
    elif opcion == "3":
        print("Saliendo")
        break
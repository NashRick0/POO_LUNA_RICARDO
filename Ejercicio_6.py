num1 = float(input("Ingrese su 1er numero: "))
num2 = float(input("Ingrese su 2do numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")
elif num2 > num1:
    print(f"El numero {num2} es menor que {num1}")
else:
    print("Los dos numeros son iguales")

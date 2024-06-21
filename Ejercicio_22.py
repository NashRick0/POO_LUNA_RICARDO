def numeros_ingresados():
    a = int(input("Ingresa su 1er numero: "))
    b = int(input("Ingresa su 2do numero: "))
    return a, b

def sumar(a, b):
    suma = a + b
    print(f"La suma de {a} + {b} = {suma}")
    return suma

def restar(a, b):
    resta = a - b
    print(f"La resta de {a} - {b} = {resta}")
    return resta

def multiplicar(a, b):
    producto = a * b
    print(f"El producto de {a} * {b} = {producto}")
    return producto

def dividir(a, b):
    division = a / b
    print(f"La división de {a} / {b} = {division}")
    return division

def opera():
    while True:
        print("\nSelecciona la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")

        op = input("Ingresa tu opción (1, 2, 3, 4): ")

        a, b = numeros_ingresados()
        if op == '1':
            sumar(a, b)
        elif op == '2':
            restar(a, b)
        elif op == '3':
            multiplicar(a, b)
        elif op == '4':
            dividir(a, b)
opera()
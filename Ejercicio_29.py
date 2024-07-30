def abstraccion():
    print("La Abstraccion es la capacidad de un lenguaje de programación para representar y manipular conceptos abstractos en el código.")

def encapsulamiento():
    print("La encapsulación es un mecanismo para reunir datos y métodos dentro de una estructura ocultando la implementación del objeto.")

def herencia():
    print("La herencia permite crear clases que reutilizan, extienden y modifican el comportamiento definido en otras clases.")

def polimorfismo():
    print("El polimorfismo es la capacidad que tienen ciertos lenguajes para hacer que, al enviar el mismo mensaje desde distintos objetos, cada uno de esos pueda responder a ese mensaje de forma distinta.")
    
def menu():
    while True:
        print("\nMenu")
        print("1. Abstraccion")
        print("2. Encapsulamiento")
        print("3. Herencia")
        print("4. Polimorfismo")
        print("5. Salir")

        op = input("Por favor, ingrese una opcion: ")

        if op == "1":
            abstraccion()
        elif op == "2":
            encapsulamiento()
        elif op == "3":
            herencia()
        elif op == "4":
            polimorfismo()
        elif op=="5":
            print("Adios")
            break
        else:
            print("Selecciona dentro del rango")
menu()
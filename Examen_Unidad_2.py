### CLASE VEHICULO ###

class Vehiculo: # Clase que representa un vehiculo
    def __init__(self, marca, modelo, año): # Inicializa vehiculo con los atributos marca, modelo y año
        self.marca = marca
        self.modelo = modelo
        self.año = año 
 
    def info(self): # Muestra Informacion del vehiculo
        print("El vehiculo es de marca", self.marca, "y de modelo", self.modelo, "ultimo año", self.año)

### ASOCIACION (CLASE CLIENTE) ###

class Cliente: # Clase que representa a un cliente
    def __init__(self, nombre): # Inicializa cliente con el atributo nombre y una lista vacia para los vehiculos del cliente
        self.nombre = nombre
        self.vehiculos = []

    def añadir_carro(self, vehiculo): # Añade un vehiculo a la lista del cliente
         self.vehiculos.append(vehiculo)
         print(vehiculo.marca, "añadido a la lista de", self.nombre) # Mensaje de confirmacion

    def lista_vehiculo(self): # Lista de todos los vehiculos del cliente
        print(self.nombre, "tiene estos vehiculos:")
        for vehiculo in self.vehiculos:
            print("Marca", vehiculo.marca, "modelo", vehiculo.modelo, "de año", vehiculo.año)      

### AGREGACION (CLASE MECANICO) ###

class Mecanico: # Clase que representa a un mecanico
    def __init__(self, nombre): # Inicializa macanico con el atributo nombre y una lista vacia con los vehiculos a checar
        self.nombre = nombre
        self.vehiculos_checados = []

    def vehiculo_checar(self, vehiculo): #  Añade un vehiculo a la lista de vehiculos checados por el mecanico
        self.vehiculos_checados.append(vehiculo)
        print(self.nombre, "esta checando al vehiculo marca", vehiculo.marca, "de modelo", vehiculo.modelo)

    def lista_vehiculos_checados(self): # Lista de todos los vehiculos checados por el mecanico
        print(self.nombre, "ha checado los siguientes vehiculos")
        for vehiculo in self.vehiculos_checados:
            print(vehiculo.marca)

### COMPOSICION (CLASE MOTOR) ###

class Motor: # Clase que representa a un motor
    def __init__(self, tipo, cilindro): # Inicializa motor con los atributos tipo y cilindro
        self.tipo = tipo
        self.cilindro = cilindro

    def describir(self, vehiculo): # Describe el motor de un vehiculo
        print(vehiculo.marca, "utiliza un motor", self.tipo, "de", self.cilindro, "cilindros")

### HERENCIA (CLASE VEHICULO DE TRANSPORTE) ###

class VehiculoTransporte(Vehiculo): # Clase que representa a un Vehiculo de Transporte y hereda los atributos de la clase Vehiculo, junto a un nuevo atributo transporte
    def __init__(self, marca, modelo, año, transporte): # Inicializa Vehiculo de Transporte con los atributos heredados
        super().__init__(marca, modelo, año) 
        self.transporte = transporte

    def utilizar(self): # Como se esta utilizando el Vehiculo de Transporte
        print(self.marca, "esta siendo utilizado como vehiculo de transporte", self.transporte)
    
    def describir(self): # Informacion del Vehiculo de Transporte junto con el tipo de servicio
        super().info()
        print("Tipo de transporte", self.transporte)

### DEPENDENCIA (CLASE GAS) ###

class Gas: # Clase que representa a gasolina
    def __init__(self, tipo, cantidad): # Inicializa Gas con los atributos tipo y cantidad
        self.tipo = tipo
        self.cantidad = cantidad
    
    def describir(self, vehiculo): # Informacion sobre el tipo de gasolina que utiliza un vehiculo especifico, asi como la cantidad maxima que soporta
        print(vehiculo.marca, "utiliza gasolina de tipo", self.tipo, "de cantidad maxima", self.cantidad, "litros")

### AGREGACION (CLASE REFACCIONARIA) ###

class Refaccionaria: # Clase que representa a refaccionaria
    def __init__(self, nombre): # Inicializa refaccionaria con el atributo nombre y una lista vacia con las refacciones a añadir
        self.nombre = nombre
        self.refacciones = []

    def añadir_refaccion(self, refaccion): # Añade refacciones al inventario de la refaccionaria
        self.refacciones.append(refaccion)
        print(refaccion.nombre, "añadido al inventario de", self.nombre)

    def lista_refacciones(self): # Muestra la refacciones disponibles en la refaccionaria
        print(self.nombre, "tiene las siguientes refacciones: ")
        for refaccion in self.refacciones:
            print(refaccion.nombre)

### DEPENDENCIA (CLASE PROBLEMA) ###

class Problema: # Clase que representa a un problema en un vehiculo
    def __init__(self, tipo): # Inicializa un problema con su tipo
        self.tipo= tipo
    
    def problem(self, vehiculo): # Describe el problema presentado en un vehiculo
        print("El vehiculo", vehiculo.marca, "tiene un problema de", self.tipo)


def menu(): # Funcion que muestra un menu principal de opciones para gestionar las operaciones
    while True:
        print("\nMenu")
        print("1. Añadir Vehiculo")
        print("2. Lista de Vehiculos")
        print("3. Checar Vehiculo por Mecanico")
        print("4. Lista de Vehiculos checados")
        print("5. Añadir Refaccion")
        print("6. Lista de Refacciones")
        print("7. Checar Gas")
        print("8. Vista Problema")
        print("9. Motor Utilizado")
        print("10. Vehiculo de Transporte")
        print("11. Salir")

        op = input("Por favor, ingrese una opcion: ") # Ingreso de la opcion a escojer

        if op == "1": # Funcion para añadir un vehiculo
            marca = input("Ingrese la marca del vehiculo: ")
            modelo = input("Ingrese el modelo del vehiculo: ")
            año = int(input("Ingrese el año del vehiculo: "))
            vh = Vehiculo(marca, modelo, año)
            cliente.añadir_carro(vh)
        
        if op =="2": # Funcion para ver la lista de los vehiculos del cliente
            cliente.lista_vehiculo()
        
        if op == "3": # Funcion para el ingreso de un vehiculo para el chequeo por parte del mecanico
            marca = input("Ingrese la marca del vehiculo para chequeo: ")
            modelo = input("Ingrese el modelo del vehiculo para chequeo: ")
            año = int(input("Ingrese el año del vehiculo para chequeo: "))
            checar = Vehiculo(marca, modelo, año)
            mecanico.vehiculo_checar(checar)
            
        if op == "4": # Funcion para ver la lista de los vehiculos checados por el mecanico
            mecanico.lista_vehiculos_checados()
        
        if op == "5": # Funcion para añadir una refaccion a la refaccioanaria
            nombre = input("Ingrese el nombre de la refaccion: ")
            rf = Refaccionaria(nombre)
            refaccionaria.añadir_refaccion(rf)
        
        if op == "6": # Funcion para ver la lista de refacciones disponibles en la refaccionaria
            refaccionaria.lista_refacciones()

        if op =="7": # Funcion para describir la gasolina del vehiculo
            tipo = input("Ingrese el tipo de gasolina a utilizar: ")
            cantidad = int(input("Ingrese la cantidad a usar (Litros): "))
            gas_utilizar = Gas(tipo, cantidad)
            gas_utilizar.describir(vehiculo1)
        
        if op == "8": # Funcion para mostrar el tipo de problema en el vehiculo
            tipo = input("Ingrese el tipo de problema que tiene el vehiculo: ")
            prom = Problema(tipo)
            prom.problem(vehiculo2)

        if op =="9": # Funcion para mostrar el tipo de motor que utiliza un vehiculo
            tipo = input("Ingrese el tipo de motor que se utiliza: ")            
            cilindro = input("Ingrese cilindrado: ")
            mot = Motor(tipo, cilindro)
            mot.describir(vehiculo1)

        if op == "10": # Funcion para mostrar el tipo de vehiculo de transporte
            marca = input("Ingrese la marca del vehiculo de transporte: ")
            modelo = input("Ingrese el modelo del vehiculo de transporte: ")
            año = int(input("Ingrese el año del vehiculo de transporte: "))
            transporte = input("Ingrese el tipo de transporte: ")
            vh_trans = VehiculoTransporte(marca, modelo, año, transporte)
            vh_trans.utilizar()

        if op == "11": # Funcion para salir del programa
            print("Saliendo......")
            break



vehiculo1 = Vehiculo("NISSAN", "RTX", 2021) # Objeto de la clase Vehiculo con informacion del mismo
vehiculo2 = Vehiculo("BEAGLE", "AMD", 2022) # Objeto de la clase Vehiculo con informacion del mismo
cliente = Cliente("Rick") # Objeto de la clase Cliente con el nombre del respectivo cliente
cliente.añadir_carro(vehiculo1) # Metodo de la clase Cliente donde añade un vehiculo a la lista
cliente.añadir_carro(vehiculo2) # Metodo de la clase Cliente donde añade un vehiculo a la lista
mecanico = Mecanico("Mario") # Objeto de la clase Mecanico con el nombre del respectivo mecanico
refaccionaria = Refaccionaria("Cancun") # Objeto de la clase Refaccionaria con el nombre de la refaccionaria
menu() # Cierre del Menu
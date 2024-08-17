import os
os.system('cls') # Limpiar la consola

import mysql.connector

# Establecer conexion con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='inv_refa'
)

# Verificar la conexion
if connection.is_connected():
    print("Conexion existosa")

####################### CLIENTE #######################

# Clase para añadir un cliente
class AñadirC():
    def __init__(self, nombre, telefono, correo, direccion):
        # Atributos del cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # Metodo para guardar un nuevo cliente en la base de datos
    def guardarC(self):
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO clientes (nombre, telefono, correo, direccion) VALUES (%s,%s,%s,%s)", 
                           (self.nombre, self.telefono, self.correo, self.direccion ))
            connection.commit()
            print("Cliente Añadido:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para eliminar un cliente
class EliminarC():
    def __init__(self, id_cliente):
        # ID del cliente a eliminar
        self.id_cliente = id_cliente
    
    # Metodo para eliminar un cliente de la base de datos
    def eliminarC(self):
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (self.id_cliente))
            connection.commit()
            print("Cliente con ID:",self.id_cliente, "ha sido eliminado correctamente")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para modificar un cliente
class ModificarC():
    def __init__(self, id_cliente, nombre, telefono, correo, direccion):
        # Atributos del Cliente
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # Metodo para actualizar un cliente en la base de datos
    def modificarC(self):
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE clientes SET nombre = %s, telefono = %s, correo = %s, direccion = %s WHERE id_cliente = %s", 
                           (self.nombre, self.telefono, self.correo, self.direccion, self.id_cliente))
            connection.commit()
            print("Cliente Actualizado:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para buscar un cliente
class BuscarC():
    def __init__(self, nombre):
        # Nombre del cliente a buscar
        self.nombre = nombre
    
    # Metodo para buscar un cliente en la base de datos
    def buscarC(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_cliente, nombre, telefono, correo, direccion FROM clientes WHERE nombre = %s", (self.nombre,))
            resultados = cursor.fetchall()
            clientes = [dict(zip(['id_cliente', 'nombre', 'telefono', 'correo', 'direccion'], fila)) for fila in resultados]
            if not clientes:
                print("Cliente NO disponible")
                return False
            for cliente in clientes:
                print(cliente)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para listar todos los clientes
class ListaC():
    def __init__(self):
        pass

    def mostrarClientes(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM clientes")
            resultadors = cursor.fetchall()
            for fila in resultadors:
                print(fila)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

####################### EMPLEADO #######################

# Clase para añadir un empleado
class AñadirE():
    def __init__(self, nombre, puesto, telefono, correo):
        # Atributos del empleado
        self.nombre = nombre
        self.puesto = puesto
        self.telefono = telefono
        self.correo = correo

    # Metodo para guardar un nuevo empleado en la base de datos
    def guardarE(self):
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO empleados (nombre, puesto, telefono, correo) VALUES (%s,%s,%s,%s)", 
                           (self.nombre, self.puesto, self.telefono, self.correo))
            connection.commit()
            print("Empleado Añadido:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para eliminar un empleado
class EliminarE():
    def __init__(self, id_empleado):
        # ID del empleado a eliminar
        self.id_empleado = id_empleado
    
    # Metodo para eliminar un empleado de la base de datos
    def eliminarE(self):
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM empleados WHERE id_empleado = %s", (self.id_empleado))
            connection.commit()
            print("Empleado con ID:",self.id_empleado, "ha sido eliminado correctamente")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para modificar un empleado
class ModificarE():
    def __init__(self, id_empleado, nombre, puesto, telefono, correo):
        # Atributos del empleado a modificar
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto
        self.telefono = telefono
        self.correo = correo

    # Metodo para actualizar un empleado en la base de datos
    def modificarE(self):
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE empleados SET nombre = %s, puesto = %s, telefono = %s, correo = %s WHERE id_empleado = %s", 
                           (self.nombre, self.puesto, self.telefono, self.correo, self.id_empleado))
            connection.commit()
            print("Empleado Actualizado:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para buscar un empleado
class BuscarE():
    def __init__(self, nombre):
        # Nombre del empleado a buscar
        self.nombre = nombre
    
    # Metodo para buscar un empleado en la base de datos
    def buscarE(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_empleado, nombre, puesto, telefono, correo FROM empleados WHERE nombre = %s", (self.nombre,))
            resultados = cursor.fetchall()
            empleados = [dict(zip(['id_empleado', 'nombre', 'puesto', 'telefono', 'correo'], fila)) for fila in resultados]
            if not empleados:
                print("Empleado NO disponible")
                return False
            for empleado in empleados:
                print(empleado)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para listar todos los empleados
class ListaE():
    def __init__(self):
        pass

    def mostrarEmpleados(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM empleados")
            resultadors = cursor.fetchall()
            for fila in resultadors:
                print(fila)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

####################### REFACCION #######################

# Clase para añadir una refaccion
class AñadirR():
    def __init__(self, nombre, descripcion, precio, id_proveedor):
        # Atributos de la refaccion
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.id_proveedor = id_proveedor

    # Metodo para guardar una nueva refaccion en la base de datos
    def guardarR(self):
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO refacciones (nombre, descripcion, precio, id_proveedor) VALUES (%s,%s,%s,%s)", 
                           (self.nombre, self.descripcion, self.precio, self.id_proveedor))
            connection.commit()
            print("Refaccion Añadida:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para eliminar una refaccion
class EliminarR():
    def __init__(self, id_refaccion):
        # ID de la refaccion a eliminar
        self.id_refaccion = id_refaccion
    
    # Metodo para eliminar una refaccion de la base de datos
    def eliminarR(self):
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM refacciones WHERE id_refaccion = %s", (self.id_refaccion))
            connection.commit()
            print("Refaccion con ID:",self.id_refaccion, "ha sido eliminada correctamente")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para modificar una refaccion
class ModificarR():
    def __init__(self, id_refaccion, nombre, descripcion, precio, id_proveedor):
        # Atributos de la refaccion a modificar
        self.id_refaccion = id_refaccion
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.id_proveedor = id_proveedor

    # Metodo para actualizar una refaccion en la base de datos
    def modificarR(self):
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE refacciones SET nombre = %s, descripcion = %s, precio = %s, id_proveedor = %s WHERE id_refaccion = %s", 
                           (self.nombre, self.descripcion, self.precio, self.id_proveedor, self.id_refaccion))
            connection.commit()
            print("Refaccion Actualizada:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para buscar una refaccion
class BuscarR():
    def __init__(self, nombre):
        # Nombre de la refacción a buscar
        self.nombre = nombre
    
    # Metodo para buscar una refaccion en la base de datos
    def buscarR(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_refaccion, nombre, descripcion, precio, id_proveedor FROM refacciones WHERE nombre = %s", (self.nombre,))
            resultados = cursor.fetchall()
            refacciones = [dict(zip(['id_refaccion', 'nombre', 'descripcion', 'precio', 'id_proveedor'], fila)) for fila in resultados]
            if not refacciones:
                print("Refaccion NO disponible")
                return False
            for refaccion in refacciones:
                print(refaccion)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para listar todas las refacciones
class ListaR():
    def __init__(self):
        pass

    def mostrarRefacciones(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM refacciones")
            resultadors = cursor.fetchall()
            for fila in resultadors:
                print(fila)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

####################### PROVEEDOR #######################

# Clase para añadir un proveedor
class AñadirP():
    def __init__(self, nombre, telefono, correo, direccion):
        # Atributos del proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # Metodo para guardar un nuevo proveedor en la base de datos
    def guardarP(self):
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO proveedores (nombre, telefono, correo, direccion) VALUES (%s,%s,%s,%s)", 
                           (self.nombre, self.telefono, self.correo, self.direccion))
            connection.commit()
            print("Proveedor Añadido:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para eliminar un proveedor en la base de datos
class EliminarP():
    def __init__(self, id_proveedor):
        # ID del proveedor a eliminar
        self.id_proveedor = id_proveedor
    
    # Metodo para eliminar un proveedor de la base de datos
    def eliminarP(self):
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM proveedores WHERE id_proveedor = %s", (self.id_proveedor))
            connection.commit()
            print("Proveedor con ID:",self.id_proveedor, "ha sido eliminado correctamente")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para modificar un proveedor en la base de datos
class ModificarP():
    def __init__(self, id_proveedor, nombre, telefono, correo, direccion):
        # Atributos del proveedor a modificar
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # Metodo para actualizar un proveedor de la base de datos
    def modificarP(self):
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE proveedores SET nombre = %s, telefono = %s, correo = %s, direccion = %s WHERE id_proveedor = %s", 
                           (self.nombre, self.telefono, self.correo, self.direccion, self.id_proveedor))
            connection.commit()
            print("Proveedor Actualizado:",self.nombre)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para buscar un proveedor en la base de datos
class BuscarP():
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Metodo para consultar un proveedor de la base de datos
    def buscarP(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_proveedor, nombre, telefono, correo, direccion FROM proveedores WHERE nombre = %s", (self.nombre,))
            resultados = cursor.fetchall()
            proveedores = [dict(zip(['id_proveedor', 'nombre', 'telefono', 'correo', 'direccion'], fila)) for fila in resultados]
            if not proveedores:
                print("Proveedor NO disponible")
                return False
            for proveedor in proveedores:
                print(proveedor)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para listar todos los proveedores
class ListaP():
    def __init__(self):
        pass

    def mostrarProveedores(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM proveedores")
            resultadors = cursor.fetchall()
            for fila in resultadors:
                print(fila)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

####################### VENTA #######################

# Clase para añadir una venta
class AñadirV():
    def __init__(self, id_cliente, id_empleado, fecha_venta, total):
        # Atributos de la venta
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.fecha_venta = fecha_venta
        self.total = total

    # Metodo para guardar una nueva venta en la base de datos
    def guardarV(self):
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO ventas (id_cliente, id_empleado, fecha_venta, total) VALUES (%s,%s,%s,%s)", 
                           (self.id_cliente, self.id_empleado, self.fecha_venta, self.total))
            connection.commit()
            print("Venta Realizada:",self.fecha_venta)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para modificar una venta
class ModificarV():
    def __init__(self, id_venta, id_cliente, id_empleado, fecha_venta, total):
        # Atributos de la venta para modificar
        self.id_venta = id_venta
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.fecha_venta = fecha_venta
        self.total = total

    # Metodo para actualizar una venta de la base de datos
    def modificarV(self):
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE ventas SET id_cliente = %s, id_empleado = %s, fecha_venta = %s, total = %s WHERE id_venta = %s",
                           (self.id_cliente, self.id_empleado, self.fecha_venta, self.total, self.id_venta))
            connection.commit()
            print("Venta actualizada")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para buscar una venta
class BuscarV():
    def __init__(self, id_venta):
        self.id_venta = id_venta
    
    # Metodo para consultar una venta de la base de datos
    def buscarV(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_venta, id_cliente, id_empleado, fecha_venta, total FROM ventas WHERE id_venta = %s", (self.id_venta,))
            resultados = cursor.fetchall()
            ventas = [dict(zip(['id_venta', 'id_cliente', 'id_empleado', 'fecha_venta', 'total'], fila)) for fila in resultados]
            if not ventas:
                print("Venta NO disponible")
                return False
            for venta in ventas:
                print(venta)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Clase para listar todos las ventas
class ListaV():
    def __init__(self):
        pass

    def mostrarVentas(self):
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM ventas")
            resultadors = cursor.fetchall()
            for fila in resultadors:
                print(fila)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

####################### MENU PRINCIPAL #######################

def menu():
    while True:
        print("\n --> Menú Principal <-- ")
        print("1. Gestionar Clientes")
        print("2. Gestionar Empleados")
        print("3. Gestionar Refacciones")
        print("4. Gestionar Ventas")
        print("5. Gestionar Proveedores")
        print("6. Salir")

        op = input("Ingrese una opción: ")

        if op == "1":
            menu_clientes()
        elif op == "2":
            menu_empleados()
        elif op == "3":
            menu_refacciones()
        elif op == "4":
            menu_ventas()
        elif op == "5":
            menu_proveedores()
        elif op == "6":
            if connection.is_connected():
                connection.close()
                print("Saliendo...")
                break
        else:
            print("Selecciona dentro del RANGO")

####################### MENU CLIENTES #######################
def menu_clientes():
    while True:
        print("\n -> Menú Clientes <-")
        print("1. Añadir")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Buscar")
        print("5. Mostrar Todos")
        print("6. Volver al Menú Principal")

        op = input("Ingrese una opción: ")

        if op == "1":
            nombre = input("Ingrese Nombre: ")
            telefono = input("Ingrese Teléfono: ")
            correo = input("Ingrese Correo: ")
            direccion = input("Ingrese Dirección: ")
            nuevoC = AñadirC(nombre, telefono, correo, direccion)
            nuevoC.guardarC()
        elif op == "2":
            lista_clientes = ListaC()
            lista_clientes.mostrarClientes()
            cliente_id = int(input("Ingrese ID para eliminar: "))
            eliminar_cliente = EliminarC(cliente_id)
            eliminar_cliente.eliminarC()
        elif op == "3":
            lista_clientes = ListaC()
            lista_clientes.mostrarClientes()
            cliente_id = int(input("Seleccione ID para modificar un dato: "))
            nombre = input("Ingrese nuevo Nombre: ")
            telefono = input("Ingrese nuevo Teléfono: ")
            correo = input("Ingrese nuevo Correo: ")
            direccion = input("Ingrese nueva Dirección: ")
            modi_cliente = ModificarC(cliente_id, nombre, telefono, correo, direccion)
            modi_cliente.modificarC()
        elif op == "4":
            nombre = input("Ingrese nombre para buscar: ")
            busc_cliente = BuscarC(nombre)
            busc_cliente.buscarC()
        elif op == "5":
            lista_clientes = ListaC()
            lista_clientes.mostrarClientes()
        elif op == "6":
            break
        else:
            print("Selecciona dentro del RANGO")

####################### MENU EMPLEADOS #######################
def menu_empleados():
    while True:
        print("\n -> Menú Empleados <-")
        print("1. Añadir")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Buscar")
        print("5. Mostrar Todos")
        print("6. Volver al Menú Principal")

        op = input("Ingrese una opción: ")

        if op == "1":
            nombre = input("Ingrese Nombre: ")
            puesto = input("Ingrese Puesto: ")
            telefono = input("Ingrese Teléfono: ")
            correo = input("Ingrese Correo: ")
            nuevoE = AñadirE(nombre, puesto, telefono, correo)
            nuevoE.guardarE()
        elif op == "2":
            lista_empleados = ListaE()
            lista_empleados.mostrarEmpleados()
            empleado_id = int(input("Ingrese ID para eliminar: "))
            eliminar_empleado = EliminarE(empleado_id)
            eliminar_empleado.eliminarE()
        elif op == "3":
            lista_empleados = ListaE()
            lista_empleados.mostrarEmpleados()
            empleado_id = int(input("Seleccione ID para modificar un dato: "))
            nombre = input("Ingrese nuevo Nombre: ")
            puesto = input("Ingrese nuevo Puesto: ")
            telefono = input("Ingrese nuevo Teléfono: ")
            correo = input("Ingrese nuevo Correo: ")
            modi_empleado = ModificarE(empleado_id, nombre, puesto, telefono, correo)
            modi_empleado.modificarE()
        elif op == "4":
            nombre = input("Ingrese nombre para buscar: ")
            busc_empleado = BuscarE(nombre)
            busc_empleado.buscarE()
        elif op == "5":
            lista_empleados = ListaE()
            lista_empleados.mostrarEmpleados()
        elif op == "6":
            break
        else:
            print("Selecciona dentro del RANGO")

####################### MENU REFACCIONES #######################
def menu_refacciones():
    while True:
        print("\n -> Menú Refacciones <-")
        print("1. Añadir")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Buscar")
        print("5. Mostrar Todos")
        print("6. Volver al Menú Principal")

        op = input("Ingrese una opción: ")

        if op == "1":
            nombre = input("Ingrese Nombre: ")
            descripcion = input("Ingrese Descripción: ")
            precio = float(input("Ingrese Precio: "))
            proveedor_id = int(input("Ingrese ID del Proveedor: "))
            nuevaR = AñadirR(nombre, descripcion, precio, proveedor_id)
            nuevaR.guardarR()
        elif op == "2":
            lista_refacciones = ListaR()
            lista_refacciones.mostrarRefacciones()
            refaccion_id = int(input("Ingrese ID para eliminar: "))
            eliminar_refaccion = EliminarR(refaccion_id)
            eliminar_refaccion.eliminarR()
        elif op == "3":
            lista_refacciones = ListaR()
            lista_refacciones.mostrarRefacciones()
            refaccion_id = int(input("Seleccione ID para modificar un dato: "))
            nombre = input("Ingrese nuevo Nombre: ")
            descripcion = input("Ingrese nueva Descripción: ")
            precio = float(input("Ingrese nuevo Precio: "))
            proveedor_id = int(input("Ingrese nuevo ID del Proveedor: "))
            modi_refaccion = ModificarR(refaccion_id, nombre, descripcion, precio, proveedor_id)
            modi_refaccion.modificarR()
        elif op == "4":
            nombre = input("Ingrese nombre para buscar: ")
            busc_refaccion = BuscarR(nombre)
            busc_refaccion.buscarR()
        elif op == "5":
            lista_refacciones = ListaR()
            lista_refacciones.mostrarRefacciones()
        elif op == "6":
            break
        else:
            print("Selecciona dentro del RANGO")

####################### MENU VENTAS #######################
def menu_ventas():
    while True:
        print("\n -> Menú Ventas <-")
        print("1. Añadir")
        print("2. Modificar")
        print("3. Buscar")
        print("4. Mostrar Todos")
        print("5. Volver al Menú Principal")

        op = input("Ingrese una opción: ")

        if op == "1":
            cliente_id = int(input("Ingrese ID del Cliente: "))
            empleado_id = int(input("Ingrese ID del Empleado: "))
            fecha = input("Ingrese Fecha (YYYY-MM-DD): ")
            total = float(input("Ingrese Total: "))
            nuevaV = AñadirV(cliente_id, empleado_id, fecha, total)
            nuevaV.guardarV()
        elif op == "2":
            lista_ventas = ListaV()
            lista_ventas.mostrarVentas()
            venta_id = int(input("Seleccione ID para modificar un dato: "))
            cliente_id = int(input("Ingrese nuevo ID del Cliente: "))
            empleado_id = int(input("Ingrese nuevo ID del Empleado: "))
            fecha = input("Ingrese nueva Fecha (YYYY-MM-DD): ")
            total = float(input("Ingrese nuevo Total: "))
            modi_venta = ModificarV(venta_id, cliente_id, empleado_id, fecha, total)
            modi_venta.modificarV()
        elif op == "3":
            lista_ventas = ListaV()
            lista_ventas.mostrarVentas()
            venta_id = int(input("Ingrese ID para buscar: "))
            busc_venta = BuscarV(venta_id)
            busc_venta.buscarV()
        elif op == "4":
            lista_ventas = ListaV()
            lista_ventas.mostrarVentas()
        elif op == "5":
            break
        else:
            print("Selecciona dentro del RANGO")

####################### MENU PROVEEDORES #######################
def menu_proveedores():
    while True:
        print("\n -> Menú Proveedores <-")
        print("1. Añadir")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Buscar")
        print("5. Mostrar Todos")
        print("6. Volver al Menú Principal")

        op = input("Ingrese una opción: ")

        if op == "1":
            nombre = input("Ingrese Nombre: ")
            telefono = input("Ingrese Teléfono: ")
            correo = input("Ingrese Correo: ")
            direccion = input("Ingrese Dirección: ")
            nuevoP = AñadirP(nombre, telefono, correo, direccion)
            nuevoP.guardarP()
        elif op == "2":
            lista_proveedores = ListaP()
            lista_proveedores.mostrarProveedores()
            proveedor_id = int(input("Ingrese ID para eliminar: "))
            eliminar_proveedor = EliminarP(proveedor_id)
            eliminar_proveedor.eliminarP()
        elif op == "3":
            lista_proveedores = ListaP()
            lista_proveedores.mostrarProveedores()
            proveedor_id = int(input("Seleccione ID para modificar un dato: "))
            nombre = input("Ingrese nuevo Nombre: ")
            telefono = input("Ingrese nuevo Teléfono: ")
            correo = input("Ingrese nuevo Correo: ")
            direccion = input("Ingrese nueva Dirección: ")
            modi_proveedor = ModificarP(proveedor_id, nombre, telefono, correo, direccion)
            modi_proveedor.modificarP()
        elif op == "4":
            nombre = input("Ingrese nombre para buscar: ")
            busc_proveedor = BuscarP(nombre)
            busc_proveedor.buscarP()
        elif op == "5":
            lista_proveedores = ListaP()
            lista_proveedores.mostrarProveedores()
        elif op == "6":
            break
        else:
            print("Selecciona dentro del RANGO")

# Finalizacion
if __name__ == "__main__":
    menu() # Cierra Menu
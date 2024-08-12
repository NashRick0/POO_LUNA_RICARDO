import os
os.system('cls')

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escolares'
)
cursor = connection.cursor()

if connection.is_connected():
    print("Conexion existosa a la BD")

def insertar():
    query = "INSERT INTO alumnos (nombre, edad, direccion, id_maestro) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, ("Pepe", 18, "Su casa", 3))
    connection.commit()
    print("Alumno insertado exitosamente")
insertar()

def mostrar():
    cursor.execute("SELECT * FROM alumnos")
    result = cursor.fetchall()
    for row in result:
        print(row)
mostrar()

def borrar():
    mostrar()
    id = input("ingresar el id a borrar:")
    query = "DELETE FROM alumnos WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Alumno eliminado exitosamente")
borrar()

def actualizar():
    mostrar()
    id = input("ingresar el id a modificar:")
    query = "UPDATE alumnos SET nombre = %s, edad = %s, direccion = %s, id_maaestro = %s WHERE id = %s"
    cursor.execute(query, ("Ricardo", 21, "Mario's House", 3, id))
    connection.commit()
    print("Alumno actualizado exitosamente")
actualizar()

if connection.is_connected():
    connection.close()
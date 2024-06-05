# Comienza la lista para las tareas
lista = [["numero de tarea", "tarea"]]
# Variables
x = 0 # Controla el ciclo
z = 1
n = 0 # Contador para el numero de tareas

# Bucle principal que repite hasta que el usuario decida salir
while x != 3:
    # Menu Principal
    print("----creador de tareas----")
    print("1. Agregar tarea")
    print("2. Terminar tarea")
    print("3. salir")
    y = int(input()) # Lee la entrada y la convierte a entero
    x = y # Actuliza la variable

    # Opcion 1: Agregar Tareas
    if y == 1:
        n = n + 1 # Incrementa el contador
        tarea = str(input("escribe la tarea: ")) # Descripcion de la tarea
        lista.append([n,tarea]) # Añade la tarea a la nueva lista

    # Opcion 2: Terminar Tareas
    if y == 2:
        # Verifica si hay tareas en la lista
        if len(lista) == 1:
            print("No hay tareas para eliminar.")
        else:
            # Muestra todas las tareas disponibles en la lista
            for tarea in lista:
                if tarea[0] != "numero de tarea": 
                    print(f'{tarea[0]} "{tarea[1]}"')
            try:
                # Pide el numero de la tarea para eliminarla
                num_eliminar = int(input("elije el numero que quieres remover: "))
                tarea_encontrada = False
                for tarea in lista:
                    if tarea[0] == num_eliminar:
                        lista.remove(tarea) # Elimina la tarea 
                        tarea_encontrada = True
                        break
                # Si no encuentra la tarea especificada, informa del error
                if not tarea_encontrada:
                    print("Numero de tarea no encontrado.")
                    # Muestra error si el usuario no ingresa un numero valido
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número.")
# Finaliza bucle e imprime todas las tareas disponibles
for tarea in lista:
    print(f'{tarea[0]} "{tarea[1]}"')


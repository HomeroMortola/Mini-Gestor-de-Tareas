import json
import os

def cargar_lista_to_do():
    if os.path.exists("To_do.json"):
        with open("To_do.json", "r") as file:
            return json.load(file)
    else:
        return []

#definimos la funcion para agregar nuevas tareas
def agregar_tarea(dic_leer):
    nombre = input("Ingrse el nombre de la tarea a añadir: ")
    tarea = input("Ingrese la tarea: ")
    
    i = len(dic_leer)+1         
    
    #creamos un dicionario para suvir
    dic_suvir = {
        "id" : i,
        "nombre" : nombre,
        "tarea" : tarea,
        "completada" : "no"
    }

    #subimos el dicionario
    dic_leer.append(dic_suvir)
    with open("To_do.json", "w") as file:
        json.dump(dic_leer, file, indent=4)
    
    print("\n---Tarea agregada---\n")

#definimos la funcion para marcar tareas como completadas
def marcar_terminacion(dic_leer):
    n_tarea = int(input("Qué tarea desea marcar como completada?"))
    n_tarea -=1
    dic_leer[n_tarea]["completada"]= "si"
    
    with open("To_do.json", "w") as file:
        json.dump(dic_leer, file, indent=4)
    
    print("\n---Tarea marcada---\n")

#definimos la funcion para elminar tareas
def eliminar_tarea(dic_leer):
    n_tarea = int(input("Que tarea desea eliminar?"))
    n_tarea-=1
    del dic_leer[n_tarea]
   
    #guardamos la lista actualisada
    with open("To_do.json", "w") as file:
        json.dump(dic_leer, file, indent=4)

    print("\n---Tarea eliminada---\n")

print("Bienvenido al ToDo manager")
dic_leer = cargar_lista_to_do()
while True:
    print ("¿Que le gusria hacer?\n1-mostrar las tareas\n2-agregar una taerea\n3-marcar tarea como terminada\n4-eliminar una tarea\n5-salir del programa")
    
    opcion = int(input(":"))
    match opcion:
        case 1:
            print(json.dumps(dic_leer, indent=4))
        case 2:
            agregar_tarea(dic_leer)
        case 3:
            marcar_terminacion(dic_leer)
        case 4:
            eliminar_tarea(dic_leer)
        case 5:
            print("saliendo...")
            break
        case _:
            print("Entrada inválida")








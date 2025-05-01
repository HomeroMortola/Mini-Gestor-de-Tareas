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
    
    #creamos un dicionaria para suvir
    dic_suvir = {
        "id" : i,
        "nombre" : nombre,
        "tarea" : tarea,
        "completada" : "no"
    }

    #suvimos el dicionario
    dic_leer.append(dic_suvir)
    with open("To_do.json", "w") as file:
        json.dump(dic_leer, file, indent=4)
    

print("Bienvenido al ToDo manger")



dic_leer = cargar_lista_to_do()
while True:
    print ("¿Que le gusria hacer?")
    
    opcion = int(input(":"))
    match opcion:
        case 1:
            print(json.dumps(dic_leer, indent=4))
        case 2:
            agregar_tarea(dic_leer)
        case 5:
            print("saliendo...")
            break
        case _:
            print("Entrada invalido")








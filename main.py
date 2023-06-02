from funciones import *
import csv
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://informatica1:bio123@informatica1.wwqyiub.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server

client = MongoClient(uri)

mybd = client["informatica1"]
mycol = mybd["equipos"]
mycol2 = mybd["responsables"]
mycol3 = mybd["ubicaciones"]



print("_______________________________\n|Bienvenido a la base de datos|\n| de mantenimiento de equipos |\n|         Biomedicos          |\n|_____________________________|")
print("¿Que deseas realizar el dia de hoy?\n")


while True:

    men= menu_principal(str(input("Seleccione que tipo de informacion desea gestionar.\n1. Equipos\n2. Responsables\n3. Ubicaciones\n4. Salir\n-->  ")))

    if men == "1":
        print("Seleccione que desea realizar\n-----------------------------")
        equ= menus_secundarios1(str(input("1. Ingresar un nuevo equipo en forma manual\n2. Ingresar un nuevo equipo en forma automática\n3. Actualizar la información de un equipo\n4. Buscar un equipo\n5. Ver la información de todos los equipos almacenados\n6. Eliminar un equipo\n7. Volver al menú principal\n-->  ")))

        if equ== "1":

            serial = str(input("Ingrese el serial del equipo:\n"))
            num_activo = variable_num(str(input("Ingrese el numero de activo:\n")))
            nom_equipo = nombres(str(input("Ingrese el nombre del equipo:\n")))
            marca = nombres(str(input("Ingrese la marca del equipo:\n")))
            cod_ubicacion = codigos_num(str(input("Ingrese un codigo de ubicacion contemplado entre 7 y 10 cifras:\n")))
            cod_responsable = codigos_num(str(input("Ingrese codigo del responsable contemplado entre 7 y 10 cifras:\n")))

            if serial and num_activo and nom_equipo and marca and cod_ubicacion and cod_responsable:
                dir = {
                    "serial":serial,
                    "numero de activo":num_activo,
                    "nombre del equipo":nom_equipo,
                    "marca":marca,
                    "codigo de ubicacion":cod_ubicacion,
                    "codigo del responsable":cod_responsable
                }
                mycol.insert_one(dir)
                print("¡La informacion ha sido guardada exitosamente!")
            
            salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            while salir !="1" and salir !="2":
                print("El parametro ingresado no es valido")
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            if salir =="1":
                print("Ha salido correctamente") 
                break
            if salir =="2":
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass



        elif equ== "2":

            print("ddd")

        #actualizar informacion
        elif equ== "3":
            
            num_activo= input("Ingresar el numero de activo del equipo que desea actualizar: ")
            buscar= mycol.find_one({"numero de activo":num_activo})

            if buscar:
                serial = str(input("Ingrese el serial del equipo:\n"))
                nom_equipo = nombres(str(input("Ingrese el nombre del equipo:\n")))
                marca = nombres(str(input("Ingrese la marca del equipo:\n")))
                cod_ubicacion = codigos_num(str(input("Ingrese un codigo de ubicacion contemplado entre 7 y 10 cifras:\n")))
                cod_responsable = codigos_num(str(input("Ingrese codigo del responsable contemplado entre 7 y 10 cifras:\n")))
            
                
                
                mycol.update_one({
                    "numero de activo":num_activo},
                    {"$set":{
                        "serial":serial,
                        "nombre del equipo":nom_equipo,
                        "marca":marca,
                        "codigo de ubicacion":cod_ubicacion,
                        "codigo del responsable":cod_responsable}
                    })
                print("Equipo actualizado")
            
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass
            
            else: 
                print("El equipo no se encuentra registrado\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass



        elif equ== "4":

            num_activo= input("Ingresar el numero de activo del equipo que desea buscar: ")
            bus= mycol.find_one({"numero de activo":num_activo})

            if bus:
                
                print("El equipo ha sido encontrado\n")
                print(bus)

                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass


            else:
                print("El equipo no se encuentra registrado\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass




        elif equ== "5":
            for y in mycol.find():
                print(y)
                print("__________________________________________________________________________________________________________________________________________________________________________________________________________________")
            salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            while salir !="1" and salir !="2":
                print("El parametro ingresado no es valido")
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            if salir =="1":
                print("Ha salido correctamente") 
                break
            if salir =="2":
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass


        elif equ== "6":
            num_activo= input("Ingresar el numero de activo del equipo que desea eliminar:\n")
            buscar= mycol.find_one({"numero de activo":num_activo})
            if buscar:
                mycol.delete_one({"numero de activo":num_activo})
                print("¡El equipo ha sido eliminado correctamente!")
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass
            else:
                print("El numero de activo no existe en la base de datos\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass
            
        elif equ== "7":
            print("¡Bienvenido nuevamente al menu principal!\n")
            pass
    


#MENU 2 RESPONSABLES------------------------------------------------------------------------------------
    elif men == "2":
        print("Seleccione que desea realizar\n-----------------------------")
        res= menus_secundarios2(str(input("1. Ingresar un nuevo responsable\n2. Ver la información de todos los responsables almacenados \n3. Actualizar la información de un responsable\n4. Eliminar un responsable\n5.Buscar un responsable \n5. Volver al menú principal\n-->  ")))

#menu para ingresar responsables
        if res== "1":
            cod_responsable = codigos_num(str(input("Ingrese codigo del responsable contemplado entre 7 y 10 cifras:\n")))
            nombre = nombres(str(input("Ingrese su primer nombre:\n")))
            apellido = nombres(str(input("Ingrese su primer apellido:\n")))
            id = variable_num(str(input("Ingrese su numero de documento de identidad:\n")))
            cargo = nombres(str(input("Ingrese su cargo actual:\n")))

            if cod_responsable and nombre and apellido and id and cargo:
                dir = {
                    "codigo del responsable":cod_responsable,
                    "nombre":nombre,
                    "apellido":apellido,
                    "ID":id,
                    "cargo":cargo,
                }
                mycol2.insert_one(dir)
                print("¡La informacion ha sido guardada exitosamente!\n")

 
#menu para ver datos
        elif res== "2":
            for y in mycol2.find():
                print(y)

                print("__________________________________________________________________________________________________________________________________________________________________________________________________________________")
            
            salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            while salir !="1" and salir !="2":
                print("El parametro ingresado no es valido")
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            if salir =="1":
                print("Ha salido correctamente") 
                break
            if salir =="2":
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass
        
#actualizar informacion de los responsables
        elif res== "3":
            cod_responsable= input("Ingresar el numero de activo del equipo que desea actualizar: ")
            buscar= mycol2.find_one({"codigo del responsable":cod_responsable})

            if buscar:
                nombre = nombres(str(input("Ingrese su primer nombre:\n")))
                apellido = nombres(str(input("Ingrese su primer apellido:\n")))
                id = variable_num(str(input("Ingrese su numero de documento de identidad:\n")))
                cargo = nombres(str(input("Ingrese su cargo actual:\n")))
                
                
                mycol2.update_one({
                    "codigo del responsable":cod_responsable},
                    {"$set":{
                        "nombre":nombre,
                        "apellido":apellido,
                        "ID":id,
                        "cargo":cargo}
                    })
                print("Datos del responsable actualizados!\n")
            
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass
                
            else: 
                print("El responsable no se encuentra registrado\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass

#ELIMINAR DATOS
        elif res== "4":
            cod_responsable= input("Ingresar el numero del responsable que desea eliminar:\n")
            buscar= mycol2.find_one({"codigo del responsable":cod_responsable})

            if buscar:
                mycol2.delete_one({"codigo del responsable":cod_responsable})
                print("¡El responsable ha sido eliminado correctamente!\n")

                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass
            else:
                print("El codigo del responsable no existe en la base de datos\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass
            
#volver al menu
        elif res== "5":
            print("¡Bienvenido nuevamente al menu principal!\n")
            pass
        




# MENU 3 UBICACIONES--------------------------------------------------------------------------------------------
    elif men == "3":
        print("Seleccione que desea realizar\n-----------------------------")
        ubi= menus_secundarios3(str(input("1. Ingresar una nueva ubicacion\n2. Ver la información de todas las ubicaciones almacenadas \n3. Actualizar la información de una ubicacion\n4. Eliminar una ubicacion de un equipo\n5.Buscar una ubicacion \n6. Volver al menú principal\n-->  ")))

        if ubi== "1":
            cod_ubicacion = codigos_num(str(input("Ingrese un codigo de ubicacion contemplado entre 7 y 10 cifras:\n")))
            nom_ubicacion = nombres(str(input("Ingrese el nombre de la ubicacion:\n")))
            piso_ubicacion = variable_num(str(input("Ingrese el piso donde se encuentra ubicada:\n")))

            if cod_ubicacion and nom_ubicacion and piso_ubicacion:
                dir = {
                    "codigo de ubicacion":cod_ubicacion,
                    "nombre de la ubicacion":nom_ubicacion,
                    "piso de la ubicacion":piso_ubicacion
                }
                mycol3.insert_one(dir)
                print("¡La informacion ha sido guardada exitosamente!")
            salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            while salir !="1" and salir !="2":
                print("El parametro ingresado no es valido")
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            if salir =="1":
                print("Ha salido correctamente") 
                break
            if salir =="2":
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass


        elif ubi== "2":
            for y in mycol3.find():
                print(y)
                print("______________________________________________________________________________________________________________________________________________________________")
            salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            while salir !="1" and salir !="2":
                print("El parametro ingresado no es valido")
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
            if salir =="1":
                print("Ha salido correctamente") 
                break
            if salir =="2":
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass


        elif ubi== "3":
            cod_ubicacion= input("Ingresar el codigo de ubicacion que desea actualizar: ")
            buscar= mycol3.find_one({"codigo de ubicacion":cod_ubicacion})

            if buscar:
                nom_ubicacion = nombres(str(input("Ingrese el nombre de la ubicacion:\n")))
                piso_ubicacion = variable_num(str(input("Ingrese el piso donde se encuentra ubicada:\n")))
            
        
                mycol3.update_one({
                    "codigo de ubicacion":cod_ubicacion},
                    {"$set":{
                        "nombre de la ubicacion":nom_ubicacion,
                        "piso de la ubicacion":piso_ubicacion}
                        })
                print("Ubicacion actualizada")
            
                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass
            
            else: 
                print("La ubicacion no se encuentra registrada\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass


        elif ubi== "4":
            cod_ubicacion= input("Ingresar el codigo de ubicacion que desea eliminar:\n")
            buscar= mycol3.find_one({"codigo de ubicacion":cod_ubicacion})

            if buscar:
                mycol3.delete_one({"codigo de ubicacion":cod_ubicacion})
                print("¡El equipo ha sido eliminado correctamente!")

                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass
            else:
                print("El codigo de ubicacion no existe en la base de datos\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass


        elif ubi== "5":
            cod_ubicacion= input("Ingresar el codigo de la ubicacion que desea buscar: ")
            bus= mycol3.find_one({"codigo de ubicacion":cod_ubicacion})

            if bus:
                print("La ubicacion ha sido encontrada\n")
                print(bus)

                salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                while  salir !="1" and salir !="2":
                    print("El parametro ingresado no es valido")
                    salir = str(input("Desea salir ahora ?\n1.SI\n2.NO\n"))
                if salir =="1":
                    print("Ha salido correctamente") 
                    break
                if salir =="2":
                    print("¡Bienvenido nuevamente al menu principal!\n")
                    pass


            else:
                print("La ubicacion no se encuentra registrada\n")
                print("¡Bienvenido nuevamente al menu principal!\n")
                pass
        
        elif ubi =="6":
            print("¡Bienvenido nuevamente al menu principal!\n")
            pass



    elif men == "4":
        print("Ha salido correctamente")   
        break
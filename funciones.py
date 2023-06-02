#funcion de validacion del menu principal
def menu_principal(menu):
    try:
        while menu != "1" and menu != "2" and menu !="3" and menu!="4":
            print("El parametro ingresado no es valido. por favor ingrese nuevamente\n")
            menu= str(input("Seleccione que tipo de informacion desea gestionar.\n1. Equipos\n2. Responsables\n3. Ubicaciones\n4. Salir\n-->  "))
        return menu
    except:
        print("Parametros incorrectos")


#FUNCIONES DE VALIDACION DE LOS MENUS SECUNDARIOS-----------------------------

#funcion de validacion menu equipos
def menus_secundarios1(menu_e):
    try:
            while menu_e!= "1" and menu_e!= "2" and menu_e!="3" and menu_e!="4" and menu_e!="5" and menu_e!="6" and menu_e!="7":
                print("El parametro ingresado no es valido. por favor ingrese nuevamente\n")
                menu_e =(str(input("1. Ingresar un nuevo equipo en forma manual\n2. Ingresar un nuevo equipo en forma automática\n3. Actualizar la información de un equipo\n4. Buscar un equipo\n5. Ver la información de todos los equipos almacenados\n6. Eliminar un equipo\n7. Volver al menú principal\n-->  ")))
            return menu_e
    except:
         print("Parametros incorrectos ")



#funcion de validacion menu responsables
def menus_secundarios2(menu_r):
    try:
            while menu_r!= "1" and menu_r!= "2" and menu_r!="3" and menu_r!="4" and menu_r!="5" and menu_r!="6" :
                print("El parametro ingresado no es valido. por favor ingrese nuevamente\n")
                menu_r = str(input("1. Ingresar un nuevo responsable\n2. Ver la información de todos los responsables almacenados \n3. Actualizar la información de un responsable\n4. Eliminar un responsable\n5.Buscar un responsable \n6. Volver al menú principal\n-->  "))
            return menu_r
    except:
         print("Parametros incorrectos")



#funcion de validacion menu ubicaciones
def menus_secundarios3(menu_u):
    try:
            while menu_u!= "1" and menu_u!= "2" and menu_u!="3" and menu_u!="4" and menu_u!="5" and menu_u!="6" :
                print("El parametro ingresado no es valido. por favor ingrese nuevamente\n")
                menu_u = str(input("1. Ingresar una nueva ubicacion\n2. Ver la información de todas las ubicaciones almacenadas \n3. Actualizar la información de una ubicacion\n4. Eliminar ubicaciones de un equipo\n5.Buscar una ubicacion \n6. Volver al menú principal\n-->  "))
            return menu_u
    except:
         print("Parametros incorrectos")
     


#FUNCIONES DE VALIDACION DE VARIABLES------------------------

#funcion de validacion de una variable numerica
def variable_num(numero):
    try:
        while numero.isnumeric() == False:
               print("La variable ingresada debe ser de tipo numerico")
               numero = str(input("Ingrese nuevamente el valor:\n"))
        return numero
    except:
         print("Parametros invalidos")

#funcion de validacion de un codigo numerico
def codigos_num(codigos):
    try:
        while codigos.isnumeric() == False or len(str(codigos)) > 10 or len(str(codigos)) < 7:
               print("¡El codigo debe estar comprendido entre 7 y 10 cifras y debe ser de tipo numerico!")
               codigos = str(input("Ingrese nuevamente el codigo:\n"))
        return codigos
    except:
         print("Parametros invalidos")

#funcion de validacion de variables alfabeticas
def nombres(nombre):
    try:
        while nombre.isalpha() == False:
              print("El dato ingresado no es valido. no debe contener espacios, numeros o caracteres especiales")
              nombre = str(input("Ingrese nuevamente un dato valido:\n"))
        return nombre
    except:
         print("Parametros invalidos")


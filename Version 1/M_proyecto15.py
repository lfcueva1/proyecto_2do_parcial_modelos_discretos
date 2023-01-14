import os
import re
import getpass

def validar_numeros_enteros():
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es entero, si lo que se ingresó no es un numero
    entero entonces el usuario tendra que volver a ingresar un numero
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        numero : int
    '''
    #mientras sea verdadero se ingresara un dato en la variable numero, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el usuario debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            numero=int(input())
            #rempemos ciclo repetitivo
            break
        #en caso de que no se haya ingresado un numero entero se imprimira un mensaje diciendo que no se ingreso un enetero
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero
def menu():
    #Doy la bienvenida e imprimo las opcines del menu
    print("BIENVENIDO AL LOGIN")
    print("1. Loguearse")
    print("2. Registrarse")
    print("3. Salir")
    print("Elija una opcion: ",end="")
    #elijo una opcion
    opcion=validar_numeros_enteros()
    #valido si mi opcion se encuentra dentro dle rango
    while(opcion<1 or opcion>3):
        print("Ingrese numeros dentro del rango: ")
        opcion=validar_numeros_enteros()
    #retorno el valor de la opcion
    return opcion
def verificar_si_contrasena_es_segura(contrasena):
    '''
    Funcion que verifica si una contraseña es segura

    Parametros:
    ------------
        contrasena : str
    Retorna:
    ------------
        1 : int
        2 : int
    '''
    numero=False
    mayuscula = False
    minuscula = False
    caracter_especial = False 
    #si la contraseña tiene menos de 10 caracteres no es valida
    if(len(contrasena)<10):
        print("Su contraseña no es segura")
        return 2
    #compruebo si la contraseña contiene al menos un numero
    for caracter in contrasena:
        if caracter.isdigit():
            numero = True
    #comprueba si la contraseña tiene al menos una letra en mayuscula
    for caracter in contrasena:
        if caracter.isupper():
            mayuscula= True
    #comprueba si la contraseña tiene al menos una letra en minuscula
    for caracter in contrasena:
        if caracter.islower():
            minuscula= True   
    #compruebo si la contraseña tiene al menos un caracter especial
    if re.search("[^a-zA-Z0-9]",contrasena):
        caracter_especial= True 
    #si hay un numero, una mayuscula, una minuscula y un caracter especial entonces la contraseña sera valida
    if(numero==True and mayuscula==True and minuscula==True and caracter_especial==True):
        print("Su contraseña es segura")
        return 1
    #caso contrario no es segura
    else:
        print("Su contraseña no es segura")
        return 2
def validar_formato_de_un_correo_electronico(correo_electronico):
    '''
    Funcion que valida si el formato de un correo electronico ingresado por teclado es valido

    Parametros:
    ------------
        correo_electronico : str 
    Retorna:
    ------------
        1 : int
        2 : int
    '''
    #Formato de correo aceptable : nombreaaaa @ xxxmail .com
    patron_correo=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    #buscamos si el formato es una subcadena de la cadena correo_electronico, la funcion imprime un mensaje de si es valido o no el formato
    #del correo
    if re.search(patron_correo, correo_electronico):
        print("El formato del correo electronico es valida")
        return 1
    else:
        print("El formato del correo electronico no es valida")
        return 2
def registrarse():
    '''
    Funcion que permite a un usuario registrarse con su correo electronico(que sea valido) y una contraseña(que sea segura)
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #creo un archivo llamado "correos_registrados.txt", si ya esta creado el codigo no generara otro archivo
    filename = "correos_registrados.txt"
    if os.path.isfile(filename):
        print("El archivo ya ha sido creado.")
    else:
        open(filename, "w").close()
    #ingreso un correo electronico
    correo_electronico=input("Ingrese un correo electronico: ")
    #verifico si el correo ingresado tiene un formato correcto
    correo_valido=validar_formato_de_un_correo_electronico(correo_electronico)
    #si el formato del correo electronico es incorrecto, intentaremos de nuevo
    while correo_valido != 1:
        print("Correo invalido,intente de nuevo")
        correo_electronico=input("Ingrese un correo electronico: ")
        correo_valido=validar_formato_de_un_correo_electronico(correo_electronico)
    #En la variable guardo todas los correos que ya esten generados en el txt
    with open("correos_registrados.txt", "r") as archivo:
        correos_en_archivo = archivo.readlines()
    #abron un ciclo repetitivo
    while True:
        #declaro la variable existe como bandera
        existe = False
        #recorremos los correos guardados en el archivo
        for n in correos_en_archivo:
            #si ya existe un correo similar a lo que se intenta ingresar la variable existe cambiara a verdadero
            if n.strip() == correo_electronico:
                existe = True
                #rompemos ciclo repetitivo
                break
        #si el correo ya existe entonces no se guardara en el archivo
        if existe:
            print("Este correo ya se encuentra en el archivo")
            os.system("pause")
            #rompemos el primer ciclo repetivio
            return 0
        #si el correo es diferente
        else:
            #abrimos el archivo y guardamos el correo generado
            with open("correos_registrados.txt", "a") as archivo:
                archivo.write(correo_electronico + "\n")
            print("Correo guardado en el archivo.")
            #rompemos el primer ciclo repetivio
            break
    
    #creo un archivo llamado "correos_registrados.txt", si ya esta creado el codigo no generara otro archivo
    filename = "contraseñas_registradas.txt"
    if os.path.isfile(filename):
        print("El archivo ya ha sido creado.")
    else:
        open(filename, "w").close()
    #ingreso una contraseña
    contrasena=input("Ingrese una contraseña: ")
    #verifico si la contraseña es segura
    contrasena_valida=verificar_si_contrasena_es_segura(contrasena)
    #si la contraseña no es segura intentaremos de nuevo
    if(contrasena_valida!=1):
        print("Su contraseña no es segura,intente de nuevo")
        contrasena=input("Ingrese una contraseña: ")
        contrasena_valida=verificar_si_contrasena_es_segura(contrasena)

    #En la variable guardo todas los correos que ya esten generados en el txt
    with open("contraseñas_registradas.txt", "r") as archivo:
        contrasenas_en_archivo = archivo.readlines()
    
    #abrimos el archivo y guardamos el correo generado
    with open("contraseñas_registradas.txt", "a") as archivo:
        archivo.write(contrasena + "\n")
    print("Contraseña guardado en el archivo.")
    #pausamos el codigo
    os.system("pause")

def loguearse():
    '''
    Funcion que permite al usuario loguear con su correo y contraseña

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        return 0
    '''
    #Ingreso correo y contraseña para loguear al usuario
    correo = input("Ingrese su correo: ")
    print("Los caracteres de la contraseña seran invisibles para su seguridad")
    contrasena = getpass.getpass("Ingrese una contraseña:")
    #guardos los correos del txt en una lista respectivamente
    with open("correos_registrados.txt","r") as correos:
        correos_registrados = correos.readlines()
    with open("contraseñas_registradas.txt", "r") as contrasenas:
        contrasenas_registradas = contrasenas.readlines()
    #limpio los caracteres /n de los correos y contraseñas
    correos_limpios = [corr.strip() for corr in correos_registrados]
    contrasenas_limpias = [contra.strip() for contra in contrasenas_registradas]
    #busco la posicion del correo ingresado
    
    #verificio si los correos y contrseñas se encuentran dentro del txt para poder loguearse correctamente o se imprimira un mensaje de error
    for i in range(len(correos_limpios)):
        if(correos_limpios[i]==correo and contrasenas_limpias[i]==contrasena):
            print("SU LOGUEO A SIDO CORRECTO")
            os.system("pause")
            return(0)
    else:
        #si no hay coincidencias el logueo no es correcto
        print("Correo o contraseña incorrectas")
    os.system("pause")

if __name__ == '__main__':
    while True:
        #limpio pantalla
        os.system("cls")
        #imprimo el menu
        opcion=menu()
        #loguearse
        if(opcion==1):
            loguearse()
        #registrarse
        if(opcion==2):
            registrarse()
        #salir del programa
        if(opcion==3):
            break

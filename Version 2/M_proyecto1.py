import os
"""
Programa donde se ingresa los dos nombres y el primer apellido de una persona la cual segun lo ingresado por
teclado generara un correo electronico, este programa tiene las validacion correspondientes y la mas importante 
la cual es que si hay un correo que ya se encuentra denttro del txt tendra que generar otro que no sea igual

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.1
"""
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
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero

def leer_variables():
    '''
    Funcion que lee los dos nombres y apellido del usuario y los valida
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        primer_nombre : str
        segundo_nombre : str
        primer_apellido : str
    '''
    #Ingreso primer nombre y lo valido
    while True:
        primer_nombre = input("Ingrese su primer nombre: ")
        tiene_numero = False
        for caracter in primer_nombre:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("El primer nombre no debe contener números. Intente de nuevo.")
        else:
            break
    #ingreso segundo nombre y lo valido
    while True:
        segundo_nombre = input("Ingrese su segundo nombre: ")
        tiene_numero = False
        for caracter in segundo_nombre:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("El segundo nombre no debe contener números. Intente de nuevo.")
        else:
            break     
    #ingreso primer apellido y lo valido   
    while True:
        primer_apellido = input("Ingrese su primer apellido: ")
        tiene_numero = False
        for caracter in primer_apellido:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("El primer apellido no debe contener números. Intente de nuevo.")
        else:
            break 
    #retorno las variables ingresadas
    return primer_nombre,segundo_nombre,primer_apellido
def cambiar_a_minusculas(primer_nombre,segundo_nombre,primer_apellido):
    '''
    Funcion que transforma todos los caracteres de los dos nombres y el apellido en minusculas

    Parametros:
    ------------
        primer_nombre : str
        segundo_nombre : str
        primer_apellido : str
    Retorna:
    ------------
        primer_nombre : str
        segundo_nombre : str
        primer_apellido : str

    '''
    #Convierto los dos nombres y el apellido en minusculas con la funcion .lower()
    primer_nombre=primer_nombre.lower()
    segundo_nombre=segundo_nombre.lower()
    primer_apellido=primer_apellido.lower()
    #retorno los nombres y apellidos en minusculas
    return (primer_nombre,segundo_nombre,primer_apellido)

def generar_correos_electronicos(primer_nombre,segundo_nombre,primer_apellido):
    '''
    Funcion que genera correos electronicos 
    Parametros:
    ------------
        primer_nombre : str
        segundo_nombre : str
        primer_apellido : str
    Retorna:
    ------------
        correo : cadena (se guarda en el txt "correos_modelos_discretos.txt")
    segun los dos nombres y apellido
    '''
    filename = "correos_modelos_discretos.txt"
    if os.path.isfile(filename):
        print("El archivo ya ha sido creado.")
    else:
        open(filename, "w").close()
    #preguntar si el correo electronico es educativo
    print("El correo electronico es educativo?")
    print("1. Si")
    print("2. No")
    institucional=validar_numeros_enteros()
    #validar el rango de las opciones
    while(institucional<1 or institucional>2):
        print("Solo ingrese numeros dentro del rango: ",end="")
        institucional=validar_numeros_enteros()
    if(institucional==1):
        print("Cual sera el dominio institucional del correo electronico")
        dominio=input("Ingrese el dominio:")
        #genero el correo en la variable correo_electronico
        correo_electronico= primer_nombre[0]+segundo_nombre[0]+primer_apellido+"@"+dominio+".edu.ec"
    elif(institucional==2):
        print("Cual sera el dominio del correo electronico")
        print("Ejemplos: hotmal, gmail, yahoo")
        dominio=input("Ingrese el dominio:")
        #genero el correo en la variable correo_electronico
        correo_electronico= primer_nombre[0]+segundo_nombre[0]+primer_apellido+"@"+dominio+".ec"

    #En la variable guardo todas los correos que ya esten generados en el txt
    with open("correos_modelos_discretos.txt", "r") as archivo:
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
            print("Este nombre ya se encuentra en el archivo, ingrese otro nombre.")
            #rompemos el primer ciclo repetivio
            break
        #si el correo es diferente
        else:
            #abrimos el archivo y guardamos el correo generado
            with open("correos_modelos_discretos.txt", "a") as archivo:
                archivo.write(correo_electronico + "\n")
            print("Correo guardado en el archivo.")
            #rompemos el primer ciclo repetivio
            break

if __name__ == '__main__':
    #Ingreso los dos nombres y apellido del usuario
    primer_nombre,segundo_nombre,primer_apellido=leer_variables()
    #los dos nombres y apellido del usuario se convertiran en letras minusculas
    primer_nombre,segundo_nombre,primer_apellido=cambiar_a_minusculas(primer_nombre,segundo_nombre,primer_apellido)
    #generamos los correos segun los dos nombres y apellido
    generar_correos_electronicos(primer_nombre,segundo_nombre,primer_apellido)
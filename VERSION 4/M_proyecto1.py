#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#Libreria que me ayuda con el manejo de archivos
import os
#libreria que me ayuda con la complejidad del tiempo
import big_o
"""
Programa donde se ingresa los dos nombres y el primer apellido de una persona la cual segun lo ingresado por
teclado generara un correo electronico, este programa tiene las validacion correspondientes y la mas importante 
la cual es que si hay un correo que ya se encuentra denttro del txt tendra que generar otro que no sea igual

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
#@profile
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
#@profile
def leer_variables():
    '''
    Funcion que lee los dos nombres y apellido del usuario y los valida
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        nombres_apellido : lista
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
            nombres_apellido.append(primer_nombre)
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
            nombres_apellido.append(segundo_nombre)
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
            nombres_apellido.append(primer_apellido)
            break 
    #retorno la lista
    return nombres_apellido
#@profile
def cambiar_a_minusculas(nombres_apellido):
    '''
    Funcion que transforma todos los caracteres de los dos nombres y el apellido en minusculas

    Parametros:
    ------------
        nombres_apellido : lista
    Retorna:
    ------------
        nombres_apellido : lista

    '''
    #Convierto los dos nombres y el apellido en minusculas con la funcion .lower()
    nombres_apellido[0]=nombres_apellido[0].lower()
    nombres_apellido[1]=nombres_apellido[1].lower()
    nombres_apellido[2]=nombres_apellido[2].lower()
    #retorno los nombres y apellidos en minusculas
    return (nombres_apellido)
#@profile
def generar_correos_electronicos(nombres_apellido):
    '''
    Funcion que genera correos electronicos 
    Parametros:
    ------------
        nombres_apellido : lista
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
        
        correo_electronico= nombres_apellido[0][0]+nombres_apellido[1][0]+nombres_apellido[2]+"@"+dominio+".edu.ec"
    elif(institucional==2):
        print("Cual sera el dominio del correo electronico")
        print("Ejemplos: hotmal, gmail, yahoo")
        dominio=input("Ingrese el dominio:")
        #genero el correo en la variable correo_electronico
        correo_electronico= nombres_apellido[0][0]+nombres_apellido[1][0]+nombres_apellido[2]+"@"+dominio+".ec"

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
    nombres_apellido=[]
    #imprimo la bienvenida y las indicaciones
    print("BIENVENIDO AL GENERADOR DE CORREOS ELECTRONICOS")
    print("Indicaciones:")
    print("      Para generar un correo electronico necesitaremos que ingrese su primer y segundo nombre y su apellido")
    print("      Una vez ingresado sus datos el programa automaticamente generara su correo electronico y lo guardara en un txt")
    print("      Si el programa detecta que el correo que ingreso ya se encuentra en uso debera ingresar otro")
    #pauso el codigo
    os.system("pause")
    #Ingreso los dos nombres y apellido del usuario
    nombres_apellido=leer_variables()
    #los dos nombres y apellido del usuario se convertiran en letras minusculas
    nombres_apellido=cambiar_a_minusculas(nombres_apellido)
    #generamos los correos segun los dos nombres y apellido
    generar_correos_electronicos(nombres_apellido)

    '''
    print("BIG_O:")
    positive_int_generator = lambda n: nombres_apellido
    best, others= big_o.big_o(generar_correos_electronicos,positive_int_generator)
    print(best)
    '''
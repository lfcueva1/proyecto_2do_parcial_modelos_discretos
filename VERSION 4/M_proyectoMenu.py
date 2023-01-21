#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que uso para obtener la tecla presionada sin necesidad de presionar Enter
import msvcrt
#funcion que uso para pausar y limpiar pantalla
import os
#funcion que uso para llamar a otros .py en este programa
import subprocess 
#funcion que me sirve para imprimir la complejidad de tiempo
import big_o
#importo libreria para ayudar a calcular la complejidad de espacio
import sys

import re
#importo las fucniones de los proyecto para calcular su big_o
from M_proyecto1 import generar_correos_electronicos
from M_proyecto2 import palabras_repetidas_ingresadas
from M_proyecto3 import encriptar_cadena,desencriptar_cadena
from M_proyecto4 import palabras_que_empiecen_con_la_letra_ingresada
from M_proyecto5 import ordenar_cadena
from M_proyecto6 import validar_placa_automovil,validar_placa_moto
from M_proyecto7 import verificar_si_contrasena_es_segura
from M_proyecto8 import anagrama
from M_proyecto9 import validar_formato_de_un_correo_electronico
from M_proyecto10 import verificar_si_una_cadena_tiene_solo_letras
from M_proyecto11 import reemplazar_palabra_en_cadena_ingresada
from M_proyecto12 import validacion_cedula
from M_proyecto13 import diferencia_de_cadenas
from M_proyecto14 import palabra_mas_larga
from M_proyecto15 import registrarse,loguearse
from M_proyecto16 import encontrar_palabras_con_tamaño_especifico
def getch():
    '''
    Funcion que obtiene la tecla presionada sin necesidad de presionar Enter, permitiendo al usuario seleccionar las opciones del 
    menú utilizando las flechas del teclado y presionando Enter para confirmar la selección.

    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        msvcrt.getch()
    '''
    return msvcrt.getch()

def menu():
    '''
    Funcion que permite iterar en el menu de opcines

    Parametros:
        Esta funcion no tiene parametros
    
    Retorna:
        choice : int
    '''
    #escribo todas las opciones que tendra el menu dentro de una lista
    options = ["1. Generar correos electrónicos", "2. Ingresar una oración e imprima la palabras que se repiten", "3. Encriptar y desencriptar una cadena",
    "4. Ingresar varias palabras e imprimir las palabras que empiecen por la letra ingresada por el usuario","5. Ingresar una cadena de caracteres y ordenarla en orden ascendente",
    "6. Validación de placa de un auto y una moto ecuatoriana","7. Validar que una contraseña sea segura","8. Determinar si una cadena dada es un anagrama de otra cadena dada",
    "9. verificar si una cadena cumple con un formato de correo electrónico","10. Determine si una cadena contiene solo letras.","11. Cambiar una palabra específica en una frase con otra palabra",
    "12. Validar una cédula ecuatoriana","13. Encontrar la diferencia entre dos cadenas dada en términos de caracteres añadidos, eliminados y cambiados",
    "14. Ingresar una oración en una cadena e imprimir la palabra más larga","15. Registrarse y loguearse con un correo",
    "16. Imprimir todas las palabras en una cadena dada que tienen una cantidad específica de numero de caracteres","17. Big_o","18. Complejidad de espacio","19. Salir"]

    
    #declarar variable igual a cero
    choice = 0
    #formo un bucle infinito que se encarga de mostrar el menu principal
    while True:
        #limpio pantalla
        os.system("cls")
        print("MENU DE OPCIONES")
        #ciclo repetitivo que permite iterar entre las opcines del menu
        for i, option in enumerate(options):
            if i == choice:
                print("> " + option)
            else:
                print("  " + option)
        #obtiene la tecla presionada por el usuario y se almacena en la variable "key".
        key = getch()
        #verifica si la tecla presionada es "w" y si la opción seleccionada actual es mayor a 0, si es así, la opcion seleccionada se decrementa en 1.
        if key == b"w" and choice > 0:
            choice -= 1
        #verifica si la tecla presionada es "s" y si la opción seleccionada actual es menor al tamaño de las opciones - 1, si es así, la opcion seleccionada se incrementa en 1.
        elif key == b"s" and choice < len(options) - 1:
            choice += 1
        #verifica si la tecla presionada es "Enter" y si es así, se sale del bucle y se devuelve la opcion seleccionada.
        elif key == b"\r":
            return choice
def menu2():
    '''
    Funcion que permite iterar en el menu de opcines

    Parametros:
        Esta funcion no tiene parametros
    
    Retorna:
        choice : int
    '''
    #escribo todas las opciones que tendra el menu dentro de una lista
    options2 = ["1. Generar correos electrónicos", "2. Ingresar una oración e imprima la palabras que se repiten", "3. Encriptar y desencriptar una cadena",
    "4. Ingresar varias palabras e imprimir las palabras que empiecen por la letra ingresada por el usuario","5. Ingresar una cadena de caracteres y ordenarla en orden ascendente",
    "6. Validación de placa de un auto y una moto ecuatoriana","7. Validar que una contraseña sea segura","8. Determinar si una cadena dada es un anagrama de otra cadena dada",
    "9. verificar si una cadena cumple con un formato de correo electrónico","10. Determine si una cadena contiene solo letras.","11. Cambiar una palabra específica en una frase con otra palabra",
    "12. Validar una cédula ecuatoriana","13. Encontrar la diferencia entre dos cadenas dada en términos de caracteres añadidos, eliminados y cambiados",
    "14. Ingresar una oración en una cadena e imprimir la palabra más larga","15. Registrarse y loguearse con un correo",
    "16. Imprimir todas las palabras en una cadena dada que tienen una cantidad específica de numero de caracteres","17. Salir"]
    #declarar variable igual a cero
    choice2 = 0
    #formo un bucle infinito que se encarga de mostrar el menu principal
    while True:
        #limpio pantalla
        os.system("cls")
        print("MENU DE OPCIONES")
        #ciclo repetitivo que permite iterar entre las opcines del menu
        for i, option2 in enumerate(options2):
            if i == choice2:
                print("> " + option2)
            else:
                print("  " + option2)
        #obtiene la tecla presionada por el usuario y se almacena en la variable "key".
        key2 = getch()
        #verifica si la tecla presionada es "w" y si la opción seleccionada actual es mayor a 0, si es así, la opcion seleccionada se decrementa en 1.
        if key2 == b"w" and choice2 > 0:
            choice2 -= 1
        #verifica si la tecla presionada es "s" y si la opción seleccionada actual es menor al tamaño de las opciones - 1, si es así, la opcion seleccionada se incrementa en 1.
        elif key2 == b"s" and choice2 < len(options2) - 1:
            choice2 += 1
        #verifica si la tecla presionada es "Enter" y si es así, se sale del bucle y se devuelve la opcion seleccionada.
        elif key2 == b"\r":
            return choice2
def caratula():
    #pinta en color amarillo
    print(chr(27)+"[1;33m")
    print("             ██████████████████████████████████████████████████████████")
    print("             ██                                                      ██")
    print("             ██                      ████████                        ██")
    print("             ██                   ███        ███                     ██")
    print("             ██                 ██████████████████                   ██")
    print("             ██               ██   ██        ██   ██                 ██")
    print("             ██               ██████████████████████                 ██")
    print("             ██               ██   ██        ██   ██                 ██")
    print("             ██               ██████████████████████                 ██")
    print("             ██                 ██ ██        ██ ██                   ██")
    print("             ██                   ██████████████                     ██")
    print("             ██                      ████████                        ██")
    print("             ██                                                      ██")
    print("             ██████████████████████████████████████████████████████████")
    print("           ██  ███  ███   ███   ███   ███    ███    ███    ███    ███  ██")
    print("         ██                                                              ██")
    print("       ██  ███   ███   ███   ███    ███    ███    ███    ███    ███   ███  ██")
    print("     ██                                                                      ██")
    print("   ██               ███    ███     ████████████     ███    ███                 ██")
    print("  ██                                                                            ██")
    print("   ██████████████████████████████████████████████████████████████████████████████")
    print(chr(27)+"[1;32m")
    print("   ██    ██    ██    ████████ ████████ ████████ ")
    print("   ███  ███  ██  ██  ██          ██    ██        Si puedes imaginarlo")
    print("   ██ ██ ██ ██    ██ ██  ████    ██    ██             puedes programarlo")
    print("   ██ ██ ██ ████████ ██    ██    ██    ██      ")
    print("   ██    ██ ██    ██ ████████ ████████ ████████")
    print("")
    print("                                    ████████ ████████ ██       ██       ████████ ████████ ████████")
    print("                                    ██       ██    ██ ██       ██       ██       ██       ██      ")
    print("                                    ██       ██    ██ ██       ██       ████████ ██  ████ ████████")
    print("                                    ██       ██    ██ ██       ██       ██       ██    ██ ██      ")
    print("                                    ████████ ████████ ████████ ████████ ████████ ████████ ████████")
    print("Sistema informatico estudiantil(UNIVERSIDADES,INSTITUTOS,COLEGIOS Y ESCUELAS)")

    
if __name__ == '__main__': 
    #limpio pantalla
    os.system("cls")
    #imprimo la caratula de la empresa
    caratula()
    #pauso el codigo
    os.system("pause")

    while True:
        print("\033[1;32m"+"")#color verde
        opcion = menu()
        if opcion == 0:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto1
            subprocess.call(["python", "./M_proyecto1.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 1:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto2
            subprocess.call(["python", "./M_proyecto2.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 2:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto3
            subprocess.call(["python", "./M_proyecto3.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 3:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto4
            subprocess.call(["python", "./M_proyecto4.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 4:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto5
            subprocess.call(["python", "./M_proyecto5.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 5:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto6
            subprocess.call(["python", "./M_proyecto6.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 6:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto7
            subprocess.call(["python", "./M_proyecto7.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 7:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto8
            subprocess.call(["python", "./M_proyecto8.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 8:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto9
            subprocess.call(["python", "./M_proyecto9.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 9:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto10
            subprocess.call(["python", "./M_proyecto10.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 10:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto11
            subprocess.call(["python", "./M_proyecto11.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 11:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto12
            subprocess.call(["python", "./M_proyecto12.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 12:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto13
            subprocess.call(["python", "./M_proyecto13.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 13:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto14
            subprocess.call(["python", "./M_proyecto14.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 14:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto15
            subprocess.call(["python", "./M_proyecto15.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 15:
            #imprime las letras en color cian
            print("\033[1;36m")
            #limpio pantalla
            os.system("cls")
            #llamo al programa M_proyecto16
            subprocess.call(["python", "./M_proyecto16.py"])
            #pauso pantalla
            os.system("pause")
        if opcion == 16:
            while True:
                print("\033[1;33m"+"")#color verde
                opcion2 = menu2()
                if opcion2 == 0:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    oracion_palabras= "hola mundo"
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: oracion_palabras
                    best, others= big_o.big_o(palabras_repetidas_ingresadas,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 1:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #Imprimo big_o
                    oracion_palabras= "hola mundo"
                    print("BIG_O:")
                    positive_int_generator = lambda n: oracion_palabras
                    best, others= big_o.big_o(palabras_repetidas_ingresadas,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 2:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #Imprimo big_o
                    oracion_palabras= "hola mundo"
                    #imprimimos el big_o de las funciones principales
                    cadena="hola mundo"
                    print("BIG_O de encriptar cadena:")
                    positive_int_generator = lambda n: cadena
                    best, others= big_o.big_o(encriptar_cadena,positive_int_generator)
                    print(best)
                    cadena_encriptada="8 15 12 1  13 21 14 4 15"
                    print("BIG_O de desencriptar cadena:")
                    positive_int_generator = lambda n: cadena_encriptada
                    best, others= big_o.big_o(desencriptar_cadena,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 3:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #Imprimo big_o
                    cadena_letra=["hola mundo","h"]
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadena_letra
                    best, others= big_o.big_o(palabras_que_empiecen_con_la_letra_ingresada,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 4:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #Imprimo big_o
                    cadena="abkjds"
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadena
                    best, others= big_o.big_o(ordenar_cadena,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 5:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #Imprimo big_o
                    placaAuto="PQR-4568"
                    placaMoto="AE456A"
                    print("BIG_O validar_placa_automovil:")
                    positive_int_generator = lambda n: placaAuto
                    best, others= big_o.big_o(validar_placa_automovil,positive_int_generator)
                    print(best)
                    print("BIG_O validar_placa_moto:")
                    positive_int_generator = lambda n: placaMoto
                    best, others= big_o.big_o(validar_placa_moto,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 6:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    contrasena="ABCdef@1234"
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: contrasena
                    best, others= big_o.big_o(verificar_si_contrasena_es_segura,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 7:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cadenas_1_y_2=["hola","aloh"]
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadenas_1_y_2
                    best, others= big_o.big_o(anagrama,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 8:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    correo_electronico="luisfernando@gmail.com"
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: correo_electronico
                    best, others= big_o.big_o(validar_formato_de_un_correo_electronico,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 9:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cadena="pablito"
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadena
                    best, others= big_o.big_o(verificar_si_una_cadena_tiene_solo_letras,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 10:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cadenas_palabras=["hola mundo","hola","adios"]
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadenas_palabras
                    best, others= big_o.big_o(reemplazar_palabra_en_cadena_ingresada,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 11:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cedula="1751486950"
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cedula
                    best, others= big_o.big_o(validacion_cedula,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 12:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cadenas_1_2=["Hola","ahloa"]
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadenas_1_2
                    best, others= big_o.big_o(diferencia_de_cadenas,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 13:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cadena="Hola como estas amigo"
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadena
                    best, others= big_o.big_o(palabra_mas_larga,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 14:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cadena="Hola como estas amigo"
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadena
                    best, others= big_o.big_o(palabra_mas_larga,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 15:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    cadena_nletra=["hola mundo",2]
                    #Imprimo big_o
                    print("BIG_O:")
                    positive_int_generator = lambda n: cadena_nletra
                    best, others= big_o.big_o(encontrar_palabras_con_tamaño_especifico,positive_int_generator)
                    print(best)
                    #pauso pantalla
                    os.system("pause")
                if opcion2 == 16:
                    break
        if opcion == 17:
            while True:
                print("\033[1;35m"+"")#color verde
                opcion3 = menu2()
                if opcion3 == 0:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    nombres_apellido=["luis","fernando","cueva"]
                    #calculo la complejidad de espacio
                    @profile
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
                    @profile
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
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 1:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def palabras_repetidas_ingresadas(oracion_palabras):
                        '''
                        Funcion que imprime las palabras repetidas de la oracion que se ingresó por teclado

                        Parametros:
                        ------------
                            oracion_palabras : str
                        Retorna:
                        ------------
                            Esta funcion no retorna ningun tipo de dato

                        '''
                        #Creo un diccionario para guardar las palabras y sus conteos
                        conteos = {}
                        #declaro esta lista apra gaurdar las palabras que se repiten en la cadena 
                        repetidas=[]
                        #Separo oración en una lista 
                        palabras = oracion_palabras.split()
                        # Recorro las palabras y contar las repeticiones
                        for palabra in palabras:
                            if palabra in conteos:
                                conteos[palabra] += 1
                            else:
                                conteos[palabra] = 1
                        #si hay una palabra que se repite se la agregara a la lista de palabras repetidas 
                        for palabra, conteo in conteos.items():
                            if conteo > 1:
                                #agrego la palbra que se repite a la lista repetidas
                                repetidas.append(palabra)
                        #retornamos las palabras que se repiten
                        return repetidas
                    oracion_palabras="hola mundo"
                    before = sys.getsizeof(palabras_repetidas_ingresadas)
                    result = palabras_repetidas_ingresadas(oracion_palabras)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 2:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    print("Funcion cadena encriptada")
                    @profile
                    def encriptar_cadena(cadena):
                        """
                        Funcion que encripta una cadena ingresada por teclado reemplazando cada letra con un numero

                        Parametros:
                        ------------
                            cadena : str
                        Retorna:
                        ------------
                            cadena_encriptada : str
                        """
                        # Crea un diccionario para almacenar las letras y sus números correspondientes
                        encriptacion = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26',' ':'27'}
                        # Crea una variable para almacenar la cadena encriptada
                        cadena_encriptada = ""
                        # Recorre cada caracter de la cadena y reemplaza con el número correspondiente
                        for caracter in cadena:
                            if caracter.isalpha():
                                cadena_encriptada += encriptacion[caracter.lower()]+' '
                            else:
                                cadena_encriptada+=caracter
                        return cadena_encriptada
                    @profile
                    def desencriptar_cadena(cadena_encriptada):
                        """
                        Funcion que desencripta una cadena  reemplazando cada numero por una letra

                        Parametros:
                        ------------
                            cadena_encriptada : str
                        Retorna:
                        ------------
                            cadena_desencriptada : str
                        """
                        # Crea un diccionario para almacenar los numeros y sus letras correspondientes
                        desencriptacion = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10':'j', '11':'k', '12':'l', '13':'m', '14':'n', '15':'o', '16':'p', '17':'q', '18':'r', '19':'s', '20':'t', '21':'u', '22':'v', '23':'w', '24':'x', '25':'y', '26':'z','27':' '}
                        # Crea una variable para almacenar la cadena desencriptada
                        cadena_desencriptada = ""
                        # Recorre cada caracter de la cadena y reemplaza con la letra correspondiente
                        for caracter in cadena_encriptada.split():
                            if caracter.isnumeric():
                                cadena_desencriptada += desencriptacion[caracter]
                            else:
                                cadena_desencriptada += caracter
                        return cadena_desencriptada
                    cadena="hola mundo"
                    before = sys.getsizeof(encriptar_cadena)
                    result = encriptar_cadena(cadena)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #calculo la complejidad de espacio
                    cadena_encriptada="8 15 12 1  13 21 14 4 15"
                    before = sys.getsizeof(desencriptar_cadena)
                    result = desencriptar_cadena(cadena_encriptada)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 3:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def palabras_que_empiecen_con_la_letra_ingresada(cadena_letra):
                        '''
                        Funcion que se guarden las palabras que empiecen por la letra ingresada para imprimirlas en la funcion main

                        Parametros:
                        ------------
                            cadena_letra : str
                        Retorna:
                        ------------
                            letra_inicial : lista
                        '''
                        #declaro una lista para guardar las palabras que empiecen con la letra ingresada
                        letra_inicial = []
                        #divido la cadena en palabras
                        palabras = cadena_letra[0].split()
                        #recorro la cadena
                        for cadena in palabras:
                            #si la palabra empieza por la letra ingresada
                            if cadena.startswith(cadena_letra[1]):
                                #agregamos esa palabra a la lista letra_inicial
                                letra_inicial.append(cadena)
                        #retorno las palabras que empiecen con la letra ingresada
                        return letra_inicial
                    cadena_letra=["hola hombre","h"]
                    before = sys.getsizeof(palabras_que_empiecen_con_la_letra_ingresada)
                    result = palabras_que_empiecen_con_la_letra_ingresada(cadena_letra)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 4:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def ordenar_cadena(cadena):
                        '''
                        Funcion que ordena una cadena de caracteres de forma (a,b,c,...,z)

                        Parametros:
                        ------------
                            cadena : str
                        Retorna:
                        ------------
                            esta funcion no retorna ningun tipo de dato
                        '''
                        #uso sorte para devolver una lista ordenada a partir de los elementos del iterable y las uno
                        cadena_ordenada = ''.join(sorted(cadena))
                        #retorno la cadena ordenada
                        return cadena_ordenada
                    cadena="sbhsljuie"
                    before = sys.getsizeof(ordenar_cadena)
                    result = ordenar_cadena(cadena)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 5:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def validar_placa_moto(placa):
                        '''
                        Funcion que valida la placa de una moto

                        Parametros:
                        ------------
                            placa :str
                        Retorna:
                        ------------
                            0 : int
                            1 : int 
                        '''
                        #si hay mas de 6 caracteres en la placa no sera valida
                        if(len(placa)!=6):
                            return 0

                        #Si los 2 primeros caracteres son letras, el tercer, cuarto y quinto caracter son numero y el ultimo caracter es una letra
                        if(placa[0].isalpha() and placa[1].isalpha() and placa[2].isdigit() and placa[3].isdigit() and placa[4].isdigit() and placa[5].isalpha()):
                            #si la primera letra empieza con A,B,C,E,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z la placa es valida
                            if(placa[0]=='A' or placa[0]=='B' or placa[0]=='C' or placa[0]=='E' or placa[0]=='G' or placa[0]=='H' or placa[0]=='I' or placa[0]=='J' or placa[0]=='K' or placa[0]=='L' or placa[0]=='M' or placa[0]=='N' or placa[0]=='O' or placa[0]=='P' or placa[0]=='Q' or placa[0]=='R' or placa[0]=='S' or placa[0]=='T' or placa[0]=='U' or placa[0]=='V' or placa[0]=='W' or placa[0]=='X' or placa[0]=='Y' or placa[0]=='Z'):
                                return 1
                            #Caso contrario es invalida
                            else:
                                return 0
                        #Caso contrario es invalida
                        else:
                            return 0
                    @profile
                    def validar_placa_automovil(placa):
                        '''
                        Funcion que valida la placa de un automvil

                        Parametros:
                        ------------
                            placa :str
                        Retorna:
                        ------------
                            0 : int
                            1 : int
                        '''
                        #si hay mas de 8 caracteres en la placa no sera valida
                        if(len(placa)!=8):
                            return 0
                        #Si los 3 primeros caracteres son letras el cuarto un guion y los ultimos 4 caracteres son numeros
                        if(placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha() and placa[3]=='-' and placa[4].isdigit() and  placa[5].isdigit() and placa[6].isdigit() and placa[7].isdigit()):
                            #si la primera letra empieza con A,B,C,E,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z la placa es valida
                            if(placa[0]=='A' or placa[0]=='B' or placa[0]=='C' or placa[0]=='E' or placa[0]=='G' or placa[0]=='H' or placa[0]=='I' or placa[0]=='J' or placa[0]=='K' or placa[0]=='L' or placa[0]=='M' or placa[0]=='N' or placa[0]=='O' or placa[0]=='P' or placa[0]=='Q' or placa[0]=='R' or placa[0]=='S' or placa[0]=='T' or placa[0]=='U' or placa[0]=='V' or placa[0]=='W' or placa[0]=='X' or placa[0]=='Y' or placa[0]=='Z'):
                                return 1
                            #Caso contrario es invalida
                            else:
                                return 0
                        #Caso contrario es invalida
                        else:
                            return 0
                    print("Fincuin validar placa automovil")
                    placa="PQR-4568"
                    before = sys.getsizeof(validar_placa_automovil)
                    result = validar_placa_automovil(placa)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #calculo la complejidad de espacio
                    print("Fincuin validar placa moto")
                    placa="PQ458Q"
                    before = sys.getsizeof(validar_placa_moto)
                    result = validar_placa_moto(placa)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 6:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def verificar_si_contrasena_es_segura(contrasena):
                        '''
                        Funcion que verifica si una contraseña es segura

                        Parametros:
                        ------------
                            contrasena : str
                        Retorna:
                        ------------
                            0 : int
                            1 : int
                        '''
                        #declaro variables banderas como falsas donde dependieno si una parte del mi codigo cumple un requisito estas cambiaran
                        numero=False
                        mayuscula = False
                        minuscula = False
                        caracter_especial = False 
                        #si la contraseña tiene menos de 10 caracteres no es valida
                        if(len(contrasena)<10):
                            return 0
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
                            return 1
                        #caso contrario no es segura
                        else:
                            return 0
                    contrasena="ABC124efg@@@"
                    before = sys.getsizeof(verificar_si_contrasena_es_segura)
                    result = verificar_si_contrasena_es_segura(contrasena)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 7:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def anagrama(cadenas_1_y_2):
                        '''
                        Funcion que compara las dos cadenas ingresadas por teclado para ver si es un anagrama o no

                        Parametros:
                        ------------
                            cadenas_1_y_2 : lista
                        Retorna:
                        ------------
                            1 : int
                            0 : int
                        '''
                        #convierto a las cadenas 1 y 2 a una lista con la funcion list y luego las ordeno con la funcion sorted
                        #si al compararlas son iguales entonces retornamos 1(anagrama)
                        if(sorted(list(cadenas_1_y_2[0]))==sorted(list(cadenas_1_y_2[1]))):
                            return 1
                        #caso contrario retornamos 0(no es anagrama)
                        else:
                            return 0
                    cadenas_1_y_2=["hola","aloh"]
                    before = sys.getsizeof(anagrama)
                    result = anagrama(cadenas_1_y_2)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 8:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def validar_formato_de_un_correo_electronico(correo_electronico):
                        '''
                        Funcion que valida si el formato de un correo electronico ingresado por teclado es valido

                        Parametros:
                        ------------
                            correo_electronico : str 
                        Retorna:
                        ------------
                            Esta funcion no retorna ningun tipo de dato
                        '''
                        #Formato de correo aceptable : nombreaaaa @ xxxmail .com
                        patron_correo=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                        #buscamos si el formato es una subcadena de la cadena correo_electronico, la funcion imprime un mensaje de si es valido o no el formato
                        #del correo
                        if re.search(patron_correo, correo_electronico):
                            return 1 
                        else:
                            return 0
                    correo_electronico="nandocueva@gmail.com"
                    before = sys.getsizeof(validar_formato_de_un_correo_electronico)
                    result = validar_formato_de_un_correo_electronico(correo_electronico)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 9:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo complejidad de espacio
                    @profile
                    def verificar_si_una_cadena_tiene_solo_letras(cadena):
                        '''
                        Funcion que verifica si una cadena tiene solo letras o si tambien esta cadena tiene numeros

                        Parametros:
                        ------------
                            cadena : str
                        Retorna:
                        ------------
                            return 2
                            return 1
                            return 0
                        '''
                        #Si la funcion contiene solo letras imprime que solo hay letras
                        if cadena.isalpha() :
                            return 0
                            
                        #Si la funcion contiene solo numeros imprime que solo hay numeros
                        elif cadena.isdigit():
                            return 1
                            
                        #Si la funcion contiene letras y numeros imprimra que tienes numeros y letras
                        else:
                            return 2
                    cadena="abfauwk"
                    before = sys.getsizeof(verificar_si_una_cadena_tiene_solo_letras)
                    result = verificar_si_una_cadena_tiene_solo_letras(cadena)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 10:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo complejidad de espacio
                    @profile
                    def reemplazar_palabra_en_cadena_ingresada(cadenas_palabras):
                        '''
                        Funcion que reemplaza la palabra de cadena ingresada por otra palabra ingresada por teclado
                        Parametros:
                        ------------
                            cadenas_palabras : lista
                        Retorna:
                        ------------
                            cadena2 : str
                        '''
                        #creamos la nueva cadena una vez reemplazada la palabra escogida
                        cadena2 = cadenas_palabras[0].replace(cadenas_palabras[1], cadenas_palabras[2])
                        return cadena2
                    cadenas_palabras=["hola mundo","hola","mundo"]
                    before = sys.getsizeof(reemplazar_palabra_en_cadena_ingresada)
                    result = reemplazar_palabra_en_cadena_ingresada(cadenas_palabras)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 11:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo complejidad de espacio
                    @profile
                    def validacion_cedula(cedula):
                        '''
                        Funcion que valida si la cedula ingresada es valida o no

                        Parametros:
                        ------------
                            cedula : str
                        Retorna:
                        ------------
                            0 : int 
                            1 : int
                        '''
                        #si el tamaño de la cedula es mayor a 10 caracteres  o menor a 10 es falsa
                        if(len(cedula)>10 or len(cedula)<10):
                            return 0
                        #si en la lista hay una letra, la cedula es falsa
                        for char in cedula:
                            if char.isalpha():
                                return 0
                        #multiplicos los numeros que esten en posiciones impares de la cedula por 2
                        impar1=int(cedula[0])*2
                        impar2=int(cedula[2])*2
                        impar3=int(cedula[4])*2
                        impar4=int(cedula[6])*2
                        impar5=int(cedula[8])*2
                        if(impar1>9):
                            impar1=impar1-9
                        if(impar2>9):
                            impar2=impar2-9
                        if(impar3>9):
                            impar3=impar3-9
                        if(impar4>9):
                            impar4=impar4-9
                        if(impar5>9):
                            impar5=impar5-9
                        suma_impares=impar1+impar2+impar3+impar4+impar5
                        #convierto la cadena en entero
                        par1=int(cedula[1])
                        par2=int(cedula[3])
                        par3=int(cedula[5])
                        par4=int(cedula[7])
                        #sumo los numeros en las posiciones pares de la ceula
                        suma_pares=par1+par2+par3+par4
                        suma_total=suma_pares+suma_impares
                        #calculo el modulo
                        modulo=suma_total%10

                        #convierto el ultimo caracter de la cadena en digito
                        ultimo_digito=int(cedula[9])
                        #si el modulo es diferente de cero
                        if(modulo>0):
                            #restamos 10 menos el valo de modulo
                            modulo=10-modulo
                            #si el valor de esa resta es igual al ultimo digito de la cedula entonces es valida, caso contrario no
                            if(modulo==ultimo_digito):
                                return 1
                            else:
                                return 0
                        #si la cedula es cero verificamos si el cero es igual al ultimo digito de la cedula entonces es valida, caso contrario no
                        else:
                            if(modulo==ultimo_digito):
                                return 1
                            else:
                                return 0
                    cedula="1751486950"
                    before = sys.getsizeof(validacion_cedula)
                    result = validacion_cedula(cedula)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    print("La complejidad espacial de la función es: ", space_complexity)
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 12:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def diferencia_de_cadenas(cadenas_1_2):
                        '''
                        Funcion que imprime la diferencia de dos cadenas en términos de caracteres añadidos, eliminados y cambiados

                        Parametros:
                        ------------
                            cadenas_1_2 : lista
                        Retorna:
                        ------------
                            caracteres_agregados : conjunto
                            caracteres_eliminados : conjunto
                            caracteres_cambiados : conjunto
                        '''
                        #en caracteres agregados se guardan las letras nuevas que estan en la segunda cadena
                        caracteres_agregados = set(cadenas_1_2[1]) - set(cadenas_1_2[0])
                        #en caracteres eliminados se guardan las letras que no se encuentran dentro de la primera cadena
                        caracteres_eliminados = set(cadenas_1_2[0]) - set(cadenas_1_2[1])
                        #en caracteres cambiados se guardan si los valores en la posicion de los caracteres es diferente
                        caracteres_cambiados = set(c1 + c2 for c1, c2 in zip(cadenas_1_2[0], cadenas_1_2[1]) if c1 != c2)
                        #retorno la diferencia
                        return caracteres_agregados,caracteres_eliminados,caracteres_cambiados
                    cadenas_1_2=["abcdef","defghi"]
                    before = sys.getsizeof(diferencia_de_cadenas)
                    result = diferencia_de_cadenas(cadenas_1_2)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 13:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def palabra_mas_larga(cadena):
                        '''
                        Funcion que imprime la palabra mas larga que se encuentre dentro de una oracion

                        Parametros:
                        ------------
                            cadena : str
                        Retorna:
                        ------------
                            palabra_mas_larga : str  
                        '''
                        #declaro una variable tipo str para guardar la palabra mas larga al recorrer la orcion
                        palabra_mas_larga = ""
                        #separon las palabras que se encuentren dentro de una oracion
                        palabras = cadena.split()
                        #recorro la lista plabras
                        for palabra in palabras:
                            #si el tamaño de la palbra es mas grande que la que se encuentra dentro de la variable palabra_mas_larga
                            if len(palabra) > len(palabra_mas_larga):
                                #esa palabra se agregara a esa variable 
                                palabra_mas_larga = palabra
                        return palabra_mas_larga
                    cadena="hola mundo como estas"
                    before = sys.getsizeof(palabra_mas_larga)
                    result = palabra_mas_larga(cadena)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 14:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    cadena="hola mundo como estas"
                    before = sys.getsizeof(palabra_mas_larga)
                    result = palabra_mas_larga(cadena)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 15:
                    #imprime las letras en color cian
                    print("\033[1;36m")
                    #limpio pantalla
                    os.system("cls")
                    #calculo la complejidad de espacio
                    @profile
                    def encontrar_palabras_con_tamaño_especifico(cadena_nletra):
                        '''
                        Funcion que encuentra palabras con el tamaño especifico segun nLetras

                        Parametros:
                        ------------
                            cadena_nletra : lista
                        Retorna:
                        ------------
                            palabras_tamaño_indicado : lista
                        '''
                        #separon las palabras de cadena
                        palabras = cadena_nletra[0].split()
                        #declaro una lista vacia
                        palabras_tamaño_indicado = []
                        #recorro la lista
                        for palabras in palabras:
                            #si el tamaño de palabas es igual a nLetra
                            if len(palabras) == cadena_nletra[1]:
                                #guardamos esa palabra en la lista
                                palabras_tamaño_indicado.append(palabras)
                        #retorno las palabras que contenga el mismo numero de caracteres que nLetra
                        return palabras_tamaño_indicado
                    cadena_nletra=["hola amigo","a"]
                    before = sys.getsizeof(encontrar_palabras_con_tamaño_especifico)
                    result = encontrar_palabras_con_tamaño_especifico(cadena_nletra)
                    after = sys.getsizeof(result)
                    space_complexity = after - before
                    #pauso pantalla
                    os.system("pause")
                if opcion3 == 16:
                    break
        if opcion == 18:
            break
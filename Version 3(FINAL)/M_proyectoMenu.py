#libreria que uso para obtener la tecla presionada sin necesidad de presionar Enter
import msvcrt
#funcion que uso para pausar y limpiar pantalla
import os
#funcion que uso para llamar a otros .py en este programa
import subprocess 
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
    "16. Imprimir todas las palabras en una cadena dada que tienen una cantidad específica de numero de caracteres","17. Salir"]
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
if __name__ == '__main__': 
    print("Selecciona una opcion:")
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
            break
    
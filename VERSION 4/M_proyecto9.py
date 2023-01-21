#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda a pausar el codigo
import os
#libreria que me ayuda con el formato de caracteres
import re
"""
Programa que valida si el formato de un correo electronico ingresado por teclado es valido

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
#@profile
def leer_correo():
    '''
    Funcion que lee una cadena de caracteres(correo)

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        correo_electronico : str
    '''
    #Ingreso una cadena por teclado
    correo_electronico=input("Ingresa un correo electronicio para validar su formato:")
    #retorno el correo electronigo ingresado por teclado
    return correo_electronico

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
        
if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Indicaciones para usar el verificador de correos electronicos")
    print("     Ingresar un corre electronico por teclado")
    print("     Para que este validado debe cumplir el siguiente formato:")
    print("     (nombre de usuario[letras,numeros, caracteres especiales])+@+dominio+.com)")
    print("     Si cumple con ese formato el correo sera valido")
    #pauso el codigo
    os.system("pause")
    #ingreso el correo electronico por teclado
    correo_electronico=leer_correo()
    #valido si el formato del correo es valido o no
    valido=validar_formato_de_un_correo_electronico(correo_electronico)
    if(valido==1):
        print("El formato del correo electronico es valida")
    if(valido==0):
        print("El formato del correo electronico no es valida")
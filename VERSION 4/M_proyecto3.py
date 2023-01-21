#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda a pausar el codigo
import os
"""
Funcion que encripta una cadena ingresada por teclado reemplazando cada letra con un numero

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
#@profile
def validar_cadena():
    '''
    Funcion que valida si lo ingresado por teclado sean caracteres y no numeros

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        letra : str
    '''
    #valido que lo que se ingreso para que no este algo que sea un numero
    while True:
        #ingreso una cadena por teclado
        cadena = input("Ingrese una cadena: ")
        #declaramos una variable bandera
        tiene_numero = False
        #recorremos la cadena
        for caracter in cadena:
            #si hay un numero en la cadena
            if caracter.isdigit():
                #cambiamos el valor de la variable bandera
                tiene_numero = True
                break
        #si la variable bandera es verdadero imprimir que no se ingreso una letra
        if tiene_numero:
            print("Hay numeros dentro de su cadena.")
        #caso contrario rompemos el ciclo repetitivo
        else:
            break
    #hago que la letra ingresada sea minuscula
    cadena=cadena.lower()
    #retorno cadena
    return cadena
#@profile
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
#@profile
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
if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona este programa?")
    print("     Se ingresa una cadena por teclado la cual se encriptara reemplazando sus letras por numeros de igual manera")
    print("     tambien se retornara la funcion desencriptada")
    print("     No ingrese numeros dentro de la cadena para que funcione correctamente")
    print("     Ejemplo:")
    print("     Ingreso -> hola amigo")
    print("     encriptacion -> 8 15 12 1  1 13 9 7 15")
    print("     desencriptacion -> holaamigo")
    #pauso el codigo
    os.system("pause")
    #ingreso una cadena de carcteres
    cadena=validar_cadena()
    #encriptamos la cadena
    cadena_encriptada=encriptar_cadena(cadena)
    print("Cadena encriptada: ",cadena_encriptada)
    #desencriptamos la cadena
    cadena_desencriptada=desencriptar_cadena(cadena_encriptada) 
    print("Cadena desencriptada: ",cadena_desencriptada)
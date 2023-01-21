#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda a pausar el codigo
import os
"""
Funcion que ordena una cadena de caracteres de forma (a,b,c,...,z)

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
#@profile
def validar_letra():
    '''
    Funcion que valida si lo ingresado por teclado sean caracteres y no numeros

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena : str
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
            print("No ingrese numeros dentro de la cadena.")
        #caso contrario rompemos el ciclo repetitivo
        else:
            break
    #convierto todo lo que este dentro de la cadena en minusculas
    cadena=cadena.lower()
    #retorno cadena
    return cadena
#@profile
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
if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona este programa?")
    print("     Se ingresan una cadena por teclado para que el programa la retorne en orden de manera ascendente")
    print("     No ingrese numeros dentro de la cadena para que funcione correctamente")
    print("     Ejemplo:")
    print("     Ingreso-> cba") 
    print("     Retorna-> abc")
    #pauso el codigo
    os.system("pause")
    #leo la cadena ingresada
    cadena=validar_letra()
    #ordeno la cadena
    print("Cadena ordenada: ",ordenar_cadena(cadena))
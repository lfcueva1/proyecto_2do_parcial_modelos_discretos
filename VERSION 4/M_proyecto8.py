#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda a pausar el codigo
import os

"""
Programa que compara las dos cadenas ingresadas por teclado para ver si es un anagrama o no

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
        cadenas_1_y_2 : lista
    '''
    #valido que lo que se ingreso para que no este algo que sea un numero
    while True:
        cadena1 = input("Ingrese la primera cadena: ")
        tiene_numero = False
        for caracter in cadena1:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("No ingrese numeros dentro de la cadena.")
        else:
            break
    #convierto todo lo que este dentro de la cadena en minusculas
    cadena1=cadena1.lower()
    #agrego cadena1 a la lista
    cadenas_1_y_2.append(cadena1)
    #valido que lo que se ingreso para que no este algo que sea un numero
    while True:
        cadena2 = input("Ingrese la segunda cadena: ")
        tiene_numero = False
        for caracter in cadena2:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("No ingrese numeros dentro de la cadena.")
        else:
            break
    #convierto todo lo que este dentro de la cadena en minusculas
    cadena2=cadena2.lower()
    #agrego cadena2 a la lista
    cadenas_1_y_2.append(cadena2)
    #retorno cadena1 y cadena2
    return cadenas_1_y_2
#@profile
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
if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como saber si una palabra es un anagrama de otra palabra?")
    print("     Un anagrama es una palabra o frase formada al reorganizar las letras de una palabra o frase diferente, ")
    print("     normalmente usando todas las letras originales exactamente una vez.")
    print("Indicaciones:")
    print("     Ingrese dos cadenas por teclado")
    print("     Evite ingresar numeros en las cadenas para evitar errores")
    #pauso el codigo
    os.system("pause")
    #declaro una lista vacia
    cadenas_1_y_2=[]
    #ingreso la cadena 1 y 2
    cadenas_1_y_2=validar_cadena()
    #verifico si es un anagrama
    valido=anagrama(cadenas_1_y_2)
    #si el valor retornado es 1 es anagrama
    if(valido==1):
        print("Es un anagrama")
    #si el valor retornado es 0 no es anagrama
    if(valido==0):
        print("la cadena 2 no es un anagrama de la primera")
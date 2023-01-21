#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda a pausar el codigo
import os
"""
Programa que imprime la diferencia de dos cadenas en términos de caracteres añadidos, eliminados y cambiados

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
#@profile
def leer_cadenas():
    '''
    Funcion que lee una cadena de caracteres
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadenas_1_2 : lista
    '''
    #Ingreso la primera cadena y segunda cadena por teclado
    cadena1 = input("Ingrese la primera cadena: ")
    cadenas_1_2.append(cadena1)
    cadena2 = input("Ingrese la segunda cadena: ")
    cadenas_1_2.append(cadena2)
    #retorno las cadenas
    return cadenas_1_2
#@profile
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
    
if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona?")
    print("     Ingresar dos cadenas por teclado")
    print("     El programa imprimira los respectivos cambios que se hicieron en las cadenas")
    #pauso el codigo
    os.system("pause")
    #declaro una lista vacia
    cadenas_1_2=[]
    #ingreso las dos cadenas
    cadenas_1_2=leer_cadenas()
    #verifico si hay diferencias
    caracteres_agregados,caracteres_eliminados,caracteres_cambiados=diferencia_de_cadenas(cadenas_1_2)
    #imprimo la diferencia de las dos cadenas en términos de caracteres añadidos, eliminados y cambiados
    print("Caracteres añadidos: ", caracteres_agregados)
    print("Caracteres eliminados: ", caracteres_eliminados)
    print("Caracteres cambiados: ", caracteres_cambiados)
    
#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda con la complejidad del tiempo
import big_o
#libreria que me ayuda a pausar el codigo
import os
"""
Programa que reemplaza la palabra de cadena ingresada por otra palabra ingresada por teclado

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
@profile
def leer_variables():
    '''
    Funcion que lee una cadena de caracteres
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadenas_palabras _ lista
    '''
    #Ingreso una cadena por teclado
    cadena=input("Ingresa una oracion:")
    cadenas_palabras.append(cadena)
    #ingreso la palabra que deseo reemplazar
    print("Que palabra dentro de la cadena ingresada desea reemplazar: ",end="")
    palabra_a_reemplazar=input()
    cadenas_palabras.append(palabra_a_reemplazar)
    #ingreso la palabra que reemplazara a la letra que deseamos reemplazar
    print("Con que palabra desea reemplazarla?: ",end="")
    palabra_reemplazo=input()
    cadenas_palabras.append(palabra_reemplazo)
    #cambio los caracteres de la cadena,palabra_a_reemplazar,palabra_reemplazo a minusculas para evitar errores
    cadenas_palabras[0]=cadenas_palabras[0].lower()
    cadenas_palabras[1]=cadenas_palabras[1].lower()
    cadenas_palabras[2]=cadenas_palabras[2].lower()
    #retorno las variables 
    return cadenas_palabras
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
if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona?")
    print("     Se debe ingresar una cadena por teclado")
    print("     Se debe ingresar la palabra que desea modificar de la primera cadena")
    print("     Se debe ingresar la palabra que reemplazara a la palabra que desea modificar")
    print("     Ejemplo:")
    print("     Ingreso -> hola mundo")
    print("     Ingreso -> hola")
    print("     Ingreso -> adios")
    print("     retorna-> adios mundo")
    #pauso el codigo
    os.system("pause")
    #declaro una cadena vacia
    cadenas_palabras=[]
    #leo la cadena ingresada por teclado
    cadenas_palabras=leer_variables()
    #imprimo la cadena original
    print("Cadena original: ",cadenas_palabras[0])
    #reemplazo la palabra
    cadena2=reemplazar_palabra_en_cadena_ingresada(cadenas_palabras)
    #imprime la oracion modificada
    print("Oración modificada: ", cadena2)
    print("BIG_O:")
    positive_int_generator = lambda n: cadenas_palabras
    best, others= big_o.big_o(reemplazar_palabra_en_cadena_ingresada,positive_int_generator)
    print(best)
#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda con la complejidad del tiempo
import big_o
#libreria que me ayuda a pausar el codigo
import os
"""
Programa que ingresa una oracion por teclado donde el programa imprime las
palabras repetidas que se encuentren dentro de esa cadena

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
@profile
def leer_variables():
    '''
    Funcion que lee los dos nombres y apellido del usuario y los valida
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        oracion : str
    '''
    #Ingreso una oracion por teclado
    oracion_palabras=input("Ingrese una oracion:")
    #retorno la cadena ingresada
    print("Oracion ingresada: ",oracion_palabras)
    #retorno la cadena
    return oracion_palabras
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

if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona este programa?")
    print("     Se ingresa una oracion de varias palabras y el programa imprime las palabras que se repiten")
    print("     Ejemplo:")
    print("     Ingreso -> hola hola amigo")
    print("     Retorna -> Palabras que se repiten:hola")
    #pauso el codigo
    os.system("pause")
    #ingreso una oracion
    oracion_palabras=leer_variables()
    #guardo lo que me retorno esta funcion en la variable
    repetidas=palabras_repetidas_ingresadas(oracion_palabras)
    #imprimo las palabras repetidas que se encuentren dentro de la oracion ingresada por teclado
    print("Palabras que se repiten: ",repetidas)
    #imprimo big_o
    print("BIG_O:")
    positive_int_generator = lambda n: oracion_palabras
    best, others= big_o.big_o(palabras_repetidas_ingresadas,positive_int_generator)
    print(best)
    
    
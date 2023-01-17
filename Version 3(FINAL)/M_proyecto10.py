#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda con la complejidad del tiempo
import big_o
#libreria que me ayuda a pausar el codigo
import os
"""
Programa que verifica si una cadena tiene solo letras o si tambien esta cadena tiene numeros

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
@profile
def leer_cadena():
    '''
    Funcion que lee una cadena de caracteres
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena : str
    '''
    #Ingreso una cadena por teclado
    cadena=input("Ingresa una cadena:")
    #convierto en minusculas los caracteres dentro de la cadena
    cadena=cadena.lower()
    #retorno la oracion ingresada
    return cadena
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
        

if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona?")
    print("     Se debe ingresar una cadena por teclado")
    print("     El programa recorre cada letra de la cadena para verificar si:")
    print("     1. Hay solo letras en la cadena")
    print("     2. Hay solo numeros en la cadena")
    print("     3. Hay letras y numeros en la cadena")
    #pauso el codigo
    os.system("pause")
    #leo la cadena ingresada por teclado
    cadena=leer_cadena()
    #verifico si la letra solo tiene letras o si en esa cadena tambien hay numeros
    tipo_dato=verificar_si_una_cadena_tiene_solo_letras(cadena)
    if(tipo_dato==0):
        print("Su cadena solo tiene letras")
    if(tipo_dato==1):
        print("Su cadena contiene solo numeros")
    if(tipo_dato==2):
        print("Su cadena tiene letras y numeros")
    print("BIG_O:")
    positive_int_generator = lambda n: cadena
    best, others= big_o.big_o(verificar_si_una_cadena_tiene_solo_letras,positive_int_generator)
    print(best)
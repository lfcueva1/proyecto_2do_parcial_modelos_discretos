#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda con la complejidad del tiempo
import big_o
#libreria que me ayuda a pausar el codigo
import os
#libreria que me ayuda con el formato de un correo electronico
"""
Programa que encuentra palabras con el tamaño especifico segun un numero ingresado por teclado

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
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
        #en caso de que no se haya ingresado un numero entero se imprimira un mensaje diciendo que no se ingreso un enetero
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero
@profile
def leer_cadena():
    '''
    Funcion que lee una cadena de caracteres
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena_nletra : lista
    '''
    #Ingreso una oracion
    cadena = input("Ingrese una oracion: ")
    cadena_nletra.append(cadena)
    #ingreso un numero el cual sera el tamañao de las palabras que podran imprimirse
    print("Ingrse el tamaño(numero entero) con las que se imprimira las palabras que tengan ese tamaño: ",end="")
    nLetras=validar_numeros_enteros()
    while(nLetras<1):
        print("Solo ingrese numeros positivos: ",end="")
        nLetras=validar_numeros_enteros()
    cadena_nletra.append(nLetras)
    #retorno la oracion y nletras
    return cadena_nletra
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
    
if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona?")
    print("     Ingresar una cadena por teclado")
    print("     Ingresar un numero entero por teclado(sirve para imprimir las palabras que tengan el mismo numero de caracteres)")
    print("     Ejemplo:")
    print("     Ingreso -> hola Fernando")
    print("     Ingreso -> 8")
    print("     Retorna -> Fernando")
    #pauso el codigo
    os.system("pause")
    #declaro una lista vacia
    cadena_nletra=[]
    #leo una cadena de palabras
    cadena_nletra=leer_cadena()
    #encuentro las palabras con el tamaño especifico
    palabras_encontradas=encontrar_palabras_con_tamaño_especifico(cadena_nletra)
    #imprimo las palabras que contengan el mismo numero de caracteres que nLetra
    print("Palabras con el tamaño ",cadena_nletra[1],": ", palabras_encontradas)
    print("BIG_O:")
    positive_int_generator = lambda n: cadena_nletra
    best, others= big_o.big_o(encontrar_palabras_con_tamaño_especifico,positive_int_generator)
    print(best)
#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda con la complejidad del tiempo
import big_o
#libreria que me ayuda a pausar el codigo
import os
"""
Funcion que guarda las palabras que empiecen por la letra ingresada para imprimirlas en la funcion main

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
@profile
def validar_cadena():
    '''
    Funcion que valida si lo ingresado por teclado sean caracteres y no numeros

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena_letra : lista
    '''
    #valido que lo que se ingreso para que no este algo que sea un numero
    while True:
        #ingreso una cadena por teclado
        cadena = input("Ingrese una cadena(sin numeros): ")
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
            print("No ingrese numeros en su cadena, solo letras.")
        #caso contrario rompemos el ciclo repetitivo
        else:
            break
    #hago que la cadena ingresada sea minuscula y la agregamos a la lista
    cadena=cadena.lower()
    cadena_letra.append(cadena)
    #creamos un bucle infinito
    while True:
        #ingreso una letra y la valido para que lo ingresado sea solo una letra y no mas, y valid para que no ingrese numeros 
        letra = input("Ingrese una letra: ")
        #mientras el tamaño de la letra sea mayor a uno
        while (len(letra)>1):
            #imprime un mensaje de error y hacemos que el usuario vuelva a ingresar una letra
            print("Ingresó mas de una letra, ingrese de nuevo:")
            letra=input("Ingrese una letra: ")
        #declaramos una variable bandera    
        tiene_numero = False
        #recorremos la cadena
        for caracter in letra:
            #si hay un numero en la cadena
            if caracter.isdigit():
                #cambiamos el valor de la variable bandera
                tiene_numero = True
                break
        #si la variable bandera es verdadero imprimir que no se ingreso una letra
        if tiene_numero:
            print("Lo que ingreso no es una letra. Intente de nuevo.")
        #caso contrario rompemos el ciclo repetitivo   
        else:
            break
    #hago que la letra ingresada sea minuscula
    letra=letra.lower()
    #agrego la letra a la lista
    cadena_letra.append(letra)
    #retorno cadena
    return cadena_letra

@profile
def palabras_que_empiecen_con_la_letra_ingresada(cadena_letra):
    '''
    Funcion que se guarden las palabras que empiecen por la letra ingresada para imprimirlas en la funcion main

    Parametros:
    ------------
        cadena_letra : str
    Retorna:
    ------------
        letra_inicial : lista
    '''
    #declaro una lista para guardar las palabras que empiecen con la letra ingresada
    letra_inicial = []
    #divido la cadena en palabras
    palabras = cadena_letra[0].split()
    #recorro la cadena
    for cadena in palabras:
        #si la palabra empieza por la letra ingresada
        if cadena.startswith(cadena_letra[1]):
            #agregamos esa palabra a la lista letra_inicial
            letra_inicial.append(cadena)
    #retorno las palabras que empiecen con la letra ingresada
    return letra_inicial

if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona este programa?")
    print("     Se ingresan varias palabras como cadena, tambien se ingresa una letra, una vez ingresadas las palabras")
    print("     se imprimirá las palabras que empiecen por el caracter que se encuentre en la variable letra")
    print("     No ingrese numeros dentro de la cadena para que funcione correctamente")
    print("     Ejemplo:")
    print("     Ingreso-> hola amigo tengo hambre")
    print("     Ingreso-> h")  
    print("     Retorna-> hola,hambre")
    #pauso el codigo
    os.system("pause")
    cadena_letra=[]
    #ingreso una cadena de carcteres
    cadena_letra=validar_cadena()
    #lista donde guardo las palabras que me genera la funcion "palabras_que_empiecen_con_la_letra_ingresada(cadena,letra)"
    letra_inicial=palabras_que_empiecen_con_la_letra_ingresada(cadena_letra)
    #imprimo las palabras que empiezan con la letra que se ingreso por teclado
    print("Palabras que empiezan con ",cadena_letra[1],":",letra_inicial)
    print("BIG_O:")
    positive_int_generator = lambda n: cadena_letra
    best, others= big_o.big_o(palabras_que_empiecen_con_la_letra_ingresada,positive_int_generator)
    print(best)
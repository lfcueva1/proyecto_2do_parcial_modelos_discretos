import big_o
def validar_letra():
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
        letra = input("Ingrese una letra: ")
        tiene_numero = False
        for caracter in letra:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("Lo que ingreso no es una letra. Intente de nuevo.")
        else:
            break
    #hago que la letra ingresada sea minuscula
    letra=letra.lower()
    return letra
def leer_variables():
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
    cadena=input("Ingrese una cadena:")
    #ingreso una letra y la valido
    letra=validar_letra()
    while (len(letra)>1):
        print("Ingresó mas de una letra, ingrese de nuevo:")
        letra=validar_letra()
    #retorno la cadena y la letra ingresada
    return cadena,letra

def palabras_que_empiecen_con_la_letra_ingresada(cadena,letra):
    '''
    Funcion que se guarden las palabras que empiecen por la letra ingresada para imprimirlas en la funcion main

    Parametros:
    ------------
        cadena : str
        letra : str
    Retorna:
    ------------
        letra_inicial : lista
    '''
    #hago que todos los caracteres de la cadena sean minusculas para que no haya ningun error
    cadena=cadena.lower()
    #declaro una lista para guardar las palabras que empiecen con la letra ingresada
    letra_inicial = []
    #divido la cadena en palabras
    palabras = cadena.split()
    #recorro la cadena
    for cadena in palabras:
        #si la palabra empieza por la letra ingresada
        if cadena.startswith(letra):
            #agregamos esa palabra a la lista letra_inicial
            letra_inicial.append(cadena)
    #retorno las palabras que empiecen con la letra ingresada
    return letra_inicial

if __name__ == '__main__':
    #ingreso una cadena de carcteres
    cadena,letra=leer_variables()
    #lista donde guardo las palabras que me genera la funcion "palabras_que_empiecen_con_la_letra_ingresada(cadena,letra)"
    letra_inicial=palabras_que_empiecen_con_la_letra_ingresada(cadena,letra)
    #imprimo las palabras que empiezan con la letra que se ingreso por teclado
    print("Palabras que empiezan con ",letra,":",letra_inicial)
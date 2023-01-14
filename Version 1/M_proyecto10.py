import big_o
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
    cadena=input("Ingresa una oracion:")
    #retorno la oracion ingresada
    return cadena
def verificar_si_una_cadena_tiene_solo_letras(cadena):
    '''
    Funcion que verifica si una cadena tiene solo letras o si tambien esta cadena tiene numeros

    Parametros:
    ------------
        cadena : str
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #Si la funcion contiene solo letras imprime que solo hay letras
    if cadena.isalpha():
        print("Su cadena solo tiene letras")
    #Si la funcion contiene solo numeros imprime que solo hay numeros
    elif cadena.isdigit():
        print("Su cadena contiene solo numeros")
    #Si la funcion contiene letras y numeros imprimra que tienes numeros y letras
    else:
        print("Su cadena tiene numeros y letras")

if __name__ == '__main__':
    #leo la cadena ingresada por teclado
    cadena=leer_cadena()
    #verifico si la letra solo tiene letras o si en esa cadena tambien hay numeros
    verificar_si_una_cadena_tiene_solo_letras(cadena)
    print("BIG_O:")
    positive_int_generator = lambda n: cadena
    best, others= big_o.big_o(verificar_si_una_cadena_tiene_solo_letras,positive_int_generator)
    print(best)
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
    cadena=input("Ingresa una cadena:")
    #convierto en minusculas los caracteres dentro de la cadena
    cadena=cadena.lower()
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
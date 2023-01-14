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
    
    #retorno la oracion 
    return cadena

def reemplazar_palabra_en_cadena_ingresada(cadena,palabra_a_reemplazar, palabra_reemplazo):
    '''
    Funcion que reemplaza la palabra de cadena ingresada por otra palabra ingresada por teclado
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena : str
    '''
    #creamos la nueva cadena una vez reemplazada la palabra escogida
    cadena2 = cadena.replace(palabra_a_reemplazar, palabra_reemplazo)
    #imprime la oracion modificada
    print("Oración modificada: ", cadena2)
if __name__ == '__main__':
    #leo la cadena ingresada por teclado
    cadena=leer_cadena()
    print(cadena)
    print("Que palabra dentro de la cadena ingresada desea reemplazar",end="")
    palabra_a_reemplazar=input()
    print("Con que palabra desea reemplazarla?: ",end="")
    palabra_reemplazo=input()
    reemplazar_palabra_en_cadena_ingresada(cadena,palabra_a_reemplazar, palabra_reemplazo)

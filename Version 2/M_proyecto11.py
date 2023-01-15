import big_o
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
    cadena=input("Ingresa una oracion:")
    #ingreso la palabra que deseo reemplazar
    print("Que palabra dentro de la cadena ingresada desea reemplazar: ",end="")
    palabra_a_reemplazar=input()
    #ingreso la palabra que reemplazara a la letra que deseamos reemplazar
    print("Con que palabra desea reemplazarla?: ",end="")
    palabra_reemplazo=input()
    #cambio los caracteres de la cadena,palabra_a_reemplazar,palabra_reemplazo a minusculas para evitar errores
    cadena=cadena.lower()
    palabra_a_reemplazar=palabra_a_reemplazar.lower()
    palabra_reemplazo=palabra_reemplazo.lower()
    #retorno las variables 
    return cadena,palabra_a_reemplazar,palabra_reemplazo

def reemplazar_palabra_en_cadena_ingresada(cadena,palabra_a_reemplazar, palabra_reemplazo):
    '''
    Funcion que reemplaza la palabra de cadena ingresada por otra palabra ingresada por teclado
    Parametros:
    ------------
        cadena : str
        palabra_a_reemplazar : str
        palabra_reemplazo : str
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #creamos la nueva cadena una vez reemplazada la palabra escogida
    cadena2 = cadena.replace(palabra_a_reemplazar, palabra_reemplazo)
    #imprime la oracion modificada
    print("Oración modificada: ", cadena2)
if __name__ == '__main__':
    #leo la cadena ingresada por teclado
    cadena,palabra_a_reemplazar,palabra_reemplazo=leer_variables()
    #imprimo la cadena original
    print("Cadena original: ",cadena)
    #reemplazo la palabra
    reemplazar_palabra_en_cadena_ingresada(cadena,palabra_a_reemplazar, palabra_reemplazo)
 
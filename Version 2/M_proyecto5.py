import big_o
def validar_letra():
    '''
    Funcion que valida si lo ingresado por teclado sean caracteres y no numeros

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena : str
    '''
    #valido que lo que se ingreso para que no este algo que sea un numero
    while True:
        cadena = input("Ingrese una cadena: ")
        tiene_numero = False
        for caracter in cadena:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("No ingrese numeros dentro de la cadena.")
        else:
            break
    #convierto todo lo que este dentro de la cadena en minusculas
    cadena=cadena.lower()
    #retorno cadena
    return cadena

def ordenar_cadena(cadena):
    '''
    Funcion que ordena una cadena de caracteres de forma (a,b,c,...,z)

    Parametros:
    ------------
        cadena : str
    Retorna:
    ------------
        esta funcion no retorna ningun tipo de dato
    '''
    #uso sorte para devolver una lista ordenada a partir de los elementos del iterable y las uno
    cadena_ordenada = ''.join(sorted(cadena))
    #retorno la cadena ordenada

    return cadena_ordenada
    #imprimo la cadena ordenada
    #print("Cadena ordenada: ",cadena_ordenada)
if __name__ == '__main__':
    #leo la cadena ingresada
    cadena=validar_letra()
    #ordeno la cadena
    print("Cadena ordenada: ",ordenar_cadena(cadena))
    #imprimo big_o
    print("BIG_O:")
    positive_int_generator = lambda n: cadena
    best, others= big_o.big_o(ordenar_cadena,positive_int_generator)
    print(best)

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
    return cadena
def leer_variables():
    '''
    Funcion que lee una cadena de caracteres
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena1 : str
        cadena2 : str
    '''
    #Ingreso una cadena por teclado
    cadena1=validar_letra()
    #Ingreso una segunda cadena por teclado
    cadena2=validar_letra()
    #retorno la cadena ingresada
    return cadena1,cadena2

def anagrama(cadena1,cadena2):
    '''
    Funcion que compara las dos cadenas ingresadas por teclado para ver si es un anagrama o no

    Parametros:
    ------------
        cadena1 : str
        cadena2 : str
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #convierto a las cadenas 1 y 2 a una lista con la funcion list y luego las ordeno con la funcion sorted
    #si al compararlas son iguales entonces es un anagrama
    if(sorted(list(cadena1))==sorted(list(cadena2))):
        print("Es un anagrama")
    else:
        print("la cadena 2 no es un anagrama de la primera")
if __name__ == '__main__':
    #ingreso la cadena 1 y 2
    cadena1,cadena2=leer_variables()
    #verifico si es un anagrama
    anagrama(cadena1,cadena2)

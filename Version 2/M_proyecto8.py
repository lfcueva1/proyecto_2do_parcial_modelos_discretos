import big_o
def validar_cadena():
    '''
    Funcion que valida si lo ingresado por teclado sean caracteres y no numeros

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cadena1 : str
        cadena2 : str
    '''
    #valido que lo que se ingreso para que no este algo que sea un numero
    while True:
        cadena1 = input("Ingrese la primera cadena: ")
        tiene_numero = False
        for caracter in cadena1:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("No ingrese numeros dentro de la cadena.")
        else:
            break
    #convierto todo lo que este dentro de la cadena en minusculas
    cadena1=cadena1.lower()

    #valido que lo que se ingreso para que no este algo que sea un numero
    while True:
        cadena2 = input("Ingrese la segunda cadena: ")
        tiene_numero = False
        for caracter in cadena2:
            if caracter.isdigit():
                tiene_numero = True
                break
        if tiene_numero:
            print("No ingrese numeros dentro de la cadena.")
        else:
            break
    #convierto todo lo que este dentro de la cadena en minusculas
    cadena2=cadena2.lower()
    #retorno cadena1 y cadena2
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
        1 : int
        0 : int
    '''
    #convierto a las cadenas 1 y 2 a una lista con la funcion list y luego las ordeno con la funcion sorted
    #si al compararlas son iguales entonces retornamos 1(anagrama)
    if(sorted(list(cadena1))==sorted(list(cadena2))):
        return 1
    #caso contrario retornamos 0(no es anagrama)
    else:
        return 0
if __name__ == '__main__':
    #ingreso la cadena 1 y 2
    cadena1,cadena2=validar_cadena()
    #verifico si es un anagrama
    valido=anagrama(cadena1,cadena2)
    if(valido==1):
        print("Es un anagrama")
    if(valido==0):
        print("la cadena 2 no es un anagrama de la primera")

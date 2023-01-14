def leer_cadenas():
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
    #Ingreso la primera cadena y segunda cadena por teclado
    cadena1 = input("Ingrese la primera cadena: ")
    cadena2 = input("Ingrese la segunda cadena: ")
    #retorno las cadenas
    return cadena1,cadena2
def diferencia_de_cadenas(cadena1, cadena2):
    '''
    Funcion que imprime la diferencia de dos cadenas en términos de caracteres añadidos, eliminados y cambiados

    Parametros:
    ------------
        cadena1 : str
        cadena2 : str
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #en caracteres agregados se guardan las letras nuevas que estan en la segunda cadena
    caracteres_agregados = set(cadena2) - set(cadena1)
    #en caracteres eliminados se guardan las letras que no se encuentran dentro de la primera cadena
    caracteres_eliminados = set(cadena1) - set(cadena2)
    #en caracteres cambiados se guardan si los valores en la posicion de los caracteres es diferente
    caracteres_cambiados = set(c1 + c2 for c1, c2 in zip(cadena1, cadena2) if c1 != c2)
    #imprimo la diferencia de las dos cadenas en términos de caracteres añadidos, eliminados y cambiados
    print("Caracteres añadidos: ", caracteres_agregados)
    print("Caracteres eliminados: ", caracteres_eliminados)
    print("Caracteres cambiados: ", caracteres_cambiados)
if __name__ == '__main__':
    #ingreso las dos cadenas
    cadena1,cadena2=leer_cadenas()
    #verifico si hay diferencias
    diferencia_de_cadenas(cadena1, cadena2)
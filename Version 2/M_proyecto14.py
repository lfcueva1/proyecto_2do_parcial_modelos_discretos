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
    #Ingreso una oracion
    cadena = input("Ingrese una oracion: ")
    #retorno la oracion
    return cadena

def palabra_mas_larga(cadena):
    '''
    Funcion que imprime la palabra mas larga que se encuentre dentro de una oracion

    Parametros:
    ------------
        cadena : str
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #declaro una variable tipo str para guardar la palabra mas larga al recorrer la orcion
    palabra_mas_larga = ""
    #separon las palabras que se encuentren dentro de una oracion
    palabras = cadena.split()
    #recorro la lista plabras
    for palabra in palabras:
        #si el tamaño de la palbra es mas grande que la que se encuentra dentro de la variable palabra_mas_larga
        if len(palabra) > len(palabra_mas_larga):
            #esa palabra se agregara a esa variable 
            palabra_mas_larga = palabra
    return palabra_mas_larga
if __name__ == '__main__':
    #ingreso una oracion
    cadena=leer_cadena()
    #verifico la palabra mas larga
    palabra_larga=palabra_mas_larga(cadena)
    #imprimimos la palabra mas larga
    print("La palabra mas larga dentro de la oracion es: ",palabra_larga)
    print("BIG_O:")
    positive_int_generator = lambda n: cadena
    best, others= big_o.big_o(palabra_mas_larga,positive_int_generator)
    print(best)
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
    #Ingreso una oracion por teclado
    cadena=input("Ingrese una cadena:")
    #retorno la cadena ingresada
    return cadena
def encriptar_cadena(cadena):
    """
    Funcion que encripta una cadena ingresada por teclado reemplazando cada letra con un numero

    Parametros:
    ------------
        cadena : str
    Retorna:
    ------------
        cadena_encriptada : str
    """
    # Crea un diccionario para almacenar las letras y sus números correspondientes
    encriptacion = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26',' ':' '}
    # Crea una variable para almacenar la cadena encriptada
    cadena_encriptada = ""
    # Recorre cada caracter de la cadena y reemplaza con el número correspondiente
    for caracter in cadena:
        if caracter.isalpha():
            cadena_encriptada += encriptacion[caracter.lower()]+' '
        else:
            cadena_encriptada+=caracter

    return cadena_encriptada

def desencriptar_cadena(cadena_encriptada):
    """
    Funcion que desencripta una cadena  reemplazando cada numero por una letra

    Parametros:
    ------------
        cadena_encriptada : str
    Retorna:
    ------------
        cadena_desencriptada : str
    """
    # Crea un diccionario para almacenar los numeros y sus letras correspondientes
    desencriptacion = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10':'j', '11':'k', '12':'l', '13':'m', '14':'n', '15':'o', '16':'p', '17':'q', '18':'r', '19':'s', '20':'t', '21':'u', '22':'v', '23':'w', '24':'x', '25':'y', '26':'z',' ':' '}
    # Crea una variable para almacenar la cadena desencriptada
    cadena_desencriptada = ""
    # Recorre cada caracter de la cadena y reemplaza con la letra correspondiente
    for caracter in cadena_encriptada.split():
        if caracter.isnumeric():
            cadena_desencriptada += desencriptacion[caracter]
        else:
            cadena_desencriptada += caracter
    return cadena_desencriptada
if __name__ == '__main__':
    #ingreso una cadena de carcteres
    cadena=leer_variables()
    #encriptamos la cadena
    cadena_encriptada=encriptar_cadena(cadena)
    print("Cadena encriptada: ",cadena_encriptada)
    #desencriptamos la cadena
    cadena_desencriptada=desencriptar_cadena(cadena_encriptada) 
    print("Cadena desencriptada: ",cadena_desencriptada)

    print("BIG_O de encriptar cadena:")
    positive_int_generator = lambda n: cadena
    best, others= big_o.big_o(encriptar_cadena,positive_int_generator)
    print(best)

    print("BIG_O de desencriptar cadena:")
    positive_int_generator = lambda n: cadena_encriptada
    best, others= big_o.big_o(desencriptar_cadena,positive_int_generator)
    print(best)
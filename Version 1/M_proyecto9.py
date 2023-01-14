import re
import big_o
def leer_correo():
    '''
    Funcion que lee una cadena de caracteres(correo)

    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        correo_electronico : str
    '''
    #Ingreso una cadena por teclado
    correo_electronico=input("Ingresa un correo electronicio para validar su formato:")
    #retorno el correo electronigo ingresado por teclado
    return correo_electronico

def validar_formato_de_un_correo_electronico(correo_electronico):
    '''
    Funcion que valida si el formato de un correo electronico ingresado por teclado es valido

    Parametros:
    ------------
        correo_electronico : str 
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #Formato de correo aceptable : nombreaaaa @ xxxmail .com
    patron_correo=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    #buscamos si el formato es una subcadena de la cadena correo_electronico, la funcion imprime un mensaje de si es valido o no el formato
    #del correo
    if re.search(patron_correo, correo_electronico):
        print("El formato del correo electronico es valida")
    else:
        print("El formato del correo electronico no es valida")
if __name__ == '__main__':
    #ingreso el correo electronico por teclado
    correo_electronico=leer_correo()
    #valido si el formato del correo es valido o no
    validar_formato_de_un_correo_electronico(correo_electronico)
    print("BIG_O:")
    positive_int_generator = lambda n: correo_electronico
    best, others= big_o.big_o(validar_formato_de_un_correo_electronico,positive_int_generator)
    print(best)
import big_o
import re
def leer_contraseña():
    '''
    Funcion que lee una cadena
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        contrasena : str
    '''
    #ingreso la contraseña por teclado
    contrasena=input("Ingrese una contraseña para verificar si es segura: ")
    #retorno la cadena
    return contrasena

def verificar_si_contrasena_es_segura(contrasena):
    '''
    Funcion que verifica si una contraseña es segura

    Parametros:
    ------------
        contrasena : str
    Retorna:
    ------------
        0 : int
        1 : int
    '''
    numero=False
    mayuscula = False
    minuscula = False
    caracter_especial = False 
    #si la contraseña tiene menos de 10 caracteres no es valida
    if(len(contrasena)<10):
        return 0
    #compruebo si la contraseña contiene al menos un numero
    for caracter in contrasena:
        if caracter.isdigit():
            numero = True
    #comprueba si la contraseña tiene al menos una letra en mayuscula
    for caracter in contrasena:
        if caracter.isupper():
            mayuscula= True
    #comprueba si la contraseña tiene al menos una letra en minuscula
    for caracter in contrasena:
        if caracter.islower():
            minuscula= True   
    #compruebo si la contraseña tiene al menos un caracter especial
    if re.search("[^a-zA-Z0-9]",contrasena):
        caracter_especial= True 
    #si hay un numero, una mayuscula, una minuscula y un caracter especial entonces la contraseña sera valida
    if(numero==True and mayuscula==True and minuscula==True and caracter_especial==True):
        return 1
    #caso contrario no es segura
    else:
        return 0

if __name__ == '__main__':
    #mientras la contraseña no sea segura sera false
    contrasena=leer_contraseña()
    #verificamos si contraseña es segura
    segura=verificar_si_contrasena_es_segura(contrasena)
    #1 si la contraseña es segura
    if(segura==1):
        print("Su contraseña si es segura")
    #0 si la contraseña no es segura
    if(segura==0):
        print("Su contraseña no es segura")
    #imprimo big_o
    print("BIG_O:")
    positive_int_generator = lambda n: contrasena
    best, others= big_o.big_o(verificar_si_contrasena_es_segura,positive_int_generator)
    print(best)
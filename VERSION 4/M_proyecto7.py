#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda a pausar el codigo
import os
#libreria que me ayuda con el formato de caracteres
import re
"""
Programa que verifica si una contraseña es segura

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
#@profile
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
#@profile
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
    #declaro variables banderas como falsas donde dependieno si una parte del mi codigo cumple un requisito estas cambiaran
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
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como saber si una contraseña es segura?")
    print("     Para que una contraseña sea segura debera cumplir con los siguientes requisitos:")
    print("     1. Debe tener al menos 10 caracteres")
    print("     2. Debe tener al menos una minuscula")
    print("     3. Debe tener al menos una mayuscula")
    print("     4. Debe tener al menos un numero")
    print("     4. Debe tener al menos un caracter especial")
    #pauso el codigo
    os.system("pause")
    #leemos una contraseña
    contrasena=leer_contraseña()
    #verificamos si contraseña es segura
    segura=verificar_si_contrasena_es_segura(contrasena)
    #1 si la contraseña es segura
    if(segura==1):
        print("Su contraseña si es segura")
    #0 si la contraseña no es segura
    if(segura==0):
        print("Su contraseña no es segura")
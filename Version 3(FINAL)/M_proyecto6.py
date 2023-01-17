#libreria que me ayuda con la complejidad de espacio
from memory_profiler import profile 
#libreria que me ayuda con la complejidad del tiempo
import big_o
#libreria que me ayuda a pausar el codigo
import os
"""
Funcion que valida la placa de un automvil y una moto

Autores:
Luis Fernando Cueva Flores
Ednan Josué Merino Calderón

Versión:
VER.1.3
"""
@profile
def validar_numeros_enteros():
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es entero, si lo que se ingresó no es un numero
    entero entonces el usuario tendra que volver a ingresar un numero
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        numero : int
    '''
    #mientras sea verdadero se ingresara un dato en la variable numero, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el usuario debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            numero=int(input())
            #rempemos ciclo repetitivo
            break
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero
@profile
def leer_placa():
    '''
    Funcion que lee una cadena de caracteres
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        placaAuto : str
        placaMoto : str
    '''
    #pregunto al usuario que desea validad, un automovil o una moto
    print("Desea validar la placa de un automovil o una moto? ")
    print("1. Vehiculo")
    print("2. Moto")
    print("Elija una opcion: ",end="")
    #ingresamos la eleccion del usuario
    opcion=validar_numeros_enteros()
    #validamos el rango de las opciones
    while(opcion<1 or opcion>2):
        print("Elija una opcion dentro del rango: ",end="")
        opcion=validar_numeros_enteros()
    if(opcion==1):
        #Ingreso una placa de automovil
        print("AAA-1234")
        placaAuto= input("Ingrese una placa de un automovil para validar: ")
        return placaAuto.upper(),opcion
    if(opcion==2):
        #Ingreso una placa de automovil
        print("AA123A")
        placaMoto= input("Ingrese una placa de una moto para validar: ")
        return placaMoto.upper(),opcion
@profile
def validar_placa_automovil(placa):
    '''
    Funcion que valida la placa de un automvil

    Parametros:
    ------------
        placa :str
    Retorna:
    ------------
        0 : int
        1 : int
    '''
    #si hay mas de 8 caracteres en la placa no sera valida
    if(len(placa)!=8):
        return 0
    #Si los 3 primeros caracteres son letras el cuarto un guion y los ultimos 4 caracteres son numeros
    if(placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha() and placa[3]=='-' and placa[4].isdigit() and  placa[5].isdigit() and placa[6].isdigit() and placa[7].isdigit()):
        #si la primera letra empieza con A,B,C,E,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z la placa es valida
        if(placa[0]=='A' or placa[0]=='B' or placa[0]=='C' or placa[0]=='E' or placa[0]=='G' or placa[0]=='H' or placa[0]=='I' or placa[0]=='J' or placa[0]=='K' or placa[0]=='L' or placa[0]=='M' or placa[0]=='N' or placa[0]=='O' or placa[0]=='P' or placa[0]=='Q' or placa[0]=='R' or placa[0]=='S' or placa[0]=='T' or placa[0]=='U' or placa[0]=='V' or placa[0]=='W' or placa[0]=='X' or placa[0]=='Y' or placa[0]=='Z'):
            return 1
        #Caso contrario es invalida
        else:
            return 0
    #Caso contrario es invalida
    else:
        return 0
@profile
def imprimir_datos_placa(placa):
    '''
    Funcion que imprime los datos de la placa segun sus letras
    
    Parametros:
    ------------
        placa :str
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #dependiendo de la letra imprimo la provincia
    print("Datos de la placa del vehiculo:")
    if(placa[0]=='A'):
        print("Provincia: Azuay")
    if(placa[0]=='B'):
        print("Provincia: Bolivar")
    if(placa[0]=='C'):
        print("Provincia: Carchi")
    if(placa[0]=='E'):
        print("Provincia: Esmeraldas")
    if(placa[0]=='G'):
        print("Provincia: Guayas")
    if(placa[0]=='H'):
        print("Provincia: Chimborazo")
    if(placa[0]=='I'):
        print("Provincia: Santo domingo de los tsachilas")
    if(placa[0]=='J'):
        print("Provincia: Carchi")
    if(placa[0]=='K'):
        print("Provincia: Sucumbios")
    if(placa[0]=='L'):
        print("Provincia: Loja")
    if(placa[0]=='M'):
        print("Provincia: Manabi")
    if(placa[0]=='N'):
        print("Provincia: Napo")
    if(placa[0]=='O'):
        print("Provincia: Oro")
    if(placa[0]=='P'):
        print("Provincia: Pichincha")
    if(placa[0]=='Q'):
        print("Provincia: Orellana")
    if(placa[0]=='R'):
        print("Provincia: Los Rios")
    if(placa[0]=='S'):
        print("Provincia: Pastaza")
    if(placa[0]=='T'):
        print("Provincia: Tungurahua")
    if(placa[0]=='U'):
        print("Provincia: Cañar")
    if(placa[0]=='V'):
        print("Provincia: Morona Santiago")
    if(placa[0]=='W'):
        print("Provincia: Galapagos")
    if(placa[0]=='X'):
        print("Provincia: Cotopaxi")
    if(placa[0]=='Y'):
        print("Provincia: Santa Elena")
    if(placa[0]=='Z'):
        print("Provincia: Zamora Chinchipe")
    #dependiendo de la segunda letra imprimo el tipo de vehiculo
    if(placa[1]=='A' or placa[1]=='U' or placa[1]=='Z'):
        print("Tipo de vehiculo: Bus/Taxi")
    elif(placa[1]=='E'):
        print("Tipo de vehiculo: Propiedad del gobierno central")
    elif(placa[1]=='M'):
        print("Tipo de vehiculo: GAD ")
    else:
        print("Tipo de vehiculo: Particular")
@profile
def validar_placa_moto(placa):
    '''
    Funcion que valida la placa de una moto

    Parametros:
    ------------
        placa :str
    Retorna:
    ------------
        0 : int
        1 : int 
    '''
    #si hay mas de 6 caracteres en la placa no sera valida
    if(len(placa)!=6):
        return 0

    #Si los 2 primeros caracteres son letras, el tercer, cuarto y quinto caracter son numero y el ultimo caracter es una letra
    if(placa[0].isalpha() and placa[1].isalpha() and placa[2].isdigit() and placa[3].isdigit() and placa[4].isdigit() and placa[5].isalpha()):
        #si la primera letra empieza con A,B,C,E,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z la placa es valida
        if(placa[0]=='A' or placa[0]=='B' or placa[0]=='C' or placa[0]=='E' or placa[0]=='G' or placa[0]=='H' or placa[0]=='I' or placa[0]=='J' or placa[0]=='K' or placa[0]=='L' or placa[0]=='M' or placa[0]=='N' or placa[0]=='O' or placa[0]=='P' or placa[0]=='Q' or placa[0]=='R' or placa[0]=='S' or placa[0]=='T' or placa[0]=='U' or placa[0]=='V' or placa[0]=='W' or placa[0]=='X' or placa[0]=='Y' or placa[0]=='Z'):
            return 1
        #Caso contrario es invalida
        else:
            return 0
    #Caso contrario es invalida
    else:
        return 0

if __name__ == '__main__':
    #Imprimo la bienvenida y explico como funciona el programa
    print("Bienvenido")
    print("Como funciona este programa?")
    print("     Este programa esta hecho para validar si una placa de un auto o moto son validos")
    print("     con los datos de la placa si es valido imprimira que tipo de vehiculo es y de que provincia proviene")
    #pauso el codigo
    os.system("pause")
    #leo la placa y retorno la placa y la opcion de si es moto o auto
    placa,opcion=leer_placa()
    #imprimo la placa ingresada
    print("Placa ingresada: ",placa)
    #si la placa es de un auto
    if(opcion==1):
        #validamos la placa
        valida=validar_placa_automovil(placa)
        #si el valor retornado es 0
        if(valida==0):
            #imprimir placa no es valida
            print("Su placa no es valida")
        #si el valor retornado es 1
        if(valida==1):
            #imprimir placa si es valida
            print("Su placa si es valida")
            #imprimo los datos de la placa
            imprimir_datos_placa(placa)
        print("BIG_O validar_placa_automovil:")
        positive_int_generator = lambda n: placa
        best, others= big_o.big_o(validar_placa_automovil,positive_int_generator)
        print(best)
    #si la placa es de una moto
    if(opcion==2):
        #validamos la placa
        valida=validar_placa_moto(placa)
        #si el valor retornado es 0
        if(valida==0):
            #imprimir placa no es valida
            print("Su placa no es valida")
        #si el valor retornado es 1
        if(valida==1):
            #imprimir placa si es valida
            print("Su placa si es valida")
            #imprimo los datos de la placa
            imprimir_datos_placa(placa)
        print("BIG_O validar_placa_moto:")
        positive_int_generator = lambda n: placa
        best, others= big_o.big_o(validar_placa_moto,positive_int_generator)
        print(best)
import big_o
def leer_cedula():
    '''
    Funcion que lee una cadena de caracteres
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        cedula : str
    '''
    #Ingreso una cadena por teclado
    cedula=input("Ingresa una cedula:")
    #retorno la oracion 
    return cedula
def validacion_cedula(cedula):
    '''
    Funcion que valida si la cedula ingresada es valida o no

    Parametros:
    ------------
        cedula : str
    Retorna:
    ------------
        0 : int 
        1 : int
    '''
    #si el tamaño de la cedula es mayor a 10 caracteres  o menor a 10 es falsa
    if(len(cedula)>10 or len(cedula)<10):
        return 0
    #si en la lista hay una letra, la cedula es falsa
    for char in cedula:
        if char.isalpha():
            return 0
    #multiplicos los numeros que esten en posiciones impares de la cedula por 2
    impar1=int(cedula[0])*2
    impar2=int(cedula[2])*2
    impar3=int(cedula[4])*2
    impar4=int(cedula[6])*2
    impar5=int(cedula[8])*2
    if(impar1>9):
        impar1=impar1-9
    if(impar2>9):
        impar2=impar2-9
    if(impar3>9):
        impar3=impar3-9
    if(impar4>9):
        impar4=impar4-9
    if(impar5>9):
        impar5=impar5-9
    suma_impares=impar1+impar2+impar3+impar4+impar5
    #convierto la cadena en entero
    par1=int(cedula[1])
    par2=int(cedula[3])
    par3=int(cedula[5])
    par4=int(cedula[7])
    #sumo los numeros en las posiciones pares de la ceula
    suma_pares=par1+par2+par3+par4
    suma_total=suma_pares+suma_impares
    #calculo el modulo
    modulo=suma_total%10

    #convierto el ultimo caracter de la cadena en digito
    ultimo_digito=int(cedula[9])
    #si el modulo es diferente de cero
    if(modulo>0):
        #restamos 10 menos el valo de modulo
        modulo=10-modulo
        #si el valor de esa resta es igual al ultimo digito de la cedula entonces es valida, caso contrario no
        if(modulo==ultimo_digito):
            return 1
        else:
            return 0
    #si la cedula es cero verificamos si el cero es igual al ultimo digito de la cedula entonces es valida, caso contrario no
    else:
        if(modulo==ultimo_digito):
            return 1
        else:
            return 0
    
if __name__ == '__main__':
    #ingreso la cedula por teclado
    cedula=leer_cedula()
    #validamos cedula
    valida=validacion_cedula(cedula)
    if(valida==1):
        print("Su cedula si es valida")
    if(valida==0):
        print("Su cedula no es valida")
    print("BIG_O:")
    positive_int_generator = lambda n: cedula
    best, others= big_o.big_o(validacion_cedula,positive_int_generator)
    print(best)
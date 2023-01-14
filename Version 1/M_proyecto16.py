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
        #en caso de que no se haya ingresado un numero entero se imprimira un mensaje diciendo que no se ingreso un enetero
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero
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
    #ingreso un numero el cual sera el tamañao de las palabras que podran imprimirse
    print("Ingrse el tamaño(numero entero) con las que se imprimira las palabras que tengan ese tamaño: ",end="")
    nLetras=validar_numeros_enteros()
    while(nLetras<1):
        print("Solo ingrese numeros positivos: ",end="")
        nLetras=validar_numeros_enteros()
    #retorno la oracion y nletras
    return cadena,nLetras

def encontrar_palabras_con_tamaño_especifico(cadena, nLetras):
    palabras = cadena.split()
    palabras_tamaño_indicado = []
    for palabras in palabras:
        if len(palabras) == nLetras:
            palabras_tamaño_indicado.append(palabras)
    print("Palabras con el tamaño ",nLetras,": ", palabras_tamaño_indicado)
if __name__ == '__main__':
    #leo una cadena de palabras
    cadena,nLetras=leer_cadena()
    encontrar_palabras_con_tamaño_especifico(cadena,nLetras)

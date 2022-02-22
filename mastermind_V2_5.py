import random

""" -------------------Variables globales predefinidas--------------------- """

largoCodigo=4 #Largo que tendra el codigo
Tletras='abcdefgh' #Letras permitidas dentro del codigo
maxIntentos=10 #antidad maima de intentos permitidos
intento=1 #Valor con el que comenzara las repeticiones
buenos=0 #valor de comienzo de aciertos buenos
regulares=0 #Valor de comienzo de aciertos regulares
perdio=True #Variable default de la variable que muestra el estado del jugador en el juego
codigoValido=False#Estado por defecto que luego se husara para determinar si el codigo que se ingresa es correcto

""" ---------------------------FUNCIONES---------------------------- """

def generaCodigoPC():
    """ Se forma el codigo a adivinar y se devuelve mediante return """
    global Tletras, largoCodigo
    i=1
    codigoPC=''
    while (i <=largoCodigo):
        codigoPC+=random.choice(Tletras)
        i+=1
    return codigoPC


def chequeoCodigoUsuario(codigoUsuario):
    """ Se comprueba que el codigo tenga el largo de letras y letras adecuadas """
    global codigoValido
    codigoValido=False
    for c in codigoUsuario:
        if (c not in Tletras):
            return False
    if (len(codigoUsuario)!=largoCodigo):
        return False
    else:
        codigoValido=True
        return True


def puntage(codigoUsuario):

    """ Se calcula cantidad de aciertos del jugador """
    global buenos, regulares, codigoPC 
    evaluadasBuenas=[False,False,False,False]
    buenos=0
    regulares=0
    j1=0
    j2=0

    """ Se recorren los dos codigos al mismo tiempo para encontrar las coincidencias con el mismo indice (buenos) """
    while (j1<largoCodigo):
        if (codigoUsuario[j1]==codigoPC[j1]):
            buenos+=1
            evaluadasBuenas[j1]=True
        j1+=1

    """ Se recorren los dos codigos al mismo tiempo para encontrar las coincidencias con distinto indice (regulares) """
    for c1 in codigoPC:
        for c2 in codigoUsuario:
            if (c2==c1) and not evaluadasBuenas[j2]:
                regulares+=1
        j2+=1


def corroboraGano():
    """ Se comprueba si la cantidad de buenos es igual al largo del codigo y se devuelve True en caso afirmativo o False en caso negativo """
    global buenos, perdio, largoCodigo
    if (buenos==largoCodigo):
        perdio=False
        return True

""" ---------------------------Bloque global---------------------------- """

codigoPC=generaCodigoPC()

while intento <= maxIntentos:
    print('Intento {}'.format(intento))

    codigoUsuario=input('Ingresa un codigo >> ')

    """ Se envia el codigo a la funcion encargada de validar o no el codigo. En caso negativo se muestra mensaje de error y se pide que se reingrese """
    chequeoCodigoUsuario(codigoUsuario) #Corregir no funciona, da fuera del rango en evaludads porque toma codigos de mas de 4 digitos
    while not codigoValido:
        chequeoCodigoUsuario(input('Codigo inadecuado. Ingresa un codigo de {} letras entre la {} y la {} >> '.format(largoCodigo, Tletras[0], Tletras[-1])))

    """ Se envia el codigo del usuario a la funcion encargada de establecer el puntage """
    puntage(codigoUsuario)
    print('Buenos: {}, Regulares: {}'.format(buenos, regulares))

    if corroboraGano():
        print('GANASTEEE!!')
        break

    intento+=1 #Se suma el intento para avanzar en la iteracion del while

""" ---------------------------Fuera de bloque global---------------------------- """

if perdio:
    print('Perdiste!!. El codigo era {}'.format(codigoPC))
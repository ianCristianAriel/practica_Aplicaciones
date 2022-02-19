from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

raiz.resizable(False, False)

resultado=0
operacion=''
op=False

#PANTALLA
numeroPantalla=StringVar()

def default():
    global operacion
    global resultado
    operacion=''
    op=False
    resultado=0

def suma(num):
    global op
    global operacion
    global resultado
    igualResultado(num)
    operacion='suma'
    op=True

def resta(num):
    global op
    global operacion
    global resultado
    igualResultado(num)
    operacion='resta'
    op=True

def multi(num):
    global op
    global operacion
    global resultado
    igualResultado(num)
    operacion='multi'
    op=True

def igual(num):
    global operacion 
    global resultado
    global op
    igualResultado(num)
    default()
    op=True

def igualResultado(num):
    global resultado
    if operacion=='suma':
        resultado+=int(num)
        numeroPantalla.set(resultado)
    elif operacion=='resta':
        resultado=resultado-int(num)
        numeroPantalla.set(resultado)
    elif operacion=='multi':
        resultado=resultado*int(num)
        numeroPantalla.set(resultado)
    else:
        resultado=int(num)


def numeroPulsado(num):
    global operacion
    global resultado
    global op
    if op:
        numeroPantalla.set(num)
        op=False
    else:
        numeroPantalla.set(numeroPantalla.get()+num)


pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=0, column=1, columnspan=4, padx=5, pady=5)
pantalla.config(bg='grey', fg='black', justify='right')
#NUMEROS
#Fila 4 de botones
cero=Button(miFrame, text="0", width=3, command=lambda: numeroPulsado('0'))
cero.grid(row=4, column=1, padx=5, pady=5)

coma=Button(miFrame, text=",", width=3, command=lambda: numeroPulsado('.'))
coma.grid(row=4, column=2, padx=5, pady=5)

igualBoton=Button(miFrame, text="=", width=3, command=lambda:igual(numeroPantalla.get()))
igualBoton.grid(row=4, column=3, padx=5, pady=5)

restaBoton= Button(miFrame, text='-', width=3, command=lambda:[resta(numeroPantalla.get())])
restaBoton.grid(row=4, column=4, padx=5, pady=5)

#Fila 3 de botones
uno=Button(miFrame, text="1", width=3, command=lambda: numeroPulsado('1'))
uno.grid(row=3, column=1, padx=5, pady=5)

dos=Button(miFrame, text="2", width=3,command=lambda: numeroPulsado('2'))
dos.grid(row=3, column=2, padx=5, pady=5)

tres=Button(miFrame, text="3", width=3, command=lambda: numeroPulsado('3'))
tres.grid(row=3, column=3, padx=5, pady=5)

sumaBoton=Button(miFrame, text='+', width=3, command=lambda:suma(numeroPantalla.get()))
sumaBoton.grid(row=3, column=4, padx=5, pady=5)

#Fila 2 de botones
cuatro=Button(miFrame, text="4", width=3, command=lambda: numeroPulsado('4'))
cuatro.grid(row=2, column=1, padx=5, pady=5)

cinco=Button(miFrame, text="5", width=3, command=lambda: numeroPulsado('5'))
cinco.grid(row=2, column=2, padx=5, pady=5)

seis=Button(miFrame, text="6", width=3, command=lambda: numeroPulsado('6'))
seis.grid(row=2, column=3, padx=5, pady=5)

multiplicar=Button(miFrame, text='*', width=3, command=lambda:multi(numeroPantalla.get()))
multiplicar.grid(row=2, column=4, padx=5, pady=5)

#Fila uno de botones
siete=Button(miFrame, text="7", width=3, command=lambda: numeroPulsado('7'))
siete.grid(row=1, column=1, padx=5, pady=5)

ocho=Button(miFrame, text="8", width=3, command=lambda: numeroPulsado('8'))
ocho.grid(row=1, column=2, padx=5, pady=5)

nueve=Button(miFrame, text="9", width=3, command=lambda: numeroPulsado('9'))
nueve.grid(row=1, column=3, padx=5, pady=5)

borrar=Button(miFrame, text='Del', width=3, command=lambda:[numeroPantalla.set(''), default()])
borrar.grid(row=1, column=4, padx=5, pady=5)

raiz.mainloop()
from tkinter import *
from tkinter import messagebox
import sqlite3

#Funcionalidades base de datos (BBDD)---------------------------------------------------------

##Conectar
def conectar():
    try:
        miConexion = sqlite3.connect('usuarios.db')
        miCursor= miConexion.cursor()
        miCursor.execute("CREATE TABLE DATOS_USUARIOS(Id primary key integer autoincrement, Nombre varchar(50), Apellido varchar(10), E-mail varchar (50), Comentario varchar(100)")
        miConexion.commit()
        messagebox.showinfo('BBDD', 'BBDD Creada con exito')
    except:
        messagebox.showwarning('Error', 'BBDD ya existente')

#Crear
def crear():
    miConexion=sqlite3.connect('usuarios.db')
    miCursor=miConexion.cursor()
    usuario= variableNombre.get(), variableApellido.get(), variableEmail.get(), variablePassword.get(), variableComentario.get("1.0", END)
    miCursor.execute('INSERT INTO DATOS_USUARIOS VALUES (NULL,?,?,?,?,?)',(usuario))
    miConexion.commit()

#Leer
def leer():
    miConexion=sqlite3.connect('usuarios.db')
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('select * from DATOS_USUARIOS where Id='+ variableId.get()) #Acomodar lectura por id
        usuario_Leido=(miCursor.fetchall())
        for u in usuario_Leido:
            variableId.set(usuario_Leido[0])
            variableNombre.set(usuario_Leido[1])
            variableApellido.set(usuario_Leido[2])
            variableEmail.set(usuario_Leido[3])
            variablePassword.set(usuario_Leido[4])
            entradaComentario.delete(1.0, END)
            entradaComentario.insert(1.0, usuario_Leido[5])
        miConexion.commit()
        messagebox.showinfo('Exito', 'Datos obtenidos con exito!')
    except:
        messagebox.showerror('Error', 'El valor de Id indicado no existe')

#Actualizar
def actualizar():
    miConexion=sqlite3.connect('usuarios.db')
    miCursor=miConexion.cursor()
    try:
        usuario_Para_Actualizar=[
            variableNombre.get(), variableApellido.get(), variableEmail.get(), variablePassword.get(), entradaComentario.get(1.0, END)
        ]
        miCursor.execute('UPDATE DATOS_USUARIOS set Nombre=?, Apellido=?, E-mail=?, Password=?, Comentario=? where Id='+variableId.get(), usuario_Para_Actualizar)
        miConexion.commit()
        mesagebox.showinfo('Exito', 'Datos actualizados con exito')
    except:
        messagebox.showwarning('Error', 'Id de registro inexistente')

#Eliminar
def eliminar():
    miConexion=sqlite3.connect('usuarios.db')
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('DELETE FROM DATOS_USUARIOS WHERE ID='+ variableId.get())
        miConexion.commit()
        messagebox.showinfo('Exito', 'Registro eliminado con exito!')
    except:
        messagebox.showwarning('Error', 'Id de registro inexistente')


#Funcionalidades Menu---------------------------------------------------------
def borrar_Campos():
    variableId.set('')
    variableNombre.set('')
    variableApellido.set('')
    variableEmail.set('')
    variablePassword.set('')
    entradaComentario.delete(1.0, END)

def salir():
    valor=messagebox.askquestion('Salir', 'Deseas salir de la aplicacion')
    if valor=='yes':
        raiz.destroy()

#--------------------------------------------------------------------------------------------------------------
raiz=Tk()

variableId=StringVar()
variableNombre=StringVar()
variableApellido=StringVar()
variableEmail=StringVar()
variablePassword=StringVar()
variableComentario=StringVar()

#Barra menu--------------------------------------------------------------------

barraMenu=Menu(raiz)

##BBDD
bbddMenu=Menu(barraMenu, tearoff=0)
###BBDD.Conectar
bbddMenu.add_command(label='Conectar', command=conectar)
###BBDD.Divisor
bbddMenu.add_separator()
###BBDD.Salir
bbddMenu.add_command(label='Salir', command=salir)

##Borrar
borrarMenu=Menu(barraMenu, tearoff=0)
###Borrar.Borrar campos
borrarMenu.add_command(label='Borrar campos',command=borrar_Campos)

##Ayuda
ayudaMenu=Menu(barraMenu, tearoff=0)
###Ayuda.Acerca de
ayudaMenu.add_command(label='Acerca de ')

bbddMenu.add_cascade(label='BBDD', menu=bbddMenu)
barraMenu.add_cascade(label='Borrar', menu=borrarMenu)
ayudaMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

raiz.config(menu=barraMenu)
#---------------------------------------------------------------------------------------

#Labels con texto---------------------------------------------------------------------------

miFrame = Frame(raiz)
miFrame.pack()

##id
textoId=Label(miFrame, text='Id: ')
textoId.grid(row=0, column=0, sticky='e', padx=10, pady=10)

##Nombre
textoNombre=Label(miFrame, text='Nombre: ')
textoNombre.grid(row=1, column=0, sticky='e', padx=10, pady=10)

##apellido
textoApellido=Label(miFrame, text='Apellido: ')
textoApellido.grid(row=2, column=0, sticky='e', padx=10, pady=10)

##Email
textoEmail=Label(miFrame, text='Email: ')
textoEmail.grid(row=3, column=0, sticky='e', padx=10, pady=10)

##Password
textoPasword=Label(miFrame, text='Pasword: ')
textoPasword.grid(row=4, column=0, sticky='e', padx=10, pady=10)

##Comentario
textoComentario=Label(miFrame, text='Comentario: ')
textoComentario.grid(row=5, column=0, sticky='e', padx=10, pady=10)

#Entradas
##id
entradaId=Entry(miFrame, textvariable=variableId)
entradaId.grid(row=0, column=1, padx=10, pady=10)

##Nombre
entradaNombre=Entry(miFrame, textvariable=variableNombre)
entradaNombre.grid(row=1, column=1, padx=10, pady=10)

##apellido
entradaApellido=Entry(miFrame, textvariable=variableApellido)
entradaApellido.grid(row=2, column=1, padx=10, pady=10)

##Email
entradaEmail=Entry(miFrame, textvariable=variableEmail)
entradaEmail.grid(row=3, column=1, padx=10, pady=10)

##Pasword
entradaPassword=Entry(miFrame, textvariable=variablePassword)
entradaPassword.grid(row=4, column=1, padx=10, pady=10)
entradaPassword.config(fg='red', show='*')

##Comentario
entradaComentario=Text(miFrame, width=15, height=5)
entradaComentario.grid(row=5, column=1, pady=10, padx=10)

scrollVerticalComentario=Scrollbar(miFrame, command=entradaComentario.yview)
scrollVerticalComentario.grid(row=5, column=2, sticky='nsew', padx=10, pady=10)

entradaComentario.config(yscrollcommand=scrollVerticalComentario.set)
#----------------------------------------------------------------------------------

#Botones, CRUD---------------------------------------------------------------------------------
miFrameBotones=Frame(raiz)
miFrameBotones.pack() 
##Crear
boton_Crear=Button(miFrameBotones, text='Crear', command=crear)
boton_Crear.grid(row=1, column=1, sticky='e', padx=10, pady=10)
##Leer
boton_Leer=Button(miFrameBotones, text='Leer', command=leer)
boton_Leer.grid(row=1, column=2, sticky='e', padx=10, pady=10)
##Actualizar
boton_Actualizar=Button(miFrameBotones, text='Actualizar', command=actualizar)
boton_Actualizar.grid(row=1, column=3, sticky='e', padx=10, pady=10)
##Boorar
boton_Eliminar=Button(miFrameBotones, text='Eliminar', command=eliminar)
boton_Eliminar.grid(row=1, column=4, sticky='e', padx=10, pady=10)


#-------------------------------------------------------------------------------------

raiz.mainloop()
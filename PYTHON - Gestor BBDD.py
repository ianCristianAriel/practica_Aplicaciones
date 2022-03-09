#Importando librerias #-----------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import sqlite3

root= Tk()
#_________________________________________________________________________________

variableId=IntVar()
variableNombre=StringVar()
variableApellido=StringVar()
variableEmail=StringVar()
variablePassword=StringVar()

#---------------------------------------------------------------------------------------
#3- Funciones #-----------------------------------------------------

#Funciones.Menu
def Conectar():
    try:
        conexion= sqlite3.connect('usuarios.db')
        cursor=conexion.cursor()
        cursor.execute('create table datos_Usuarios(id integer primary key autoincrement, Nombre varchar(10), Apellido varchar (10), Email varchar(50), Password varchar (50), Comentario varchar (100))')
        conexion.commit()
        messagebox.showinfo('Exito', 'BBDD creada exitosamente')
    except:
        messagebox.showerror('Error', 'La base de datos ya existe')


def Salir():
    if messagebox.askyesno('Salir', 'Deseas salir de la aplicacion?'):
        root.destroy()


def borrar_Campos():
    variableId.set('')
    variableNombre.set('')
    variableApellido.set('')
    variableEmail.set('')
    variablePassword.set('')
    entrada_Comentario.delete(1.0, END)
    messagebox.showinfo('Exito', 'Se borraron los campos!')


def acercaDe():
    messagebox.showinfo('Acerca de..', 'Aplicación creada por Ian Yané, tecnico superior en ciencia de datos y inteligencia artificial')


#funciones.Botones
def Crear():
    try:
        conexion= sqlite3.connect('usuarios.db')
        cursor = conexion.cursor()
        cursor.execute('insert into datos_Usuarios values(NULL, ?, ?, ?, ?, ?)', (variableNombre.get(), variableApellido.get(), variableEmail.get(), variablePassword.get(), entrada_Comentario.get(1.0, END)) )
        conexion.commit()
        messagebox.showinfo('Exito', 'La tabla se creo correctamente')
    except:
        messagebox.showerror('Error', 'Ya se creo una tabla con el mismo id')



def Leer():
    try:
        conexion= sqlite3.connect('usuarios.db')
        cursor=conexion.cursor()
        cursor.execute('select * from datos_Usuarios where id='+str(variableId.get()))
        datos_Usuarios_leido= cursor.fetchall()
        variableNombre.set(datos_Usuarios_leido[0][1])
        variableApellido.set(datos_Usuarios_leido[0][2])
        variableEmail.set(datos_Usuarios_leido[0][3])
        variablePassword.set(datos_Usuarios_leido[0][4])
        entrada_Comentario.delete(1.0, END)
        entrada_Comentario.insert(1.0, datos_Usuarios_leido[0][5])
        conexion.commit()
        messagebox.showinfo('Exito', 'A continuacion se muestra los datos para el id:'+str(variableId.get()))
    except:
        messagebox.showerror('Error', 'La tabla no se encontro. Compruebe con que es correcto el numero ingresado')



def Actualizar():
    try:
        conexion= sqlite3.connect('usuarios.db')
        cursor= conexion.cursor()
        cursor.execute('update datos_Usuarios set Nombre=?, Apellido=?, Email=?, Password=?, Comentario=?', (variableNombre.get(), variableApellido.get(), variableEmail.get(), variablePassword.get(), entrada_Comentario.get(1.0, END)))
        conexion.commit()
        messagebox.showinfo('Exito', 'Se actualizo la BBDD')
    except:
        messagebox.showerror('Error', 'No se pudo actualizar el registro')

def Eliminar():
    try:
        conexion= sqlite3.connect('usuarios.db')
        cursor= conexion.cursor()
        cursor.execute('delete from datos_Usuarios where id='+str(variableId.get()))
        conexion.commit()
        messagebox.showinfo('Exito', 'Se elimino el registro correctamente')
    except:
        messagebox.showerror('No se pudo eliminar los campos, ingresa un id correcto')


#_________________________________________________________________________________
#Barra de menu -------------------------------------------------------------------------
barraMenu=Menu(root)

#Menu.BBDD
menu_BBDD=Menu(barraMenu, tearoff=0)
menu_BBDD.add_command(label='Conectar', command=Conectar)
menu_BBDD.add_separator()
menu_BBDD.add_command(label='Salir', command=Salir)

#Menu.Borrar
menu_Borrar=Menu(barraMenu, tearoff=0)
menu_Borrar.add_command(label='Borrar campos', command=borrar_Campos)

#Menu.Ayuda
menu_Ayuda=Menu(barraMenu, tearoff=0)
menu_Ayuda.add_command(label='Acerca de..', command=acercaDe)
menu_Ayuda.add_command(label='')

barraMenu.add_cascade(label='BBDD', menu=menu_BBDD)
barraMenu.add_cascade(label='Borrar', menu=menu_Borrar)
barraMenu.add_cascade(label='Ayuda', menu=menu_Ayuda)

root.config(menu=barraMenu)
#Referencias de las entradas ____________________________________________________

miFrame=Frame(root)
miFrame.pack()

id = Label(miFrame, text='Id: ')
id.grid(row=1, column=0, sticky='e',padx=5, pady=5 )

nombre = Label(miFrame, text='Nombre: ')
nombre.grid(row=2, column=0, sticky='e',padx=5, pady=5 )

Apellido = Label(miFrame, text='Apellido: ')
Apellido.grid(row=3, column=0, sticky='e',padx=5, pady=5 )

E_mail = Label(miFrame, text='E-mail: ')
E_mail.grid(row=4, column=0, sticky='e',padx=5, pady=5 )

password= Label(miFrame, text='Password: ')
password.grid(row=5, column=0, sticky='e',padx=5, pady=5 )

comentario = Label(miFrame, text='Comentario:')
comentario.grid(row=6, column=0, sticky='e',padx=5, pady=5 )

#Entradas de texto
entrada_Id=Entry(miFrame, textvariable=variableId)
entrada_Id.grid(row=1, column=1, padx=5, pady=5)

entrada_Nombre=Entry(miFrame, textvariable=variableNombre)
entrada_Nombre.grid(row=2, column=1, padx=5, pady=5)

entrada_Apellido=Entry(miFrame, textvariable=variableApellido)
entrada_Apellido.grid(row=3, column=1, padx=5, pady=5)

entrada_E_mail=Entry(miFrame, textvariable=variableEmail)
entrada_E_mail.grid(row=4, column=1, padx=5, pady=5)

entrada_Password=Entry(miFrame, textvariable=variablePassword)
entrada_Password.grid(row=5, column=1, padx=5, pady=5)
entrada_Password.config(fg='red', show='*')

entrada_Comentario=Text(miFrame, width=15, height=5)
entrada_Comentario.grid(row=6, column=1, padx=5, pady=5)
scrollVerticalComentario=Scrollbar(miFrame, command=entrada_Comentario.yview)
scrollVerticalComentario.grid(row=6, column=2, sticky='nsew', padx=10, pady=10)
entrada_Comentario.config(yscrollcommand=scrollVerticalComentario.set)

#Botones-----------------------------------------------------------------------
frame_Botones=Frame(root)
frame_Botones.pack()

boton_Crear=Button(frame_Botones, text='Crear', command=Crear)
boton_Crear.grid(row=0, column=0, padx=5, pady=5)

boton_Leer=Button(frame_Botones, text='Leer', command=Leer)
boton_Leer.grid(row=0, column=1,padx=5, pady=5)

boton_Actualizar=Button(frame_Botones, text='Actualizar', command=Actualizar)
boton_Actualizar.grid(row=0, column=2,padx=5, pady=5)

boton_Eliminar=Button(frame_Botones, text='Eliminar', command=Eliminar)
boton_Eliminar.grid(row=0, column=3, padx=5, pady=5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

#---------------------------------------------------------------------------------------

#Fin del codigo-------------------------------------------------------------------------
root.mainloop()

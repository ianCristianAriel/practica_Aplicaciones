import pymongo
from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox
import os.path

#Quiero un gestor que :
""" 
Tenga manu para: 1)crear base de datos, 2)Para salir
Tenga datos en forma de labels y entryes: 1)Id, 2)Nombre, 3)Apellido, 4)Comentario
Botones encargados de las funciones: 1)Crear registro, 2)Leer registro 3)Actualizar registro, 4)Eliminar registro
"""
#General:

uri='mongodb://localhost'
cliente=MongoClient(uri)
try:
    db=cliente['base_Usuarios']
    coleccion= db['datos_Usuarios']
except:
    coleccion= db['datos_Usuarios']

ventana=Tk()

identificador_variable=IntVar()
nombre_variable=StringVar()
apellido_variable=StringVar()

#Back-end

##funciones----------------------------------------------------------------------------------------------------------------------
###Base de datos-----------------------------------------------------------------------------------------------------------------

def nueva_base():
    i=1
    j=False
    while j==False:
        try:
            db=cliente['base_Usuarios'+str(i)]
            j=True
        except:
            i+=1
    coleccion= db['datos_Usuarios']

def crear_registro():
    documento={
        '_id':identificador_variable.get(),
        'Nombre':nombre_variable.get(),
        'Apellido':apellido_variable.get(),
        'Comentario':comentario.get(1.0, END)
    }
    try:
        coleccion.insert_one(documento)
    except:
        messagebox.showerror('Id erroneo', 'El id ingresado ya existe')

def leer_registro():
    datos_usuario=coleccion.find({'_id':identificador_variable.get()})[0]
    nombre_variable.set(datos_usuario['Nombre'])
    apellido_variable.set(datos_usuario['Apellido'])
    comentario.delete(1.0,END)
    comentario.insert(datos_usuario['Comentario'])

def actualizar_registro():
    comentario.delete(1.0,END)
    coleccion.update_one({'_id':identificador_variable.get()}, {'$set':{
        'Nombre':nombre_variable.get(), 
        'Apellido': apellido_variable.get(), 
        'Comentario':comentario.get(1.0,END)
    }})

def eliminar_registro():
    coleccion.delete_one({'_id':identificador_variable.get()})

def funcion_salir():
    ventana.destroy()

def acerca_de():
    messagebox.showinfo('Info', 'Creado con el fin de afianzar conocimientos sobre pymongo')

#Front-end

##Menu----------------------------------------------------------------------------------------------------------------------

barra_menu=Menu(ventana)

###Base
base=Menu(barra_menu, tearoff=0)
####Nueva
base.add_command(label='Nueva Base', command=lambda: nueva_base())

###Salir
salir=Menu(barra_menu, tearoff=0)
####Salir
salir.add_command(label='Salir', command=lambda: funcion_salir())
####Acerca de..
salir.add_command(label='Acerca de..', command=lambda: acerca_de())

barra_menu.add_cascade(label='Base', menu=base)
barra_menu.add_cascade(label='salir', menu=salir)

ventana.config(menu=barra_menu)
##Datos---------------------------------------------------------------------------------------------------------------------

datos_frame=Frame(ventana)
datos_frame.pack()

###Labels
####ID
Label(datos_frame, text='Identificador: ').grid(column=0, row=0)
####Nombre
Label(datos_frame, text='Nombre: ').grid(column=0, row=1)
####Apellido
Label(datos_frame, text='Apellido: ').grid(column=0, row=2)
####Comentario
Label(datos_frame, text='Comentario: ').grid(column=0, row=3)

###Entryes
####ID
identificador=Entry(datos_frame, textvariable=identificador_variable)
identificador.grid(column=1, row=0)
####Nombre
nombre=Entry(datos_frame, textvariable=nombre_variable)
nombre.grid(column=1, row=1)
####Apellido
apellido=Entry(datos_frame, textvariable=apellido_variable)
apellido.grid(column=1, row=2)
####Comentario
comentario=Text(datos_frame, height=5, width=15)
comentario.grid(column=1, row=3)
scrollbar_vertical_comentario=Scrollbar(datos_frame, command=comentario.yview)
scrollbar_vertical_comentario.grid(column=2, row=3, sticky='nsew')
comentario.config(yscrollcommand=scrollbar_vertical_comentario.set)

##Botones-------------------------------------------------------------------------------------------------------------------

cruds_frame=Frame(ventana)
cruds_frame.pack()
###Crear
crear=Button(cruds_frame, text='Crear',command=crear_registro)
crear.grid(column=0, row=0)
###Leer
leer=Button(cruds_frame, text='Leer', command=leer_registro)
leer.grid(column=1, row=0)
###Actualizar
actualizar=Button(cruds_frame, text='Actualizar', command=actualizar_registro)
actualizar.grid(column=2, row=0)
###Borrar
borrar=Button(cruds_frame, text='Borrar', command=eliminar_registro)
borrar.grid(column=3, row=0)

#----------------------------------------------------FIN DEL CODIGO---------------------------------------------------------
ventana.mainloop()
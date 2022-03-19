from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId

#Variables globales:
id_Usuario=''

#Creacion base de datos y coleccion
mongo_Uri= 'mongodb://localhost'

cliente= MongoClient(mongo_Uri)

db= cliente['gestorUsuarios']

coleccion=db['Usuarios']

#Funciones
def crearUsuario():#Crea un alumno y lo agrega a la base de datos
    coleccion.insert_one(
        {
            'Nombre':nombre.get(),
            'Apellido':apellido.get(),
            'Edad':edad.get()
            })
    datosTabla()


def actualizarDatos(id, nombre, apellido, edad):#Actualiza los datos de un registro
    coleccion.update_one({'_id':id}, {'$set':{'Nombre':nombre, 'Apellido':apellido, 'Edad':edad}})


def eliminarUsuarios():#Elimina los datos de un registro
    global id_Usuario
    coleccion.delete_one({'_id':id_Usuario})
    datosTabla()


def datosTabla():#mustra los datos almacenados en la base de datos
    try:
        datosAntiguos=tabla.get_children()
        for datoA in datosAntiguos:
            tabla.delete(datoA)
        datos= coleccion.find()
        for d in datos:
            tabla.insert('',0,text=d['_id'], values=d['Nombre'])
        nombre.delete(0,END)
        apellido.delete(0,END)
        edad.delete(0,END)
    except:
        messagebox.showerror('Error', 'los campos no pueden estar vacios')


def dobleClickTabla(event):#Al hacer doble click en la info de un registro, mustra dicha info sobre cada entry
    global id_Usuario
    id_Usuario=ObjectId(str(tabla.item(tabla.selection())['text'])) 
    usuarioSeleccionado= coleccion.find({'_id':id_Usuario})[0]
    nombre.delete(0, END)
    nombre.insert(0,usuarioSeleccionado['Nombre'])
    apellido.delete(0, END)
    apellido.insert(0,usuarioSeleccionado['Apellido'])
    edad.delete(0, END)
    edad.insert(0,usuarioSeleccionado['Edad'])
    crear['state']='disabled'
    editar['state']='normal'
    eliminar['state']='normal'


def editarUsuario():#Edita la info de los registros
    global id_Usuario
    coleccion.update_one({'_id':id_Usuario}, {'$set':{'Nombre':nombre.get(), 'Apellido':apellido.get(), 'Edad':edad.get()}})
    crear['state']='normal'
    editar['state']='disabled'
    eliminar['state']='disabled'


def buscarUsuario(nombre="", apellido=""): #Busca un registro y muestra los registros que coincidan
    try:
        datosBuscar={}
        if len(nombre)!=0 or len(apellido)!=0:
            if len(nombre)!=0:
                datosBuscar['Nombre']=nombre
            if len(apellido)!=0:
                datosBuscar['Apellido']=apellido
            resultado=coleccion.find(datosBuscar)
            datosAntiguos=tabla.get_children()
            for datoA in datosAntiguos:
                tabla.delete(datoA)
            for r in resultado:
                tabla.insert('',0,text=r['_id'], values=r['Nombre'])
        else:
            datosTabla()
    except:
        print('No se encontraron coincidencias')


#Interfaz grafica
ventana = Tk()
#Tabla
tabla=ttk.Treeview(ventana, columns=2)
tabla.grid(row=1, column=0, columnspan=5, sticky=W+E)
tabla.heading('#0', text='ID')
tabla.heading('#1', text='Nombre')
tabla.bind("<Double-Button-1>", dobleClickTabla)
#Nombre
Label(ventana, text='Nombre').grid(row=2,column=1)
nombre=Entry(ventana)
nombre.grid(row=2, column=2, columnspan=2, sticky=W+E, padx=5, pady=5)
nombre.focus()
#Apellido
Label(ventana, text='Apellido').grid(row=3,column=1)
apellido=Entry(ventana)
apellido.grid(row=3, column=2, columnspan=2, sticky=W+E, padx=5, pady=5)
#Edad
Label(ventana, text='Edad').grid(row=4,column=1)
edad=Entry(ventana)
edad.grid(row=4, column=2, columnspan=2, sticky=W+E, padx=5, pady=5)
#BusquedaNombre
Label(ventana, text='Nombre a Buscar').grid(row=8, column=0)
nombreBuscar=Entry(ventana)
nombreBuscar.grid(row=8, column=1, sticky=W+E, padx=5, pady=5)
#BusquedaApellido
Label(ventana, text='Apellido a Buscar').grid(row=8, column=2)
apellidoBuscar=Entry(ventana)
apellidoBuscar.grid(row=8, column=3, sticky=W+E, padx=5, pady=5)

#Botones
#Boton crear
crear=Button(ventana, text='Crear usuario', command=crearUsuario, bg='green', fg='white', justify='center')
crear.grid(row=5, columnspan=5, sticky=W+E, padx=5, pady=5)
#Boton editar
editar=Button(ventana, text='Editar usuario', command=editarUsuario, bg='yellow', fg='white')
editar.grid(row=6, columnspan=5, sticky=W+E, padx=5, pady=5)
editar['state']='disabled'
#Boton eliminar
eliminar=Button(ventana, text='Eliminar usuario', command=eliminarUsuarios, bg='red', fg='white')
eliminar.grid(row=7, columnspan=5, sticky=W+E, padx=5, pady=5)
eliminar['state']='disabled'
#Boton buscar
buscar=Button(ventana, text='Buscar usuario', command= lambda: buscarUsuario(nombreBuscar.get(), apellidoBuscar.get()), bg='blue', fg='white')
buscar.grid(row=8, column=4, sticky=W+E, padx=5, pady=5)

#Codigo principal
datosTabla()

ventana.mainloop()
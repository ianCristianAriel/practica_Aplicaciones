#---------------Importacion de librerias------------------

import sqlite3
import os
import platform

#______________BBDD Indispensable_________________

""" Intenta crear la tabla de la base de datos, si esta inexistente """
try:
    miConexion=sqlite3.connect('biblioteca.db')
    miCursor=miConexion.cursor()
    miCursor.execute('create table catalogo (estante integer primary key, NOMBRE VARCHAR (50), SECTOR VARCHAR(50),DESCRIPCION VARCHAR(500), Editorial varchar(50))')
    miConexion.commit()
except:
    pass

#------------------------------------------------------------funciones-----------------------------------------------------------------------------

def limpiaPantalla():
    os.system('cls')


""" Busca el registro que se encuntre vacio por haber sido eliminado """
def comprubaEstanteVacio():
    estanteVacio=0
    miConexion=sqlite3.connect('biblioteca.db')
    miCursor=miConexion.cursor()
    miCursor.execute('select estante, nombre, sector, descripcion, Editorial from catalogo')
    catalogo=miCursor.fetchall()
    miConexion.commit()
    for tupla in catalogo:#Recorre el arreglo hasta que aparezca un registro vacio
	    estanteVacio+=1
	    if (tupla[0]!=estanteVacio):
	        break
    if (estanteVacio!=0) and (tupla[0]!=estanteVacio): #Comprueva que ademas alla tuplas en el catalogo
        print('Hay lugares vacios en estante: ', str(estanteVacio))
        respuesta=input('Ingrese -y para utilizar el lugar disponible o -n para utilizar el estante que sigue en el catalogo >> ')
        limpiaPantalla()
        if (respuesta=='y'):
            insertarLibroEstanteVacio(estanteVacio)
            return True
    else:
        return False


""" Devuelve el estante del ultimo registro que se agrego """
def estanteMayor():
    miConexion=sqlite3.connect('biblioteca.db')
    miCursor=miConexion.cursor()
    miCursor.execute('select estante, nombre, sector, descripcion, Editorial from catalogo')
    catalogo=miCursor.fetchall()
    miConexion.commit()
    try:
        return (catalogo[-1][0])+1 #Devuelve el valor numerico del estante mayor + uno (lugar a ocupar por el proximo estante mayor)
    except:
        return 1


""" Inserta la Libros en el registro que se encuentra vacio sin ser el ultimo agregado"""
def insertarLibroEstanteVacio(estanteVacio):
    nombre=input('Nombre: ')
    sector=input('Sector: ') 
    descripcion=input('Descripcion: ') 
    Editorial=input('Editorial: ')
    miConexion=sqlite3.connect('biblioteca.db')
    miCursor=miConexion.cursor()
    miCursor.execute('insert into catalogo values (?,?,?,?,?)',(str(estanteVacio),nombre,sector,descripcion,Editorial))
    miConexion.commit()


""" Inserta registro al final de la tabla """
def insertarLibrosestanteMayorSiguiente(estanteMayor):
    nombre=input('Nombre: ')
    sector=input('Sector: ') 
    descripcion=input('Descripcion: ') 
    Editorial=input('Editorial: ')
    miConexion=sqlite3.connect('biblioteca.db')
    miCursor=miConexion.cursor()
    miCursor.execute('insert into catalogo VALUES(?,?,?,?,?)', (estanteMayor, nombre, sector, descripcion, Editorial))
    miConexion.commit()
    limpiaPantalla()


""" Muestra el catalogo de los libros registradas """
def mostrarCatalogoLibros():
    estante=''
    contadorTuplas=0
    miConexion=sqlite3.connect('biblioteca.db')
    miCursor=miConexion.cursor()
    miCursor.execute('select estante, nombre from catalogo')
    catalogo=miCursor.fetchall()
    miConexion.commit()
    for tupla in catalogo:
        print(tupla[0],' '+tupla[1])
        contadorTuplas+=1
    if (contadorTuplas!=0):
        while (estante!='m'):
            estante=input('Ingresa un estante para ver informacion del libro o -m para volver al menu principal >> ')
            if (estante!='m') and (int(estante) in range(100)): #Se comprueba que el estante para la seleccion de Libros no sea la m, y que sea un numero entero entre 1 y 100
                informacionLibros(int(estante))
                limpiaPantalla()
                return True #Devuelve True si hay Libross para mostrar
    else:
        return False #Devuelve False si no hay Libross para mostrar


""" Muestra la informacion de la Libros que se seleccione """
def informacionLibros(estante):
    respuesta=''
    while (respuesta!='b') and (respuesta!='m'):
        miConexion=sqlite3.connect('biblioteca.db')
        miCursor=miConexion.cursor()
        miCursor.execute('select estante, nombre, sector, descripcion, Editorial from catalogo')
        catalogo=miCursor.fetchall()
        for tupla in catalogo: #Arecorre las tuplas del catalogo perteneciente a un registro de la bbdd
            if (tupla[0]==estante):#Comprueba que el estante recivido por parametro corresponda con el de la tupla
                #Se imprime la informacion del libro que corresponde al valor del estante recivido
                    print ('Nombre: '+tupla[1])
                    print ('Sector: '+tupla[2])
                    print ('Descripcion: '+tupla[3])
                    print ('Editorial: '+tupla[4])

        respuesta=input('Ingresa -e para editar, -d para eliminar o -b para volver al catalogo >> ')
        limpiaPantalla()
        if (respuesta=='d'):
            eliminaLibros(estante) #LLama a la funcion que eliminara el libro del estante que se le pasa como argumento
            while (respuesta!='0') and (respuesta!='m') and (respuesta!='b'):
                respuesta=input('Ingresa -b para volver al catalogo o -m para volver al menu principal >> ')
                limpiaPantalla()
        elif (respuesta=='e'):
            respuesta=input('Ingrese -n para modificar nombre, -s para modificar sector, -d para modificar descripcion, -i para modificar Editoriales, -b para volver al catalogo de libros >> ')
            limpiaPantalla()
            if (respuesta=='n'):
                nombre=input('Nombre: ')
                miCursor.execute('update catalogo set nombre=? where estante=?',(nombre, estante)) #Actualiza el nombre de la Libros con el estante recivido en el parametro
                miConexion.commit()
                limpiaPantalla()
                print('Nombre actualizado con exito')
            elif (respuesta=='s'):
                sector=input('Sector: ')
                miCursor.execute('update catalogo set sector=? where estante=?',(sector, estante))#actualiza el sector de la Libros con el estante recivido en el parametro
                miConexion.commit()
                limpiaPantalla()
                print('Sector actualizado con exito')
            elif (respuesta=='d'):
                descripcion=input('Descripcion: ')
                miCursor.execute('update catalogo set descripcion=? where estante=?',(descripcion, estante)) #actualiza la descrpcion de la Libros con el estante recivido en el parametro
                miConexion.commit()
                limpiaPantalla()
                print('Descripcion actualizada con exito')
            elif (respuesta=='i'):
                Editorial=input('Editorial: ')
                miCursor.execute('update catalogo set Editorial=? where estante=?',(Editorial, estante))#Actualiza la Editorial de la Libros con el estante recivestanteo en el parametro
                miConexion.commit()
                limpiaPantalla()
                print('Editorial actualizada con exito')
    if (respuesta=='b'):
        mostrarCatalogoLibros()


""" Elimina la Libros que se seleccione para eliminar """
def eliminaLibros(estante): #Resive el estante de la Libros que se quiere eliminar
    estanteVacio=0
    miConexion=sqlite3.connect('biblioteca.db')
    miCursor=miConexion.cursor()
    miCursor.execute('select estante=? from catalogo', str(estante))
    catalogo=miCursor.fetchall()
    for tupla in catalogo:
        if (tupla[0]==0):
            miConexion.commit()
            print('Es un estante vacio')
            break
        else:
            miCursor.execute('delete from catalogo where estante=?', str(estante))
            miConexion.commit()
            print('Eliminacion realizada con exito')
            break

#----------------------------Codigo global-------------------------------------------------------------------------------------------------

print('Ejersicio Libros')

respuesta=''
while (respuesta!='0'): #Comprueba que no se eligio salir
    if (respuesta=='1'):#Comprueba que se eligio mostrar catalogo de Libros
        if not mostrarCatalogoLibros(): #Intenta mostrar el catalogo de Libros
            print('No hay Libros registradas')#Si la funcion anterior devuelve False

    elif (respuesta=='2'):
        if not comprubaEstanteVacio():#Comprueva si hay estante vacios
            insertarLibrosestanteMayorSiguiente(estanteMayor())#Si no hay estante vacio se llama a la funcion que agrega un registro al final de la tabla
    
    respuesta=input("Selecciona una opción: \n1- Mostrar catalogo de Libros \n2- Agregar Libros\n0- Salir\n>> ") #Opciones del menu principal
    limpiaPantalla()

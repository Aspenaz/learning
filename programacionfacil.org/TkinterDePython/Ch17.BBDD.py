# localhost/phpmyadmin
# 127.0.0.1
from tkinter import *
import mariadb
import sys

root = Tk()
root.title('Conexión a BBDD')
root.geometry('400x350')

try:
    conexion = mariadb.connect(
        user='root',
        password='',
        host='127.0.0.1',
        port=3306,
        database='prueba'
        )
    
    Label(root, text='Conexión correcta a \'' + conexion.database + '\'').pack()   
    
except mariadb.Error as error:
    print(f'\nError al conectarse a la base de datos: {error}\n')
    # Label(root, text='\nError al conectarse a la base de datos: {error}\n').pack()   
    sys.exit(1)


mainloop()

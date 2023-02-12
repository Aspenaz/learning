from tkinter import * 

import mariadb 
import sys

root = Tk()
root.title('Ventana de registros')
# root.geometry('200x250')


#  INTERFAZ LÓGICA

# Conexión con la base de datos
try:
      conexion = mariadb.connect(
            user='root',
            password='',
            host='127.0.0.1',
            port=3306,
            database='prueba'
      )
      # Obtiene el cursor
      cursor = conexion.cursor()
      
except mariadb.Error as error:
      print(f'Error al conectar con la base de datos: {error}')
      sys.exit(1)


# Funciones
def registro_cliente():
      nombre = e_nombre.get()
      apellidos = e_apellidos.get()
      telefono = e_telefono.get()
      direccion = e_direccion.get()
      
      try:
            cursor.execute('INSERT INTO clientes                       \
                           nombre, apellidos, telefono, direccion      \
                           VALUES (?, ?, ?, ?)',                        
                           (nombre, apellidos, telefono, direccion) )
            conexion.commit()
            
      except mariadb.Error as error_registro:
            print(f'Error en el registro: {error_registro} ')


# INTERFAZ GRÁFICA

Label(root,
      text='Nuevo Cliente',
      font='calibri 18',
      fg='spring green'
      ).grid(row=0, columnspan=2, padx=60, pady=10)


Label(root,
      text='Nombre'
      ).grid(row=1, column=0, pady=10)

e_nombre = Entry(root)
e_nombre.grid(row=1, column=1, pady=10)

Label(root,
      text='Apellidos'
      ).grid(row=2, column=0, pady=10)

e_apellidos = Entry(root)
e_apellidos.grid(row=2, column=1, pady=10)


Label(root,
      text='Teléfono'
      ).grid(row=3, column=0, pady=10)

e_telefono = Entry(root)
e_telefono.grid(row=3, column=1, pady=10)


Label(root,
      text='Dirección'
      ).grid(row=4, column=0, pady=10)

e_direccion = Entry(root)
e_direccion.grid(row=4, column=1, pady=10)


boton = Button(root, text='Register', width=20, command=registro_cliente).grid(row=5, columnspan=2, pady=10)


mainloop()
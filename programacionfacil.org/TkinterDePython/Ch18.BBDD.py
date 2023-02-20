from tkinter import * 

import mariadb 

# Ventana principal 
root = Tk()
root.title('Ventana principal')
root.geometry('300x150')
root.resizable(0, 0)


# Conexión a BBDD
try: 
    conexion = mariadb.connect(
        user='root',
        password='',
        host='127.0.0.1',
        port=3306,
        database='prueba'
    )    
    cursor = conexion.cursor()
    
except mariadb.Error as error:
    print('Error al conectar con la base de datos: {error}')
    # sys.exit(1)




def crea_tabla():
    try:
        cursor.execute('CREATE TABLE clientes (id INT NOT NULL AUTO_INCREMENT,' 
                       'nombre VARCHAR (128) NOT NULL,'
                       'apellidos VARCHAR (128) NOT NULL,'
                       'telefono VARCHAR (24) NOT NULL,' 
                       'direccion VARCHAR (256),' 
                       'PRIMARY KEY (id) ); ')
        conexion.commit()
        
    except mariadb.Error as error_tabla:
        print(f'Error al crear la tabla: {error_tabla}')

    
    

# Interfaz gráfica
boton = Button(root, text='Crear tabla', command=crea_tabla, width=20)
boton.place(x=25, y=10)


mainloop() 



# Formularios con el widget Entry() y contraseñas protegidas

from tkinter import * 

root = Tk()

def click_boton():
    Label(root,
          text='¡No vuelvas a presionarlo!'
          ).grid(row=0,
                 column=2)
          
    Label(root,
          text='¡No vuelvas a presionarlo!'
          ).grid(row=0,
                 column=0)
          
boton1 = Button(root,
                text='No presiones este botón',
                bg='grey',
                padx=100,
                pady=25,
                command=click_boton
                ).grid(row=0,
                       column=1)
                
root.mainloop()


#===========================================================================


# Cómo crear una entrada de datos.

from tkinter import * 

root = Tk()

entrada = Entry(root)
entrada.grid(row=0, column=0)

def click_boton():
    # texto = Label(root, text='¡Enviado correctamente!').grid(row=0, column=0)
    texto = Label(root, 
                  text=f'Se almacenó \'{entrada.get()}\' correctamente'
                  ).grid(row=2, column=0)
    
boton1 = Button(root,
                text='Enviar',
                bg='green',
                padx=50,
                pady=10,
                command=click_boton
                ).grid(row=1, column=0)

root.mainloop()



#===========================================================================



from tkinter import * 

root = Tk()

entrada = Entry(root, width=25, show='*')
entrada.insert(0, 'Escriba aquí...')
entrada.grid(row=0, column=0)

def click_boton():
    taxto = Label(root,
                  text=f'Se almacenó \'{entrada.get()}\' correctamente'
                  ).grid(row=2, column=0)
    
boton1 = Button(root,
                text='Enviar',
                bg='brown',
                padx=75,
                pady=10,
                command=click_boton
                ).grid(row=1, column=0)

root.mainloop()



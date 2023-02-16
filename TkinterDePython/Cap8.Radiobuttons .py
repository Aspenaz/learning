# Bucle autogenerador de radiobuttons y botón de envío.

from tkinter import *

root = Tk()

x = IntVar()
x.set(value=1)

def actualiza_radio(value):
    Label(root, text=value).grid(row=3)
    
titulo = Label(root, text='Seleccione una opción').grid(row=0)

Radiobutton(root,
            text='Esta es la primera opción.',
            value=1,
            variable=x).grid(row=1)

Radiobutton(root,
            text='Esta es la segunda opción.',
            value=2,
            variable=x).grid(row=2)

boton_envia = Button(root,
                     text='Enviar',
                     command=lambda: actualiza_radio(x.get())).grid(row=4)
    
root.mainloop()
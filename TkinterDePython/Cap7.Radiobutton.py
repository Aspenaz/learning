# Formularios con el widget Radiobutton() y variables de control 

from tkinter import *
# # # 
root = Tk()

x = IntVar()
x.set(value=1)

Label(root, text='Seleccione una opción').grid(row=0)

Radiobutton(root, 
            text='Esta es la primera opción.',
            value=1,
            variable=x,
            command=lambda: actualiza(x.get())).grid(row=1)

Radiobutton(root,
            text='Esta es la segunda opción.',
            value=2,
            variable=x,
            command=lambda: actualiza(x.get())).grid(row=2)

# Para que se actualice la opción seleccionada en cada momento, deberás crear 
# una función que sea capaz de actualizarla. Simplemente pones el label dentro 
# de la función:
# opcion_set = Label(root, text=x.get()).grid(row=3)

def actualiza(value):
    Label(root, text=value).grid(row=3)
    

root.mainloop()
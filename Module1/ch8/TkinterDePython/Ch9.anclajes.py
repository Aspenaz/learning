# Los anclajes se utilizan para definir dónde se coloca el texto de los widgets.
# Estos anclajes utilizan el sistema de puntos cardinales.

from tkinter import * 

root = Tk()

titulo1 = Label(root, text='Noroeste').pack(anchor=NW)
titulo2 = Label(root, text='Norte').pack(anchor=N)
titulo3 = Label(root, text='Noreste').pack(anchor=NE)
titulo4 = Label(root, text='Oeste').pack(anchor=W)
titulo5 = Label(root, text='Centro').pack(anchor=CENTER)
titulo6 = Label(root, text='Este').pack(anchor=E)
titulo7 = Label(root, text='Suboeste').pack(anchor=SW)
titulo8 = Label(root, text='Sud').pack(anchor=S)
titulo9 = Label(root, text='Sudeste').pack(anchor=SE)

mainloop()




from tkinter import * 

root = Tk()

def actualiza_radio(value):
    Label(root, text=value).pack()
    
titulo = Label(root, text='Selecciona una opción:').pack()

opciones = [
    ['Color Rojo', 'rojo'],
    ['Color Azul', 'azul'],
    ['Color Verde', 'verde'],
    ['Color Amarillo', 'amarillo'],
    ['Color Naranja', 'naranja']
]

colores = StringVar()
colores.set('rojo')

for opcion, valor in opciones:
    Radiobutton(root, text=opcion, value=valor, variable=colores).pack(anchor=NW)
    
boton_envia = Button(root, 
                     text='Enviar',
                     command=lambda: actualiza_radio(colores.get())).pack()

root.mainloop()
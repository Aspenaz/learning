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
    Radiobutton(root, text=opcion, value=valor, variable=colores).pack()

boton_envia = Button(root, 
                     text='Enviar',
                     command=lambda: actualiza_radio(colores.get())).pack()

root.mainloop()
# Tkinter desde cero - Capítulo 1
# Primera ventana gráfica 

from tkinter import * 

root = Tk()

etiqueta = Label(root, text='¡Bienvenidos al curso de Tkinter!')
etiqueta.pack()

root.mainloop()
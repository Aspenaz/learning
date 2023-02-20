# Tkinter desde cero - Capítulo 2
# ¿Qué son los widgets? - El widget frame() y el método pack() 

from tkinter import * 

root = Tk()
root.geometry('300x200')

# Creación del marco
marco_principal = Frame()
# Empaquetado del marco
marco_principal.pack()
# Redimencionado del marco
marco_principal.config(width='180', height='160', bg='brown')

root.mainloop()
# Tkinter desde cero - Capítulo 2
# ¿Qué son los widgets? - El widget frame() y el método pack() 

from tkinter import * 

root = Tk()

# Creación del marco
marco_principal = Frame()
# Empaquetado del marco
marco_principal.pack()
# Redimencionado del marco
marco_principal.config(width='800', height='600', bg='red')

root.mainloop()
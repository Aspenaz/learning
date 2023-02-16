# El método grid().

"""
from tkinter import * 

root = Tk()

# Creación del marco
marco_principal = Frame()

# Etiqueta
texto = Label(root, text='Capítulo 3 del curso Tkinter.')
texto.pack()

marco_principal.config(width='800', height='600', bg='red')
marco_principal.pack()

root.mainloop()
"""




"""
from tkinter import * 

root = Tk()

# Creación del marco
marco_principal = Frame()

# Etiqueta
texto = Label(root, text='Capítulo 3 del curso Tkinter.')

marco_principal.config(width='800', height='600', bg='red')
marco_principal.pack()

texto.pack()

root.mainloop()
"""






from tkinter import * 

root = Tk()

# Creación del marco
marco_principal = Frame()

# Etiqueta
texto = Label(root, text='Capítulo 3 del curso Tkinter.')
texto.grid(row=0, column=1)
# texto.grid(row=0, column=0)
# texto.pack()

marco_principal.config(width='800', height='600', bg='orange')
marco_principal.grid(row=0, column=0)
# marco_principal.grid(row=1, column=0)
# marco_principal.pack()

root.mainloop()


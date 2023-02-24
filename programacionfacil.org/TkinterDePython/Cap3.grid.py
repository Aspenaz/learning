# El método grid().


from tkinter import * 

root = Tk()

# Creación del marco
marco_principal = Frame()
marco_principal.config(width='800', height='600', bg='brown')
marco_principal.pack()

# Etiqueta
texto = Label(root, text='Capítulo 3 del curso Tkinter.')
texto.pack()

root.mainloop()




from tkinter import * 

root = Tk()

# Creación del marco
marco_principal = Frame()
marco_principal.config(width='800', height='600', bg='red')
marco_principal.pack()

# Etiqueta
texto = Label(root, text='Capítulo 3 del curso Tkinter.')
texto.pack()

root.mainloop()





from tkinter import * 

root = Tk()

# Creación del marco
marco_principal = Frame()
marco_principal.config(width='800', height='600', bg='orange')
marco_principal.grid(row=0, column=0)

# Etiqueta
texto = Label(root, text='Capítulo 3 del curso Tkinter.')
texto.grid(row=0, column=1)
# texto.grid(row=0, column=0)
# texto.pack()


# marco_principal.grid(row=1, column=0)
# marco_principal.pack()

root.mainloop()


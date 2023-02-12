# Posiciones relativas y el widget Button().

from tkinter import *

root = Tk()

# Marco 1
marco_principal1 = Frame()
marco_principal1.grid(row=0, column=0)
marco_principal1.config(width='100', height='100')
marco_principal1.config(bg='orange')

# marco 2 
marco_principal2 = Frame()
marco_principal2.grid(row=1, column=0)
marco_principal2.config(width='100', height='100')
marco_principal2.config(bg='blue')

# marco 3 
marco_principal3 = Frame()
marco_principal3.grid(row=2, column=0)
marco_principal3.config(width='100', height='100')
marco_principal3.config(bg='yellow')

# marco 4
marco_principal4 = Frame()
marco_principal4.grid(row=0, column=1)
marco_principal4.config(width='100', height='100')
marco_principal4.config(bg='green')

# marco 5
marco_principal5 = Frame()
marco_principal5.grid(row=1, column=1)
marco_principal5.config(width='100', height='100')
marco_principal5.config(bg='grey')

# marco 6
marco_principal6 = Frame()
marco_principal6.grid(row=2, column=1)
marco_principal6.config(width='100', height='100')
marco_principal6.config(bg='brown')

botton1 = Button(root, 
                 text='No presione este botón', 
                 bg='orange',
                 padx=100,
                 pady=25,
                # state=DISABLED
                 ).grid(row=1, column=2)

root.mainloop()
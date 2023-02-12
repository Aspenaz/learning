from tkinter import * 

root = Tk()
root.title('Frames')
root.iconbitmap('Z:/Compartido/Python.Journey/learning/Module1/ch8/TkinterDePython/img/Bonjour.ico')


buscador = LabelFrame(root, text='Buscador', padx=30, pady=30) # los márgenes los crea en el inteerior. Relativos a los widgets dentro de los marcos
buscador.grid(row=0, column=0, padx=100, pady=100)  # grid general de la ventana principal root

barra = Entry(buscador, text='¿Buscas algo?').pack()
boton = Button(buscador, text='Buscar').pack()


buscador2 = LabelFrame(root, text='Buscador 2', padx=150, pady=100)
buscador2.grid(row=1, column=0, padx=5, pady=5)

barra2 = Entry(buscador2, text="¿Buscas algo?").grid(row=0, column=0)
boton2 = Button(buscador2, text="Buscar").grid(row=0, column=1)


mainloop()

# Llamar a funciones desde un botón

from tkinter import * 

root = Tk()

def click_boton():
    Label(root, text='¡No vuelvas a presionarlo!').grid(row=2, column=2)
    
boton1 = Button(root,
                text='No presiones este botón',
                bg='green',
                padx=100,
                pady=25,
                command=click_boton              # Aquí sí se ejecuta
                ).grid(row=1, 
                       column=2, 
                    #    command=click_boton     # Aquí en grid no se ejecuta
                    #    command=click_boton()   # Si se añaden los paréntesis se ejecuta la función directamente.                     
                       )

root.mainloop()

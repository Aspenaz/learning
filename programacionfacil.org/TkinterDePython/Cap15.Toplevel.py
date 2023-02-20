from tkinter import * 

root = Tk()
root.title('Ventana Principal')
root.geometry('300x100')

entrada = Entry(root, width=35)
entrada.grid(row=0)


def envia_boton():
    ventana_nueva_1 = Toplevel()
    ventana_nueva_1.geometry('300x200')
    ventana_nueva_1.title('Ventana Secundaria')
    
    Label(ventana_nueva_1, text='El valor de Entry es: ' + entrada.get()).grid(row=0)
    
    Button(ventana_nueva_1, text='Cerrar ventana', command=ventana_nueva_1.destroy).grid(row=1)


Button(root, text='Enviar', command=envia_boton).grid(row=1)
Button(root, text='Cerrar ventana', command=root.destroy).grid(row=2)



mainloop()
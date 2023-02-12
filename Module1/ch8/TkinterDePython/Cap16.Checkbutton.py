from tkinter import * 

root = Tk()
root.title('Ventana Principal')
root.geometry('300x300')

def seleccion():
    # etiqueta = Label(root, text=controlInt.get()).pack()
    Label(root, text=controlInt.get()).pack()
    Label(root, text=controlString.get()).pack()

controlInt = IntVar()
controlString = StringVar()

opcion_1 = Checkbutton(root, text='Opción 1', variable=controlInt)
opcion_2 = Checkbutton(root, text='Opción 2', variable=controlString)   # la opción marcada por defecto si utilizamos StringVar.

opcion_1.pack()
opcion_2.pack()

opcion_2.deselect()

Button(root, text='Mostrar seleción', command=seleccion).pack()

mainloop()


#============================================================================


from tkinter import *

root = Tk()
root.title('Segunda ventana')
root.geometry('350x400')

def seleccion():
    Label(root, text=control_1.get()).pack()
    Label(root, text=control_2.get()).pack()
    
control_1 = StringVar()
control_2 = StringVar()

opcion_1 = Checkbutton(root,
                       text='Opción 1',
                       variable=control_1,
                       onvalue='1 Seleccionado',
                       offvalue='1 No Seleccionado')

opcion_2 = Checkbutton(root,
                       text='Opción 2',
                       variable=control_2,
                       onvalue='2 Seleccionado',
                       offvalue='2 No Seleccionado')

opcion_1.pack()
opcion_2.pack()

opcion_1.deselect()
opcion_2.deselect()

Button(root, text='Presentar selección', command=seleccion).pack()


mainloop()
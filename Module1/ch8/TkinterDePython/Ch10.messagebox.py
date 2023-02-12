from tkinter import *
from tkinter.messagebox import * 

root = Tk()
root.title('Este es el título de la ventana principal')
root.iconbitmap('Z:/Compartido/Python.Journey/learning/Module1/ch8/TkinterDePython/img/favicon.ico')

def ventana_showinfo():
    showinfo('Aquí se escribe el título de la ventana', 'Este es el mensaje que se muestra en la ventana.')

def ventana_showwarning():
    showwarning('aquí se muestra el título de la ventana', 'Este es el mensaje que se muestra en la ventana.')

def ventana_showerror():
    showerror('Auí se escribe el título de la ventana', 'Este es el mensaje que se muestra en la ventana.')

def ventana_askquestion():
    askquestion('Aquí se escribe el título de la ventana', '¿Debería olvidar la programación?')    
    
def ventana_askyesno():
    askyesno('Aquí se escribe el título de la ventana', '¿Debería dejar de intentar programar?')
    
   
boton1 = Button(root, text='Showinfo', command=ventana_showinfo, width=75).pack()
boton2 = Button(root, text='Sowwarning', command=ventana_showwarning, width=75).pack()
boton3 = Button(root, text='Showerror', command=ventana_showerror, width=75).pack()
boton4 = Button(root, text='Askquestion', command=ventana_askquestion, width=75).pack()
boton5 = Button(root, text='Askyesno', command=ventana_askyesno, width=75).pack()

mainloop()

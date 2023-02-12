from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('Este es el título de la ventana principal')
root.iconbitmap('Z:/Compartido/Python.Journey/learning/Module1/ch8/TkinterDePython/img/favicon1.ico')

def ventana_askquestion():
    
    respuesta = askquestion(title='Pregunta seria', message='¿Debería dejar de intentar programar?')
   
    if respuesta == 'no':
        showinfo(title='¡A seguir programando!', message='Muy bien, eligió la respuesta correcta.')
    
    if respuesta == 'yes':  # else:
        respuesta_retry = askretrycancel(title='Botón equivocado', message='Haga click en \'Reintentar\' para seguir programando.')
        if respuesta_retry:
            showinfo(title='¡A seguir programando!', message='Respuesta correcta.')
        else:
            showinfo(title='Adiós', message='¡Esperamos que vuelvas pronto!')

boton1 = Button(root, text='Askquestion', command=ventana_askquestion, width=75).pack()    

mainloop()
from tkinter import * 

root = Tk()
root.title('Calculadora básica')
root.iconbitmap('Z:/Compartido/Python.Journey/learning/Module1/ch8/TkinterDePython/img/GRAPH.ico')
root.resizable(0, 0)     # evita que el usuario pueda redimensionar el tamaño de la ventana. 0 = false, 1 = true
root.geometry('296x306') # permite darle tamaño a la ventana.


pantalla = Entry(root, 
                 width=22,
                 bg='grey',
                 fg='white',
                 borderwidth=0,
                 font=('arial', 18, 'bold'))

pantalla.grid(row=0, padx=2, pady=2, columnspan=4)



def envia_boton(valor):
    anterior = pantalla.get()
    pantalla.delete(0, END) 
    pantalla.insert(0, str(anterior) + str(valor))  # tiene que ser string por el tipo de formulario Entry.
    
def suma():
    global num1 
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END) 
    operacion = '+'

def resta():
    global num1 
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END) 
    operacion = '-'
    
def multiplicacion():
    global num1 
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END) 
    operacion = '*'
    
def division():
    global num1 
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END) 
    operacion = '/'
    
def igual():
    try: 
        global num2 
        num2 = pantalla.get()
        pantalla.delete(0, END) 
        
        if operacion == '+':
            pantalla.insert(0, num1 + float(num2))
            
        if operacion == '-':
            pantalla.insert(0, num1 - float(num2))
            
        if operacion == '*':
            pantalla.insert(0, num1 * float(num2))
            
        if operacion == '/':
            pantalla.insert(0, num1 / float(num2))
            
    except NameError:
        pantalla.insert(0, 'Error')
        

def clear():
    pantalla.delete(0, END)
    

# lambda es para que no envíe el valor directamente sin pulsar los botones.

boton_1 = Button(root, 
                 text=1,
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(1)).grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root, 
                 text='2',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(2)).grid(row=1, column=1, padx=1, pady=1)

boton_3 = Button(root,
                 text='3',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(3)).grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root,
                 text='4',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(4)).grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root,
                 text='5',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(5)).grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root,
                 text='6',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(6)).grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root,
                 text='7',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(7)).grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root,
                 text='8',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(8)).grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root,
                 text='9',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(9)).grid(row=3, column=2, padx=1, pady=1)

boton_0 = Button(root,
                 text='0',
                 width=9,
                 height=3,
                 bg='white',
                 fg='orange',
                 borderwidth=0,
                 cursor='hand2',
                 command=lambda: envia_boton(0)).grid(row=4, column=1, padx=1, pady=1)


boton_igual = Button(root,
                     text='=',
                     width=9,
                     height=3,
                     bg='orange',
                     fg='white',
                     borderwidth=0,
                     cursor='hand2',
                     command=igual
                     ).grid(row=4, column=0, padx=1, pady=1)

boton_punto = Button(root,
                     text='.',
                     width=9,
                     height=3,
                     bg='spring green',
                     fg='black',
                     cursor='hand2',
                     borderwidth=0,
                     command=lambda: envia_boton('.')
                     ).grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root,
                   text='+',
                   width=9,
                   height=3,
                   bg='deep sky blue',
                   fg='black',
                   borderwidth=0,
                   cursor='hand2',
                   command=suma
                   ).grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root,
                     text='-',
                     width=9,
                     height=3,
                     bg='deep sky blue',
                     fg='black',
                     borderwidth=0,
                     cursor='hand2',
                     command=resta
                     ).grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root,
                              text='*',
                              width=9,
                              height=3,
                              bg='deep sky blue',
                              fg='black',
                              borderwidth=0,
                              cursor='hand2',
                              command=multiplicacion
                              ).grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root,
                        text='/',
                        width=9,
                        height=3,
                        bg='deep sky blue',
                        fg='black',
                        borderwidth=0,
                        cursor='hand2',
                        command=division
                        ).grid(row=4, column=3, padx=1, pady=1)

boton_clear = Button(root,
                     text='Clear',
                     width=40,
                     height=3,
                     bg='deep sky blue',
                     fg='black',
                     borderwidth=0,
                     cursor='hand2',
                     command=clear
                     ).grid(row=5, column=0, columnspan=4, padx=1, pady=1)

mainloop()

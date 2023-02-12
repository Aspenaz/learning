# import tkinter
from tkinter import *
from tkinter import messagebox


top = Tk()

def helloCallBack():
    messagebox.showinfo('Hello Python top', 'Hello World top')
    
B = Button(top, text='Hello top', command=helloCallBack)
B.pack()
top.mainloop()
    


# topMsgBox = Tk()
# topMsgBox.geometry('150x100')
# def hello():
#     messagebox.showinfo('Say Hello', 'Hello World')
# B1 = Button(topMsgBox, text='Say Hello button', command=hello)
# B1.place(x=35, y=50)
# topMsgBox.mainloop()
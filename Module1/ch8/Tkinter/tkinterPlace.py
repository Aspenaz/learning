from tkinter import * 
from tkinter import messagebox

top = Tk()

def helloCallBack():
    messagebox.showinfo('Hello Python', 'Hello Sun')
    
B = Button(top, text='Sun', command=helloCallBack)
B.pack()
B.place(bordermode=OUTSIDE, height=150, width=150)

mainloop()
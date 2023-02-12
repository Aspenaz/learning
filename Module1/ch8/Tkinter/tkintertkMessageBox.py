from tkinter import * 
from tkinter import messagebox 

top = Tk()

def hello():
    messagebox.showinfo('Say hello', 'Hello Sun')
    messagebox.askokcancel('Ok', 'Cancel')
    
B1 = Button(top, text='Say hello sun', command=hello)
B1.pack()
    
top.mainloop()
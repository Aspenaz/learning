# from tkinter import * 

# import tkinter

# root = Tk()

# for r in range(3):
#     for c in range(4):
#         Label(root, text='R%s/C%s'%(r,c), borderwidth=1).grid(row=r, column=c)
        
# root.mainloop()




from tkinter import * 
# from tkinter.ttk import *

master = Tk()

l1 = Label(master, text='Height:')
l2 = Label(master, text='Width:')
l1.grid(row=0, column=0, sticky=W, padx=2, pady=2)
l2.grid(row=1, column=0, sticky=W, padx=2, pady=2)

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, column=1, pady=2)

c1 = Checkbutton(master, text='Preserve')
c1.grid(row=2, column=0, sticky=W, columnspan=2)

img = PhotoImage(file=r'Z:\Compartido\Python.Journey\learning\Module1\ch8\owl-alcohol.png')
img = img.subsample(2, 2)

Label(master, image=img).grid(row=0, column=2, columnspan=2, rowspan=2, padx=2, pady=5)

b1 = Button(master, text='Zoom in')
b2 = Button(master, text='Zoom out')
b1.grid(row=2, column=2, sticky=E)
b2.grid(row=2, column=3, sticky=E)

# master.mainloop()
mainloop()

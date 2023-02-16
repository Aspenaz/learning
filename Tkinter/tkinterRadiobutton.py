from tkinter import *

def sel():
    selection = 'You selected the option: ' + str(var.get()) # var.get() optain value=[] in R[n] = Radiobutton(root, text='Option []', variable=var, value=[], command=sel) 
    label.config(text = selection)
    

root = Tk()

var = IntVar() # StringVar()

R1 = Radiobutton(root, text='Option 1', variable=var, value=1, command=sel, fg='green')
R1.pack(anchor=W)

R2 = Radiobutton(root, text='Option 2', variable=var, value=2, command=sel, bg='yellow')
R2.pack(anchor=W)

R3 = Radiobutton(root, text='Option 3', variable=var, value=3, command=sel, activebackground='Blue')
R3.pack(anchor=W)

R4 = Radiobutton(root, text='Option 4', variable=var, value=4, command=sel, activeforeground='grey')
R4.pack(anchor=W)

R5 = Radiobutton(root, text='Option 5', variable=var, value=5, command=sel, highlightbackground='red')
R5.pack(anchor=W)

R6 = Radiobutton(root, text='Option 6', variable=var, value=6, command=sel, highlightcolor='brown')
R6.pack(anchor=W)



label = Label(root)
label.pack()

mainloop()
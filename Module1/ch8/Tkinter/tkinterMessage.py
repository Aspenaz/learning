from tkinter import * 

root = Tk()

var = StringVar()
var.set('Hey! How are you doing?')
label = Message(root, textvariable=var, relief=RAISED)
label.pack()

var = StringVar()
var.set('What are you doing?')
label = Message(root, textvariable=var, relief=RAISED)
label.pack()

# root.mainloop()
mainloop()
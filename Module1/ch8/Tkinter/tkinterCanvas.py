# import tkinter
from tkinter import *

# top = tkinter.Tk()
top = Tk()

# C = tkinter.Canvas(top, bg='blue', height=200, width=300)
C = Canvas(top, bg='blue', height=200, width=300, bd=5)

coord = 10, 50, 240, 210 
arc = C.create_arc(coord, start=0, extent=150, fill='red')

C.pack()
top.mainloop()

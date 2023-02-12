from tkinter import * 

root = Tk()


frame = Frame(root)
frame.pack(side=BOTTOM)

redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=RIGHT)

greenbotton = Button(frame, text='Green', fg='green')
greenbotton.pack(side=LEFT)

bluebutton = Button(frame, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)

blackbutton = Button(frame, text='Yellow', fg='yellow')
blackbutton.pack(side=BOTTOM)



bottomframe = Frame(root)
bottomframe.pack()

blackbutton = Button(bottomframe, text='Black', fg='black')
blackbutton.pack(side=TOP)

# root.mainloop()
mainloop()
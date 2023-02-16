from tkinter import *

def onclick():
    pass

root = Tk()
text = Text(root)

text.insert(INSERT, 'Good by ... \n')
text.insert(INSERT,    'See you later!')
text.pack()

text.tag_add('here', '1.0', '1.7')
text.tag_add('start', '1.8', '1.12')

text.tag_config('here', background='blue', foreground='orange')
text.tag_config('start', background='grey', foreground='green')

root.mainloop()

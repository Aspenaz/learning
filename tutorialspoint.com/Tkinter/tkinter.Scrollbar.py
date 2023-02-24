from tkinter import * 

root = Tk()
root.geometry("200x300")

scrollbar = Scrollbar(root) # .pack(side=RIGHT, fill=Y)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)  #.pack(side=LEFT, fill=BOTH)
mylist.pack(side=LEFT, fill=BOTH, anchor=CENTER, expand=1)  # , expand=1

scrollbar.config(command=mylist.yview)

for line in range(1, 101):
    mylist.insert(END, 'This is line number ' + str(line))
    




mainloop()



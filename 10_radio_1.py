# Adding radio buttons
from tkinter import *

root = Tk()
root.title('Radio Example')
root.iconbitmap('./files/predator.ico')

# we will use this variable in radio button
r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()


myButton = Button(root, text="Click me!", command=lambda: clicked(r.get()))
myButton.pack()

root.mainloop()

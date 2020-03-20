# Positioning With Tkinter's Grid System
from tkinter import *

root = Tk()

# create a label widget
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='I am Mohammad Khan.')
# this is another way of putting the label onto the screen
myLabel3 = Label(root, text='           ').grid(row=1, column=1) 

# shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
# myLabel2.grid(row=1, column=1)
# myLabel2.grid(row=1, column=5)


root.mainloop()


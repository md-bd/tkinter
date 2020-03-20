# Creating Buttons
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='Look I clicked a Button!')
    myLabel.pack()

# myButton = Button(root, text='Click Me!')
# myButton = Button(root, text='Click Me!', state=DISABLED)
# myButton = Button(root, text='Click Me!', padx=50, pady=50)
# CAUTION: command=myClick() will not work!!!!
myButton = Button(root, text='Click Me!', command=myClick, fg="green", bg='#000000')

myButton.pack()

root.mainloop()


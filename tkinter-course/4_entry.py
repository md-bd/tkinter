# Creating Input Fields
from tkinter import *

root = Tk()

# a widget to enter values
e = Entry(root, width=50, bg='#aaaaaa', fg='#ffffff', borderwidth=10)
e.pack()

e.insert(0, 'Enter your name: ')

def myClick():
    # e.get() fetches the value from the input field of entry widget
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

# myButton = Button(root, text='Click Me!')
# myButton = Button(root, text='Click Me!', state=DISABLED)
# myButton = Button(root, text='Click Me!', padx=50, pady=50)
# CAUTION: command=myClick() will not work!!!!
myButton = Button(root, text='Click Me!', command=myClick, fg="green", bg='#000000')

myButton.pack()

root.mainloop()

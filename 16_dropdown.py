# Dropdown boxes
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Slider')
root.iconbitmap('./files/predator.ico')
root.geometry("400x400")

def show():
	myLabel = Label(root, text=clicked.get()).pack()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday",
	"Saturday"
]	

clicked = StringVar()
clicked.set(options[0])

# pay extra attention to the parameters
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()


mainloop()


# Check boxes
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Slider')
root.iconbitmap('./files/predator.ico')
root.geometry("400x400")

var = StringVar()
c =Checkbutton(root, text="SuperSize your order? Check Here!", variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()

def show():
	myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show Selection", command=show).pack()


mainloop()


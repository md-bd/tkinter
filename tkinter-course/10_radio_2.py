# Adding radio buttons
from tkinter import *

root = Tk()
root.title('Radio Example')
root.iconbitmap('./files/predator.ico')

TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()


myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()

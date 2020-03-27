# Create New Windows in tKinter
from tkinter import *
from PIL import ImageTk,Image



root = Tk()
root.title('Main Window')
root.iconbitmap('./files/predator.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('My Second Window')
	top.iconbitmap('./files/predator.ico')
	my_img = ImageTk.PhotoImage(Image.open("files/overwatch.jpg"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()



btn = Button(root, text="Open Second Windo", command=open).pack()



mainloop()


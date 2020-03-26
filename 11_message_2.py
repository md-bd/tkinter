# Message Boxes
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title('Message Box')
root.iconbitmap('./files/predator.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.askquestion("This is my Popup!", "Hello World!")
    #Label(root, text=response).pack()
	if response == "yes":
		Label(root, text="You Clicked Yes!").pack()
	else:
		Label(root, text="You Clicked No!!").pack()

Button(root, text="Popup", command=popup).pack()



mainloop()


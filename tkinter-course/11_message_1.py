# Message Boxes
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title('Message Box')
root.iconbitmap('./files/predator.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup(text):
	if text == "showinfo":
		response = messagebox.showinfo("This is my Popup!", "Hello World!")
	elif text == "showwarning":
		response = messagebox.showwarning("This is my Popup!", "Hello World!")
	elif text == "showerror":
		response = messagebox.showerror("This is my Popup!", "Hello World!")
	elif text == "askquestion":
		response = messagebox.askquestion("This is my Popup!", "Hello World!")
	elif text == "askokcancel":
		response = messagebox.askokcancel("This is my Popup!", "Hello World!")
	elif text == "askyesno":
		response = messagebox.askyesno("This is my Popup!", "Hello World!")
	Label(root, text="You Clicked " + response).pack()

Button(root, text="Popup_showinfo", command=lambda: popup("showinfo")).pack()
Button(root, text="Popup_showwarning", command=lambda: popup("showwarning")).pack()
Button(root, text="Popup_showerror", command=lambda: popup("showerror")).pack()
Button(root, text="Popup_askquestion", command=lambda: popup("askquestion")).pack()
Button(root, text="Popup_askokcancel", command=lambda: popup("askokcancel")).pack()
Button(root, text="Popup_askyesno", command=lambda: popup("askyesno")).pack()




mainloop()


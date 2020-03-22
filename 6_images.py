# Using Icons, Images, and Exit Buttons
from tkinter import *

root = Tk()
root.title("Image Displayer")
# icon addition
root.iconbitmap('./files/predator.ico')

# quit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()

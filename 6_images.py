# Using Icons, Images, and Exit Buttons
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image Displayer")
# icon addition
root.iconbitmap('./files/predator.ico')

# quit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open('./files/overwatch.jpg'))
my_label = Label(image=my_img)
my_label.pack()


root.mainloop()

# OSliders
from tkinter import *
from PIL import ImageTk,Image
# from tkinter import filedialog


root = Tk()
root.title('Slider')
root.iconbitmap('./files/predator.ico')
root.geometry("400x400")

# look out for from_ and to. its not going to work without the underscore after from
vertical = Scale(root, from_=0, to=400)
vertical.pack()


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_label = Label(root, text=str(horizontal.get())+'x'+str(vertical.get())).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

my_btn = Button(root, text="Click Me!", command=slide).pack()

mainloop()


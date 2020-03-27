# Open Files Dialog Box
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title('Image File Viewer')
root.iconbitmap('./files/predator.ico')



def open():
    global my_image
    # initialdir somehow isn't working with relative path. absolute path does work however
    root.filename = filedialog.askopenfilename(initialdir="/files/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename)) 
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()



mainloop()


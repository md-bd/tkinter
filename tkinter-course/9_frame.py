# Adding frames
from tkinter import *

root = Tk()
root.title('Frame Example')
root.iconbitmap('./files/predator.ico')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
# inside a frame we can choose whether to use grid or pack regardless of our choice of grid or pack in frame itself
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()

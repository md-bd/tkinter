# ------------------------------------------------------------------------------
# Python program to create a image crop application in Tkinter
# Written by Mohammad Khan (mohammad.buet@gmail.com)
# Version 1.0.2022.07.15
# ------------------------------------------------------------------------------

# import all components from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

# import other image processing libraries
import cv2
from PIL import Image, ImageTk
from PIL import ImageGrab

# import other useful libraries
import datetime
import os

crop_coordinates = {
    "x1": 0,
    "y1": 0,
    "x2": 0,
    "y2": 0
}

image_coordinates = {
    "image-width": 0, 
    "image-height": 0
}


crop_flag = False
image_in_display_flag = False
crop_rectangle_drawing_flag = False

canvas = None
canvas_rectangle = None

def save_as_png(canvas, _fileName):
    """
    This function is not used here. for some reason .eps file was not read properly in Image.open
    """
    # save postscipt image 
    canvas.postscript(file = _fileName + '.eps') 
    # use PIL to convert to PNG 
    _image = Image.open(_fileName + '.eps') 
    # _image.save(_fileName + '.png', 'png')
    _image.save(_fileName + ".png")

# https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image/38645917#38645917
def save_widget_as_image(widget, file_name):
    """
    Saves image of the widget.
    """
    ImageGrab.grab(bbox=(
        widget.winfo_rootx(),
        widget.winfo_rooty(),
        widget.winfo_rootx() + widget.winfo_width(),
        widget.winfo_rooty() + widget.winfo_height()
    )).save(file_name)

def save_file_haldler():
    """
    save button will call this handler and this function will call the save image function to save the image.
    """
    global canvas
    if canvas:
        _output_file_name = "crop_" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".png"
        # save_as_png(canvas, "output")
        save_widget_as_image(canvas, _output_file_name)

def browseFiles():
    """
    Load  the selected file and show in canvas.
    """
    global filename
    filename = filedialog.askopenfilename(initialdir = ".", title = "Select a File", filetypes = (("image files", "*.png*"), ("all files", "*.*")))
    
    if os.path.isfile(filename): 
        # Change label contents
        label_file_explorer.configure(text="File Opened: " + filename)
        
        # open image
        global img
        # img = PhotoImage(file=filename)
        img = Image.open(filename)
        # print(dir(img)) # img.height, img.width
        # print(img.height(), " ", img.width())
        global _img
        _img = ImageTk.PhotoImage(img)
        
        # global image_label
        # image_label = Label(window, image=img)
        # image_label.grid(row = 4)
        # # https://stackoverflow.com/questions/66299120/how-to-get-the-x-and-y-coordinates-of-a-label-in-tkinter
        # print(image_label.place_info())

        # https://www.geeksforgeeks.org/reading-images-with-python-tkinter/
        # window.geometry(str(img.width() + 100) + "x" + str(img.height() + 100))
        # show in canvas
        global canvas
        global window

        if canvas is None:
            canvas = Canvas(window, bg="yellow", height=_img.height(), width=_img.width())
        else:
            canvas.config(height=_img.height(), width=_img.width())
        
        if _img.width() > 500 and _img.height() > 500:
            window.geometry(str(_img.width() + 5) + "x" + str(_img.height() + 65))
        else:
            window.geometry("500x500")

        global canvas_image
        canvas_image = canvas.create_image(0, 0, image=_img, anchor = NW)
        canvas.grid(row = 2, columnspan = 5)
        
        global image_in_display_flag
        image_in_display_flag = True

        global image_coordinates 
        image_coordinates["image-width"] = _img.width()
        image_coordinates["image-height"] = _img.height()

def crop():
    """
    start cropping and show the cropped image
    """
    global crop_flag
    global canvas
    global filename

    if image_in_display_flag:
        
        if crop_flag:
            label_file_explorer.configure(text="Press Crop to start cropping again or press save to save image")
            # crop the image
            # https://www.tutorialspoint.com/how-do-i-update-images-on-a-tkinter-canvas
            global cropped_img
            global img
            # _img = Image.open(filename)
            # _img = Image.open("/app/xx.png")
 
 
            left = crop_coordinates["x1"]
            top = crop_coordinates["y1"]
            right = crop_coordinates["x2"]
            bottom = crop_coordinates["y2"]

            # print("DEBUG| cropping: ", left, ", ", top, ", ", right, ", ", bottom)
 
  
            img = img.crop((left, top, right, bottom))
            cropped_img = ImageTk.PhotoImage(img)

            canvas.config(width=cropped_img.width(), height=cropped_img.height())
            global canvas_image
            canvas.itemconfig(canvas_image, image=cropped_img)

            global window
            if cropped_img.width() > 500 and cropped_img.height() > 500:
                window.geometry(str(cropped_img.width() + 5) + "x" + str(cropped_img.height() + 65))
            else:
                window.geometry("500x500")
            
            global image_coordinates 
            image_coordinates["image-width"] = cropped_img.width()
            image_coordinates["image-height"] = cropped_img.height()

            crop_flag = False

            global canvas_rectangle
            crop_coordinates["x1"] = 0
            crop_coordinates["y1"] = 0
            crop_coordinates["x2"] = 0
            crop_coordinates["y2"] = 0
            
            # https://pythonprogramming.altervista.org/delete-an-object-on-the-canvas/
            canvas.delete(canvas_rectangle)
            canvas_rectangle = None
            crop_rectangle_drawing_flag = False


        else:
            label_file_explorer.configure(text="Draw the cropping rectangle area and then press crop to crop the area")
            crop_flag = True
    else:
        label_file_explorer.configure(text="First Select an image and then press crop to crop the image")

def left_click_handler(event):
    """
    this function is of no use now.
    """
    global canvas
    if crop_flag:
        # label_file_explorer.configure(text="left click pressed at " + str(canvas.canvasx(event.x)) + ", " + str(event.y))
        return

        # crop_coordinates["x1"] = event.x
        # crop_coordinates["y1"] = event.y
        
def left_click_drag_handler(event):
    """
    draw the rectangle region and keep track of its coordinates
    """
    if crop_flag:
        # label_file_explorer.configure(text="left click dragged at " + str(event.x) + ", " + str(event.y))

        global canvas
        global canvas_rectangle
        global crop_rectangle_drawing_flag

        global image_coordinates 
        
        if event.x > image_coordinates["image-width"]:
            _x2 = image_coordinates["image-width"]
        else:
            _x2 = event.x
        
        if event.y > image_coordinates["image-height"]:
            _y2 = image_coordinates["image-height"]
        else:
            _y2 = event.y
         

        if canvas_rectangle is None:
            # https://stackoverflow.com/a/57998416

            crop_coordinates["x1"] = _x2
            crop_coordinates["y1"] = _y2

            canvas_rectangle = canvas.create_rectangle(crop_coordinates["x1"], crop_coordinates["y1"], _x2, _y2, fill="")
            crop_rectangle_drawing_flag = True
        
        elif crop_rectangle_drawing_flag:
            canvas.coords(canvas_rectangle, crop_coordinates["x1"], crop_coordinates["y1"], _x2, _y2)
        
        elif not crop_rectangle_drawing_flag:
            crop_coordinates["x1"] = _x2
            crop_coordinates["y1"] = _y2

            canvas.coords(canvas_rectangle, crop_coordinates["x1"], crop_coordinates["y1"], _x2, _y2)
            crop_rectangle_drawing_flag = True

def left_click_release_handler(event):
    """
    mark the end of the rectangle
    """
    global crop_rectangle_drawing_flag
    if crop_flag:
        # label_file_explorer.configure(text="left click released at " + str(event.x) + ", " + str(event.y))
        
        # check coordinate before assigning...
        global image_coordinates 
        
        if event.x > image_coordinates["image-width"]:
            _x2 = image_coordinates["image-width"]
        else:
            _x2 = event.x
        
        if event.y > image_coordinates["image-height"]:
            _y2 = image_coordinates["image-height"]
        else:
            _y2 = event.y
        
        crop_coordinates["x2"] = _x2
        crop_coordinates["y2"] = _y2
        crop_rectangle_drawing_flag = False


# Create the root window
window = Tk()

# Set window title
window.title('Image Cropper')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
							text = "File Explorer using Tkinter",
							# width = 100, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)

button_crop = Button(window,
					text = "crop",
					command = crop)

button_save = Button(window,
					text = "Save",
					command = save_file_haldler)


# https://tkinterexamples.com/events/mouse/
window.bind("<Button-1>", left_click_handler)
window.bind("<B1-Motion>", left_click_drag_handler)
window.bind("<ButtonRelease-1>", left_click_release_handler)


# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
# label_file_explorer.grid(column = 0, row = 0)
label_file_explorer.grid(row = 1, columnspan = 4, sticky = W, pady = 2, padx = 2)

button_explore.grid(column = 0, row = 0, sticky = W, pady = 2)

button_exit.grid(column = 3, row = 0, sticky = W, pady = 2, padx = 2)

button_crop.grid(column = 1, row = 0, sticky = W, pady = 2, padx = 2)

button_save.grid(column = 2, row = 0, sticky = W, pady = 2, padx = 2)


# https://pythonguides.com/python-tkinter-image/#:~:text=Image%20in%20Python%20Tkinter%20can%20be%20displayed%20either,will%20use%20the%20create_image%20method%20from%20the%20canvas.
# filename = '/app/Screenshot from 2022-07-12 22-16-41.png'
# img = PhotoImage(file=filename)
# # global image_label
# image_label = Label(window, image=img)
# image_label.grid(row = 4)


# Let the window wait for any events
window.mainloop()

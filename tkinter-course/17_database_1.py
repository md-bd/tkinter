# Creating Database
from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('DATABASE CREATE')
root.iconbitmap('./files/predator.ico')
root.geometry("400x400")

# Create a database or connect to one
conn = sqlite3.connect('./files/address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")


# commit changes and close connection
conn.commit()
conn.close()

mainloop()


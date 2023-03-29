# Project 4: A SIMPLE desktop program where you can upload images and add a Watermark.
# I decided to use in this version Tkinter as a UI and Pillow as the Image Manipulator
# Remember Pillow supports PNG, JPEG, PPM, GIF, TIFF, and BMP

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageGrab
import os

# ----- Variables  Area ----- #


# Define Constants

DARKGREY = '#2F4F4F'
GREY = '#696969'
BACK_COLOR = '#ffffff'
L_GREY = '#EAEAEA'
MIDGREY = '#A6A6A6'
D_GREY = '#333333'
LIGHTBLUE = '#0078D7'
SKY_BLUE = '#00B7C3'
FONT_1 = ('times', 30, 'bold')
FONT_2 = ('courier', 14)
FONT_3 = ('times', 14, 'bold')

# ----- Function definition  Area ----- #


def select_files():
   """Uses Tkinter filedialog Module and PIL to load an image on the root window"""
   global img
   # open the dialog box to choose the file to be open ( any type of file)
   filetypes = [('All files', '*.*')]
   filename = fd.askopenfilename(
      title='SELECT A FILE',
      initialdir='/',
      filetypes=filetypes)
   img = Image.open(filename)

   # get the size of the image and scale it down
   iwidth = img.width
   iheight= img.height
   ypix = int(iheight*300/iwidth)
   img = img.resize((300, ypix))

   # Be able to use the label to show the photo in tkinter root window
   # img1 = ImageTk.PhotoImage(img)
   # label = Label(window, image=img1)

   # to keep a reference of the image, so it is not destroyed
   # label.image = img1
   # label.pack(side=BOTTOM, anchor=SW, pady=15, padx=10, before=leave)

   # create a new window to display the image
   # the function creates a new window using Toplevel(), which is a function in the tkinter library that creates a
   # new window. The image is displayed in the new window using a Label widget, just like in your original code.
   # Finally, the function returns the img object as before.
   image_window = Toplevel(window)
   image_window.title("Your Image")
   img1 = ImageTk.PhotoImage(img)
   label = Label(image_window, image=img1)
   label.image = img1
   label.pack()
   return img


def create_watermark():
   """Function creates a single phrase watermark"""
   # getting global variables
   global img
   global texto
   global the_image

   the_image = img
   # get image size
   img_width = the_image.width
   img_height = the_image.height

   # draw on Image
   draw = ImageDraw.Draw(the_image)

   # specify the font size
   the_text = texto.get()
   font_size = int(img_width / 8)
   font = ImageFont.truetype('Arial.ttf', font_size)

   # Image Coordinates
   x, y = int(img_width/2), int(img_height / 2)

   # add the watermark and place it at the center of the screen
   draw.text((x, y), the_text, font=font, fill='#ffff', stroke_with=5, stroke_fill='#222f', anchor='ms')

   # show new image
   the_image.show()
   return the_image

def photo_saver():
   """This function allow us to save the image to a dir of our choosing"""
   global the_image
   filetypes = [('Portable Network Graphics', '*.png'), ('Windows Bitmap', '*.bmp'),
                     ('JPEG / JFIF', '*.jpg'), ('CompuServer GIF', '*.gif')]

   # To open the dialog box for saving the file
   photo = fd.asksaveasfilename(initialdir="/", title="SELECT A DIRECTORY", filetypes=filetypes)
   if photo:
      the_image.save(photo)

def quit():
   exit()


def restart():
   print("Button activated")
   # ----- Need a way to restart the window  for another  photo ----- #
   # Delete all widgets from the window
   # window.destroy()
   # initial_window()


# def initial_window():
# global window


# -------- Widget Definition Area ----------- #

# Todo 1 configure the starting presentation window.
window = tk.Tk()
window.title('App for Adding a Watermark to a Photo by Pedro Hernandez')
window.geometry('400x400')
window.config(background=BACK_COLOR, highlightbackground=DARKGREY, highlightthickness=7)


# Todo 2 Add Initial Label.
# add a Title Label
title_label = Label(window, text='Please, Choose Your Image', width=30, font=FONT_1, bg=BACK_COLOR)
title_label.pack(pady=20)

# Todo 3 add the image browsing/loading button.
# Create a button to display the text of entry widget
button = ttk.Button(window, text="Choose Image", command=select_files, padding=4)
button.pack(pady=5)

# Todo 4 Add a input box for watermark text.
# add a box for input the watermark text
water_label = Label(window, text="Add the Watermark text", font=FONT_2, bg=BACK_COLOR)
water_label.pack(pady=10)
texto = Entry(window, font=FONT_2, width=30)
texto.pack(pady=3)

# Todo 5  Add a button for download the final product and a box foe adding the new location for the file.
water_button = ttk.Button(window, text="Apply the Watermark", command=create_watermark, padding=5)
water_button.pack(pady=5)

want_to_save = ttk.Button(window, text="Save Your Photo", command=photo_saver, padding=3)
want_to_save.pack(side=TOP, anchor=N, expand=True, pady=10)

# todo 6 add a button for leaving the app or to watermark another photo.
leave_fmr = tk.Frame(window, relief=tk.RAISED, bd=3)
leave = ttk.Button(leave_fmr, text="QUIT", command=quit)
leave.pack(side=BOTTOM, anchor=N, expand=True)
leave_fmr.pack(side=BOTTOM, anchor=N, expand=True)

# todo 7 add a button for restarting the program
one_fmr = tk.Frame(window, relief=tk.RAISED, bd=3)
one_more = ttk.Button(one_fmr, text="Restart", command=restart)
one_more.pack(side=RIGHT, anchor=N, expand=True)
one_fmr.pack(side=RIGHT, anchor=N, expand=True)


window.pack_propagate(False)  # disable window size propagation
window.mainloop()

#main

#import necessary libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

from Upload_Save import upload,save




#open a dialog box displaying options to select an image
top=tk.Tk()
top.geometry('400x400')
top.title('Image Cartoonification! Select-Cartoonify-Save ')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

#display a button to select image from any file or folder 
upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)  
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)

top.mainloop()  #used to block any event until tkinter box is active








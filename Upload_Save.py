#Upload and Save the cartoonified image

#import necessary libraries

import cv2 
import easygui   
import numpy as np 
import imageio

import tkinter as tk
import sys
import os

from Image_Cartoonification import cartoonify

def upload():
    image_path=easygui.fileopenbox()
    cartoonify(image_path)

def save(image_cartoon, image_path):

    #read the directory and name of original image file
    path1 = os.path.dirname(image_path)
    name_old=os.path.basename(image_path)

    #modify the name to avoid file replacements when working with different images
    name_new="Cartoonified_Image-"+name_old
    path = os.path.join(path1, name_new)

    #file will be saved in the same path
    cv2.imwrite(path, cv2.cvtColor(image_cartoon, cv2.COLOR_RGB2BGR))
    I= "Image is saved as " + name_new +" at "+ path
    tk.messagebox.showinfo(title=None, message=I)

    
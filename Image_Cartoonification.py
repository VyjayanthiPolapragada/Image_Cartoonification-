#Cartoonification of an image

#import necessary libraries

#libraries for image processing
import cv2 
import easygui   
import numpy as np 
import imageio  

#libraries for cartoonification options (pop up)
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import sys
import matplotlib.pyplot as plt
import os

#import save function
from Upload_Save import save

def cartoonify(image_path):

    image_org = cv2.imread(image_path) #read the original image


    image_org = cv2.cvtColor(image_org, cv2.COLOR_BGR2RGB) #change the color format as cv2 reads BGR by default
    

    # exit if choosen file is not an image
    if image_org is None:
        print("Error! Please choose an image file")
        sys.exit()

   
    image_gray= cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY) #convert from bgr to gray


    #smoothening image using median blur
    gray_smooth = cv2.medianBlur(image_gray, 5)

   
    #edges are retreived for cartoon effect using threshold technique
    image_edges = cv2.adaptiveThreshold(gray_smooth, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)



    #removing noise from image using bilateral filter while edges are sharp
    image_filter = cv2.bilateralFilter(image_org, 9, 300, 300)


    #masing both edged and filtered images to get cartoon effect
    image_cartoon = cv2.bitwise_and(image_filter, image_filter, mask=image_edges)


    #display the transition of image from color to cartoon effect

    #resize for better oreintation and display
    image1 = cv2.resize(image_org, (960, 540))  
    image2 = cv2.resize(image_gray, (960, 540))  
    image3 = cv2.resize(gray_smooth, (960, 540))
    image4 = cv2.resize(image_edges, (960, 540))
    image5 = cv2.resize(image_filter, (960, 540))
    image6 = cv2.resize(image_cartoon, (960, 540))


    images=[image1, image2,image3,image4,image5,image6]

    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    #after the successful transition, display another button to save the catoonified image
    save_image=Button(top,text="Save Cartoonified Image",command=lambda: save(image_cartoon, image_path),padx=30,pady=5)
    save_image.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save_image.pack(side=TOP,pady=50)
    
    plt.show()



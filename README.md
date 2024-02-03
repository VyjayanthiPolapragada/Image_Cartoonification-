# Image Cartoonification 
Apply cartoon effect to images using opencv with python

Different functions are used to apply cartoon effects and save the image

1. upload_save.py : contains functions to upload the image file from a folder and save the cartoonified image to the same folder
2. image_cartoonification.py : used to apply cartoon effect on the selected images

Cartoon effect is applied using the following steps for an image (each image transition is plotted after final output) : 
1. Read the image using opencv
2. Convert to gray scale and apply median blur to smoothen the image
3. Retreive edges using adaptive threshold technique (efficient when detailed edges are required)
4. Apply bilateral filter to RGB image (this ensures smoothness but edges remain sharp)
5. Mask both filtered and edged images to obtain cartoon effect

main.py consists of the main code to initiate a tkinter event (dialog box) to uplaod the image (using easygui) and save the image to the original path

Libraries used: opencv,numpy,tkinter,PIL,easygui,imageio,matplotlib,os,sys (except easygui other libraries are in-built jupyter notebook)

*Sample images and their output is attached above




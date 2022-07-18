import glob
import os
import shutil
import tkinter
from tkinter import *

import PIL
from PIL import Image, ImageTk


def pic_info():  # sourcery skip: assign-if-exp
   print(root.grid_size)
   print(root.grid)
   print(canvas.canvasx)
   
   ''' tracker = tracker1
    
    1 == on
    0 == off
    
    nUm = "no"
    for _ in range(1):
        if tracker == 1:
            nUm = "yes"
        else:
            break
    labelframe.pack(fill="both", expand="yes")
    left = Label(labelframe, text="Inside the LabelFrame")
    left.pack()
    if nUm == "no":
        tracker1 = 1 #yes
    else:
        tracker1 = 0 #no'''

root = Tk()
root.iconbitmap("ponyo.ico")
root.title("ponko")
canvas = Canvas(root,background="#666666", width = 960, height = 974)
canvas.pack()
#canvas.create_image(0, 0, anchor=NW, image=img)
labelframe = LabelFrame(root, text="This is a LabelFrame")
  

info_button = tkinter.Button(root, text="info", command=pic_info)
info_button.pack()
root.mainloop() 
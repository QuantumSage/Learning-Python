# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:42:35 2022

@author: Quantum Sage
"""

import numpy as np
from PIL import Image
width=5
height=4
array=np.zeros([height,width,3],dtype=np.uint8) #3 is the colorcodes RGB and uint8 is just int with 8 bytes
img=Image.fromarray(array)
img.save("test.png")
array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0]
array1[:,100:]=[0,0,255]
img=Image.fromarray(array1)
img.save("test1.png")
im=Image.open("test1.png")
rgb_im=im.convert("RGB")
r,g,b=rgb_im.getpixel((150,1))
print(r,g,b)




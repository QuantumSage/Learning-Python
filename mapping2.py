# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:34:12 2022

@author: Quantum Sage
"""

from PIL import Image
import random

img=Image.open("pn.png") #no images provided and the ones on internet were artifacted so color grading wont match
rgb_im=img.convert("RGB")
count_pun=0
count_in=0
count=0
while(count<=10000):
    x=random.randint(0,300)
    y=random.randint(0,168)
    z=0
    r,g,b=rgb_im.getpixel((x,y))
    if(r==60):
        count_in=count_in+1
        count=count+1
    else:
        if(r==80):
            count_pun=count_pun+1
            count+=1

area=count_pun/count_in*3287263
print(area)

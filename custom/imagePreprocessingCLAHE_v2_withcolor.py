import numpy as np
import cv2

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html

directory_in_str="/media/RED/Thesis/Datensets/cct_images_bbox_all"

import os

directory = os.fsencode(directory_in_str)
targetdirectory="/media/Pool/Thesis/Datensets/cct_images_bbox_all_clahe_color"
#targetdirectory=os.path.join(directory_in_str,"clahe_out_color")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
        print(os.path.join(directory_in_str, filename))
        fileFullname=os.path.join(directory_in_str, filename)
        img = cv2.imread(fileFullname,1)
        # create a CLAHE object (Arguments are optional).
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        #clahe = cv2.createCLAHE()
        #cl1 = clahe.apply(img)
        #targetFilename=os.path.join(targetdirectory, filename)
        #cv2.imwrite(targetFilename,cl1)




        lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        #cv2.imshow('l_channel', l)
        #cv2.imshow('a_channel', a)
        #cv2.imshow('b_channel', b)

        #-----Applying CLAHE to L-channel-------------------------------------------
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        #cv2.imshow('CLAHE output', cl)

        #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
        limg = cv2.merge((cl,a,b))
        #cv2.imshow('limg', limg)

        #-----Converting image from LAB Color model to RGB model--------------------
        final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        #cv2.imshow('final', final)

        targetFilename=os.path.join(targetdirectory, filename)
        cv2.imwrite(targetFilename,final)







        continue
    else:
        continue




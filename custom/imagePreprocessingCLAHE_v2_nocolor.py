import numpy as np
import cv2

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html

directory_in_str="/media/RED/Thesis/Datensets/cct_images_bbox_all"

import os

directory = os.fsencode(directory_in_str)
targetdirectory=os.path.join(directory_in_str,"clahe_out")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
        print(os.path.join(directory_in_str, filename))
        fileFullname=os.path.join(directory_in_str, filename)
        img = cv2.imread(fileFullname,0)
        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        targetFilename=os.path.join(targetdirectory, filename)
        cv2.imwrite(targetFilename,cl1)
        continue
    else:
        continue




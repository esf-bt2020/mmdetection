import numpy as np
import cv2



img = cv2.imread('/home/felice/Work/Git_Ext/esf-bt2020_mmdetection/custom/images/img01.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('/home/felice/Work/Git_Ext/esf-bt2020_mmdetection/custom/images/img01_out.jpg',cl1)
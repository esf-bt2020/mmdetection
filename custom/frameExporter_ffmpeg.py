#import cv2 
import os 

# Read the video from specified path 

rootpath = '/media/Pool/Thesis/Datensets/boku_extracted/SE10_ausgewertet'
videoname = '200714AA.TLV'
#filetype = ".m4v"

#cam = cv2.VideoCapture(rootpath + videoname + filetype) 

targetFolder = rootpath + videoname + 'frames/'

try: 
	
	# creating export folder if not exists
	if not os.path.exists(targetFolder): 
		os.makedirs(targetFolder) 

# if not created then raise error 
except OSError: 
	print ('Error: Creating directory of data') 

command = "ffmpeg -i " + rootpath + videoname + " -vcodec copy frame%d.jpg"
print(command)
import cv2 
import os 

# Read the video from specified path 

rootpath = '/home/felice/Videos/'
videoname = '200715AA_Frame502'
filetype = ".m4v"

cam = cv2.VideoCapture(rootpath + videoname + filetype) 

targetFolder = rootpath + videoname + 'frames/'

try: 
	
	# creating export folder if not exists
	if not os.path.exists(targetFolder): 
		os.makedirs(targetFolder) 

# if not created then raise error 
except OSError: 
	print ('Error: Creating directory of data') 

# frame 
currentframe = 0

while(True): 
	
	# reading from frame 
	ret,frame = cam.read() 

	if ret: 
		# if video is still left continue creating images 
		name = targetFolder + videoname + "_frame_" + str(currentframe) + '.jpg'
		print ('Creating...' + name) 

		# writing the extracted images 
		cv2.imwrite(name, frame) 

		# increasing counter so that it will 
		# show how many frames are created 
		currentframe += 1
	else: 
		break

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 

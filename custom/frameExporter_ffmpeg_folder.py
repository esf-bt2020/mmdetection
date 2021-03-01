#import cv2 
import os 

# Read the video from specified path 

rootpath = '/media/Pool/Thesis/Datensets/boku_extracted/SE10_ausgewertet/'
#videoname = '200714AA.TLV'
#filetype = ".m4v"


for filename in os.listdir(rootpath):
    if filename.endswith(".TLV"):
        targetFolder = rootpath + filename + 'frames/'
        # creating export folder if not exists
        if not os.path.exists(targetFolder): 
            os.makedirs(targetFolder)
            #print(targetFolder)
        # if not created then raise error 
        #except OSError: 
        #    print ('Error: Creating directory of data') 
        command = "ffmpeg -i '" + rootpath + filename + "' -vcodec copy '" + targetFolder + filename + "frame%d.jpg'"
        print(command)
        os.system(command)
        # print(os.path.join(directory, filename))
        continue
    else:
        continue
#cam = cv2.VideoCapture(rootpath + videoname + filetype) 





#command = "ffmpeg -i " + rootpath + videoname + " -vcodec copy frame%d.jpg"
#print(command)
import os

directory = r'C:\Temp\COCO_CONVERT\raubtierv2_b\test'
for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		fullfilename =os.path.join(directory, filename)
		if ( ".rf" in fullfilename ):
			targetfilename = fullfilename.replace(".rf.", "")
			os.rename(fullfilename,targetfilename )
		else:
			continue
	else:
		continue
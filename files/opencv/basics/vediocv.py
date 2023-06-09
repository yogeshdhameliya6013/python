#importing the opencv module  
import cv2 as cv
import sys
import os
import numpy as np

# load vedio from file
#video = cv.VideoCapture('files/opencv/sample.mp4',0)
# it will run the camera 
video = cv.VideoCapture(0)

# status of file or vedio it wil return True or False
print(video.isOpened())

# get the properties of veio frame

print(video.get(cv.CAP_PROP_FRAME_WIDTH))
print(video.get(cv.CAP_PROP_FRAME_HEIGHT))
print(video.get(cv.CAP_PROP_FPS))
print(video.get(cv.CAP_PROP_FRAME_COUNT))

# set the properties of veio frame

video.set(cv.CAP_PROP_FRAME_WIDTH,600)
video.set(cv.CAP_PROP_FRAME_HEIGHT,600)

print(video.get(cv.CAP_PROP_FRAME_WIDTH))
print(video.get(cv.CAP_PROP_FRAME_HEIGHT))

#fourcc is a vedio code .avi *'MP4V'
fourcc = cv.VideoWriter_fourcc(*'XVID')
# to write a vedio ,30 is FPS and width,height(640,480)
output = cv.VideoWriter('New-vedio.avi',fourcc,30,(1280,720))



while (video.isOpened()) :
    # it will read the vedio frame from camera ,ret is boolean True if frame is available 
    ret,frame =video.read()
    
    if ret == True :
        
        #convert BGR vedio frame to Gray 
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        #convert BGR vedio frame to RGB
        rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

        # Write a video , you can pass original frame or converted frame
        output.write(rgb)
        #it will run the vedio frame on window
        cv.imshow("My Vedio",rgb)
        cv.imshow("grat Vedio",gray)

        #for camera value is 1
        key = cv.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        else :
            break

# to release the resources from memory ie camera
video.release()
output.release()
#to destroy all opened windows.
#cv.destroyAllWindow()

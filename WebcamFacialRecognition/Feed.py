import os.path
import cv2
import numpy as np

def count_pixels(img):
	(h, w, d) = img.shape
	print "Height: {0}, Width: {1}".format(h, w)
	
def analyze_face_roi(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	
	for (x,y,w,h) in faces:
    		print "x: {0}, y: {1}".format(x, y)
    		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    		save_image(0, img)
    		#cv2.imshow('img',img)
    	if not faces:
    		print "No faces."
	
def save_image(i, img):
    """Checks to see if image file name is free and saves the web cam feed"""
    
    fileName = "WebcamFeed_" + str(i) + ".png"
    if os.path.isfile(fileName):
        save_image(i + 1, img)
    else:
        cv2.imwrite(fileName, img)
        count_pixels(img)
        print 'Saved camera image: ' + "\"" + fileName + "\""
        
        
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Webcam", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    elif key == ord('s'):
		#save_image(0, frame)
		analyze_face_roi(frame)
        
cv2.destroyWindow("Webcam")
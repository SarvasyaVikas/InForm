import cv2
import numpy as np
import fnmatch
import os
import argparse
import csv
import time

vid = cv2.VideoCapture('InForm-5VID-Data-MP4.mp4')

centersX = []
centersY = []

cX = 0
cY = 0

def Interact(action, x, y, flags, *userdata):
	global counter
	global LX
	global TY
	global RX
	global BY

	if action == cv2.EVENT_LBUTTONDBLCLK:
		print('CLICK')
		cX = x
		cY = y
		print([cX, cY])
		cv2.circle(frame, (cX, cY), radius = 5, color = (0, 0, 255), thickness = -1)
	
	if action == cv2.EVENT_MBUTTONDOWN:
		cX = 0
		cY = 0
		print("RESET")


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", Interact)

fr = 0
while (vid.isOpened()):
    ret, frame = vid.read()
    if ret:
    	if fr % 5 == 0:
    		while True:
    			frame = cv2.resize(frame, (640, 360))
    			cv2.imshow("Image", frame)
    			if cv2.waitKey(10) & 0xFF == ord('q'):
    				print("NEXT")
    				print(fr)
    				break
    			
    			centersX.append(cX)
    			centersY.append(cY)
    fr += 1

vid.release()

csvfile = open("InForm-Tennis-Serve-AC.csv", "a+")
csvwriter = csv.writer(csvfile)

for row in range(len(centersX)):
	print("start save")
	dtype = "Tennis_Serve"
	lst = [dtype, row + 1]
	for i in range(4):
		lst.append(centersX[row + 1])
		lst.append(centersY[row + 1])
	
	csvwriter.writerow(lst)

csvfile.close()

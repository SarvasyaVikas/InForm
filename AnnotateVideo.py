import cv2
import numpy as np
import fnmatch
import os
import argparse
import csv
import time

vid = cv2.VideoCapture('InForm-5VID-Data-MP4.mp4')

LXs = []
RXs = []
TYs = []
BYs = []

LX = 0
TY = 0
RX = 0
BY = 0
	
counter = 0

def Interact(action, x, y, flags, *userdata):
	global counter
	global LX
	global TY
	global RX
	global BY

	if action == cv2.EVENT_LBUTTONDBLCLK:
		print('CLICK')
		if counter >= 0:
			counter += 1
			if counter == 1:
				LX = x
				TY = y
			elif counter == 2:
				RX = x
				BY = y
				temp = image.copy()
				cv2.rectangle(temp, (LX, TY), (RX, BY), (0, 0, 255), 2)
				cv2.imshow("Image", temp)
				cv2.waitKey(10)
				
	if action == cv2.EVENT_MBUTTONDOWN:
		counter = 0
		LX = 0
		TY = 0
		RX = 0
		BY = 0
		temp = image.copy()
		print("RESET")
	
	if counter == 1:
		temp = image.copy()
		cv2.rectangle(temp, (LX, TY), (x, y), (0, 255, 0), 2)
		init = time.time()
		while (time.time() - init) < 0.01:
			cv2.imshow("Image", temp)


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", Interact)

while (vid.isOpened()):
    ret, frame = vid.read()
    if ret:
        while True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                    counter = 0
                    break

        lx = min(LX, RX)
        rx = max(LX, RX)
        ty = min(TY, BY)
        by = max(TY, BY)

        LXs.append(lx)
        RXs.append(rx)
        TYs.append(ty)
        BYs.append(by)

        else:
            break

vid.release()

csvfile = open("InForm-Tennis-Serve-AC.csv", "a+")
csvwriter = csv.writer(csvfile)

for row in range(len(LXs)):
	dtype = "Tennis_Serve"
	lst = [dtype, row + 1]
	for i in range(4):
		lst.append(LXs[row + 1])
		lst.append(TYs[row + 1])
		lst.append(RXs[row + 1])
		lst.append(BYs[row + 1])
	
	csvwriter.writerow(lst)

csvfile.close()

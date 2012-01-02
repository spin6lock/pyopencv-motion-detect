# -*- coding:utf8 -*-

import opencv
from opencv import highgui as hg

capture= hg.cvCreateCameraCapture(0)
hg.cvNamedWindow("Snapshot")

frames = []
for i in range(10):
	frame = hg.cvQueryFrame(capture)
	frames.append(opencv.cvClone(frame))
	hg.cvShowImage("Snapshot", frame)
	hg.cvWaitKey(1000)

hg.cvNamedWindow("hello")
for i in range(10):
	frame = frames[i]
	hg.cvShowImage("hello", frame)
	hg.cvWaitKey(1000)

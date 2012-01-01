# -*- coding:utf8 -*-

from opencv import highgui as hg
capture= hg.cvCreateCameraCapture(0)
hg.cvNamedWindow("Snapshot")
for i in range(10):
	frame = hg.cvQueryFrame(capture)
	hg.cvShowImage("Snapshot", frame)
	hg.cvWaitKey(1000)

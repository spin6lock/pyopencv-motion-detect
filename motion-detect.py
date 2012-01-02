# -*- coding:utf8 -*-
import opencv
from opencv import highgui as hg
capture = hg.cvCreateCameraCapture(0)
hg.cvNamedWindow("Snapshot")
frames = []
for i in range(10):
	frame = hg.cvQueryFrame(capture)
	frames.append(frame)
	hg.cvShowImage("Snapshot", frame)
hg.cvWaitKey(1000)

hg.cvNamedWindow("hello")
for i in range(10):
	hg.cvShowImage("hello", frames[i])
	hg.cvWaitKey(1000)
"""
import copy
dst=copy.copy(frames[1])
opencv.cvSub(frames[2], frames[1], dst)
hg.cvShowImage("Snapshot", dst)
from IPython.Shell import IPShellEmbed
IPShellEmbed()()
hg.cvWaitKey(10000)
"""

from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap=cv2.VideoCapture('vtest.avi')
while(True):
    _,image=cap.read()
    image=imutils.resize(image,width=min(400,image.shape[1]))

    (rects,weights)=hog.detectMultiScale(image,winStride=(4,4),padding=(8,8),scale=1.05)


    rects=np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])
    pick=non_max_suppression(rects,probs=None,overlapThresh=0.65)

    for (xA,yA,xB,yB) in pick:
        cv2.rectangle(image,(xA,yA),(xB,yB),(0,255,0),2)

    cv2.imshow('result',image)
    key=cv2.waitKey(0)

    if key==27:
        break

cap.release()
cv2.destroyAllWindows()

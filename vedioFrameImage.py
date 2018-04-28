
# -*- coding: UTF-8 -*-

#######视频保存每一帧为图片#####

import cv2
import numpy

cap = cv2.VideoCapture("/Users/huan/Downloads/00000.MTS")
frames = 1
person = 1
count = 1

while cv2.waitKey(30)!=ord('q'):
    retval, image = cap.read()
    if count%60==0:
        #cv2.imwrite("./image1/%4d_%2d.png" % (frames, person), image)
        cv2.imwrite("/Users/huan/code/PycharmProjects/PedestrianDetection/images2/%04d_%02d.png" % (frames,person),image)
        cv2.imshow("video",image)
        frames = frames+1
        person = person + 1
    count = count+1
cap.release()


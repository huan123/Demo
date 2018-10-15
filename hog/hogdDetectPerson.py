 # import the necessary packages
# -*- coding: utf-8 -*-
from __future__ import print_function #确保代码同时在Python2.7和Python3上兼容
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils   #安装库pip install imutils ；pip install --upgrade imutils更新版本大于v0.3.1
import cv2

image = cv2.imread("1.bmp")
image = imutils.resize(image, width=min(400, image.shape[1]))
origin = image.copy()
# 初始化我们的行人检测器
hog = cv2.HOGDescriptor()   #初始化方向梯度直方图描述子
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  #设置支持向量机(Support Vector Machine)使得它成为一个预先训练好了的行人检测器

# detect people in the image：
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
        padding=(8, 8), scale=1.05)

#应用非极大抑制方法，通过设置一个阈值来抑制那些重叠的边框
rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
# draw the final bounding boxes
for (xA, yA, xB, yB) in pick:
    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
cv2.imshow("origin",origin)
cv2.imshow("image",image)
cv2.waitKey(0)
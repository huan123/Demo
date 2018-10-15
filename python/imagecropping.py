# -*- coding: utf-8 -*-
import cv2
image = cv2.imread("1.bmp")
frames = 1
person =1
origin = image.copy()
x = 10
y = 10
w = 10
h = 10
rect = image[y:y+h,x:x+h]
cv2.imwrite("./images1/%04d_%02d.bmp"%(frames,person),rect)#写入文件
#原始图
cv2.imshow("origin",origin)
#裁剪的图
cv2.imshow("rect",rect)
cv2.waitKey(0)
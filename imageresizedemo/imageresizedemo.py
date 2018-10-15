# -*- coding: utf-8 -*-
import cv2



def t():
    image = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/images/0029_29.png"
    src = cv2.imread(image)

    src = cv2.resize(src, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)

    cv2.imshow("hha",src)
    cv2.waitKey(0)

t()
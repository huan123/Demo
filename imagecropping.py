import cv2
image = cv2.imread("1.bmp")
origin = image.copy()
cv2.imshow("origin",origin)
x = 10
y = 10
w = 10
h = 10
rect = image[y:y+h,x:x+h]
cv2.imshow("rect",rect)
cv2.waitKey(0)
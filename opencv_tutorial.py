import cv2
import numpy as np

img = cv2.imread("v2_train/image1.jpg")
imgCanny = cv2.Canny(img, 50,50)


cv2.imshow("Base", img)
cv2.imshow("Canny", imgCanny)
cv2.waitKey(0)

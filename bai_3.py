import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread(r"C:\Users\Luong Hieu\Music\de_test_pencv\anh3.png")
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
imgray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img1, contours, -1, (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
img1 = cv2.imread(r"C:\Users\Luong Hieu\Music\de_test_pencv\anh1.png")
img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow('img', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


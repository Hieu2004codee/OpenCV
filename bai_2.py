import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r"C:\Users\Luong Hieu\Music\de_test_pencv\anh2.PNG")
kernel = np.ones((25, 25), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.subplot(121), plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(opening)
plt.title('opening Image'), plt.xticks([]), plt.yticks([])
plt.show()



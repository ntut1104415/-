import cv2
import numpy as np

if __name__ == __main__:

img = cv2.imread("image.jpg")

cv2.nameWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyALLWindows()

# 垂直镜像， 水平镜像
import cv2
import numpy as np

img = cv2.imread("../data/Linus.png")
cv2.imshow("image", img)

# 垂直镜像
img_flip_vertical = cv2.flip(img, 0)

# 水平镜像
img_flip_horizontal = cv2.flip(img, 1)
cv2.imshow("image_flip_vertical", img_flip_vertical)
cv2.imshow("image_flip_horizontal", img_flip_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

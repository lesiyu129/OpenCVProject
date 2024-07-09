# 图像缩放示例
import numpy as np
import cv2

im = cv2.imread("../data/Linus.png")
cv2.imshow("Linus", im)

h, w = im.shape[:2]

dst_size = (int(w / 2), int(h / 2))
dst = cv2.resize(im, dst_size)
cv2.imshow("Linus_resize", dst)
# 最邻近插值
dst_size = (200, 300)  # 缩放尺寸
dst = cv2.resize(im, dst_size, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Linus_resize_nearest", dst)
# 双线性插值
dst_size = (200, 300)  # 缩放尺寸
dst = cv2.resize(im, dst_size, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Linus_resize_linear", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

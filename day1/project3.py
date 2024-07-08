# 灰度直方图均衡化
from matplotlib import pyplot as plt
import cv2
import numpy as np

# 直接读取灰度图
img = cv2.imread("../data/sunrise.jpg", 0)
cv2.imshow("img", img)
im_equ = cv2.equalizeHist(img)
cv2.imshow("im_equ", im_equ)


# 绘制图像直方图
# 扁平化
img_ravel = img.ravel()
# 直方图
plt.subplot(2, 1, 1)
plt.hist(img_ravel, 256, (0.0, 256.0), label="img")
plt.legend()

plt.subplot(2, 1, 2)
plt.hist(im_equ.ravel(), 256, (0.0, 256.0), label="im_equ")
plt.legend()
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

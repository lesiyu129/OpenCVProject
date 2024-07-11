# 轮廓检测

import cv2

img = cv2.imread("../data/3.png", 1)
# print(img.shape)
# 灰度化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)
# cv2.imshow("img", img)

# 二值化
t, img_gray_threshold = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓

contours, hierarchy = cv2.findContours(
    img_gray_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)
drawContours_img = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
cv2.imshow("img", drawContours_img)
print(contours)
cv2.waitKey()
cv2.destroyAllWindows()
